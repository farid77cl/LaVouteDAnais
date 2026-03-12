# ══════════════════════════════════════════════════════════════════
# LA VOÛTE D'ANAÏS — Script de Instalación para Windows
# PowerShell 5.1+ / Windows 10 o Windows 11
# Uso: Click derecho sobre el archivo → "Ejecutar con PowerShell"
#      O desde PowerShell como Administrador:
#      Set-ExecutionPolicy Bypass -Scope Process -Force
#      .\setup.ps1
# ══════════════════════════════════════════════════════════════════

#Requires -Version 5.1

param(
    [string]$ProjectDir = "$env:USERPROFILE\lavoutedanais"
)

# ── Verificar que se ejecuta como Administrador ──────────────────
$currentPrincipal = [Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
$isAdmin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host ""
    Write-Host "  Este script necesita permisos de Administrador." -ForegroundColor Red
    Write-Host "  Click derecho sobre el archivo → Ejecutar con PowerShell" -ForegroundColor Yellow
    Write-Host "  O abre PowerShell como Administrador y ejecuta el script." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Presiona Enter para cerrar"
    exit 1
}

# ── Funciones de output ──────────────────────────────────────────
function Log    { param($msg) Write-Host "  [OK] $msg" -ForegroundColor Green }
function Warn   { param($msg) Write-Host "  [!]  $msg" -ForegroundColor Yellow }
function Err    { param($msg) Write-Host "  [X]  $msg" -ForegroundColor Red }
function Section{ param($msg) Write-Host "`n══ $msg ══`n" -ForegroundColor Cyan }
function Ask    { param($msg) Write-Host "  [?]  $msg" -ForegroundColor Magenta }

# ── Banner ───────────────────────────────────────────────────────
Clear-Host
Write-Host ""
Write-Host "  ⬡  ✦  ⬡" -ForegroundColor DarkYellow
Write-Host ""
Write-Host "  LA VOUTE D'ANAIS" -ForegroundColor White
Write-Host "  Sistema de Instalacion para Windows" -ForegroundColor Gray
Write-Host ""
Write-Host "  Directorio del proyecto: $ProjectDir" -ForegroundColor Gray
Write-Host ""

# ══════════════════════════════════════════════════════════════════
Section "1. Verificacion del Sistema"
# ══════════════════════════════════════════════════════════════════

$osInfo  = Get-CimInstance Win32_OperatingSystem
$ramGB   = [math]::Round($osInfo.TotalVisibleMemorySize / 1MB)
$diskInfo= Get-PSDrive C
$diskGB  = [math]::Round($diskInfo.Free / 1GB)
$winVer  = $osInfo.Caption
$winBuild= $osInfo.BuildNumber

Write-Host "  Sistema: $winVer (Build $winBuild)" -ForegroundColor Gray
Write-Host "  RAM:     ${ramGB}GB disponibles" -ForegroundColor Gray
Write-Host "  Disco C: ${diskGB}GB libres" -ForegroundColor Gray

if ($ramGB -lt 8)  { Warn "RAM menor a 8GB. Usar modelos cuantizados Q4." }
if ($diskGB -lt 50) { Warn "Menos de 50GB libres en C:. Los modelos LLM ocupan ~35GB." }

# Verificar Windows 10/11
if ([int]$winBuild -lt 19041) {
    Err "Se requiere Windows 10 version 2004 (Build 19041) o superior para WSL2."
    Read-Host "Presiona Enter para cerrar"
    exit 1
}

Log "Sistema verificado: $winVer"

# ══════════════════════════════════════════════════════════════════
Section "2. Activar WSL2 y Hyper-V"
# ══════════════════════════════════════════════════════════════════

Write-Host "  Verificando WSL2..." -ForegroundColor Gray

$wslStatus = Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -ErrorAction SilentlyContinue

if ($wslStatus.State -ne "Enabled") {
    Write-Host "  Activando WSL2 (requiere reinicio al final)..." -ForegroundColor Yellow
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart | Out-Null
    Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart | Out-Null
    $needsRestart = $true
    Log "WSL2 activado (se aplicará en el reinicio)"
} else {
    Log "WSL2 ya está activado"
}

# Hyper-V (necesario para Docker Desktop)
$hyperv = Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -ErrorAction SilentlyContinue
if ($hyperv -and $hyperv.State -ne "Enabled") {
    Write-Host "  Activando Hyper-V..." -ForegroundColor Yellow
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -NoRestart | Out-Null
    $needsRestart = $true
    Log "Hyper-V activado"
} else {
    Log "Hyper-V disponible"
}

# ══════════════════════════════════════════════════════════════════
Section "3. Instalar Winget (si no esta disponible)"
# ══════════════════════════════════════════════════════════════════

$winget = Get-Command winget -ErrorAction SilentlyContinue
if (-not $winget) {
    Write-Host "  Instalando App Installer (winget)..." -ForegroundColor Yellow
    $wingetUrl = "https://aka.ms/getwinget"
    $wingetPath = "$env:TEMP\AppInstaller.msixbundle"
    Invoke-WebRequest -Uri $wingetUrl -OutFile $wingetPath -UseBasicParsing
    Add-AppxPackage -Path $wingetPath
    Log "winget instalado"
} else {
    Log "winget disponible: $(winget --version)"
}

# ══════════════════════════════════════════════════════════════════
Section "4. Instalar Docker Desktop"
# ══════════════════════════════════════════════════════════════════

$dockerCmd = Get-Command docker -ErrorAction SilentlyContinue
$dockerDesktop = Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Where-Object { $_.DisplayName -like "*Docker Desktop*" } -ErrorAction SilentlyContinue

if ($dockerDesktop) {
    Log "Docker Desktop ya está instalado"
} else {
    Write-Host "  Descargando Docker Desktop..." -ForegroundColor Yellow
    Write-Host "  (puede tardar varios minutos según tu conexión)" -ForegroundColor Gray

    $dockerUrl      = "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe"
    $dockerInstaller= "$env:TEMP\DockerDesktopInstaller.exe"

    try {
        # Intentar con winget primero (más rápido)
        Write-Host "  Intentando instalar via winget..." -ForegroundColor Gray
        winget install -e --id Docker.DockerDesktop --silent --accept-package-agreements --accept-source-agreements
        Log "Docker Desktop instalado via winget"
    } catch {
        # Fallback: descarga directa
        Write-Host "  Descargando instalador directo..." -ForegroundColor Gray
        Invoke-WebRequest -Uri $dockerUrl -OutFile $dockerInstaller -UseBasicParsing
        Write-Host "  Ejecutando instalador (sigue las instrucciones en pantalla)..." -ForegroundColor Yellow
        Start-Process -FilePath $dockerInstaller -ArgumentList "install --quiet --accept-license" -Wait
        Log "Docker Desktop instalado"
    }

    $needsRestart = $true
}

# ══════════════════════════════════════════════════════════════════
Section "5. Crear Estructura del Proyecto"
# ══════════════════════════════════════════════════════════════════

# Crear directorio principal
New-Item -ItemType Directory -Force -Path $ProjectDir | Out-Null

# Estructura de carpetas del universo
$dirs = @(
    "voute_data\00_Canon",
    "voute_data\01_Personajes",
    "voute_data\02_Arcos",
    "voute_data\03_Literatura\en_progreso",
    "voute_data\03_Literatura\finalizados",
    "voute_data\03_Literatura\publicados",
    "voute_data\04_Memoria",
    "biblioteca\data",
    "n8n_workflows",
    "prompts",
    "scripts",
    "backups"
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Force -Path "$ProjectDir\$dir" | Out-Null
}

Log "Estructura de directorios creada en $ProjectDir"

# ══════════════════════════════════════════════════════════════════
Section "6. Generar Credenciales y archivo .env"
# ══════════════════════════════════════════════════════════════════

# Generar contraseñas aleatorias seguras
function New-RandomPassword {
    param([int]$Length = 16)
    $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    $password = -join ((1..$Length) | ForEach-Object { $chars[(Get-Random -Max $chars.Length)] })
    return $password
}

$POSTGRES_PASSWORD = New-RandomPassword -Length 20
$N8N_KEY = New-RandomPassword -Length 32

$envContent = @"
# ── Credenciales ─────────────────────────────────────────────
POSTGRES_PASSWORD=$POSTGRES_PASSWORD
N8N_ENCRYPTION_KEY=$N8N_KEY

# ── Ollama ───────────────────────────────────────────────────
OLLAMA_HOST=http://ollama:11434
OLLAMA_TIMEOUT=300

# ── Configuracion del universo ───────────────────────────────
VOUTE_DATA_PATH=./voute_data
MAX_EDIT_LOOPS=2
MIN_QUALITY_SCORE=7
"@

$envContent | Out-File -FilePath "$ProjectDir\.env" -Encoding UTF8
Log ".env creado con credenciales seguras"

# ══════════════════════════════════════════════════════════════════
Section "7. Crear docker-compose.yml"
# ══════════════════════════════════════════════════════════════════

$composeContent = @'
version: "3.9"

networks:
  voute_net:
    driver: bridge

volumes:
  n8n_data:
  ollama_data:
  postgres_data:
  redis_data:

services:

  # ── PostgreSQL ───────────────────────────────────────────────
  postgres:
    image: postgres:16-alpine
    container_name: voute_postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: voute_db
      POSTGRES_USER: voute_user
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks: [voute_net]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U voute_user -d voute_db"]
      interval: 10s
      timeout: 5s
      retries: 5

  # ── Redis ────────────────────────────────────────────────────
  redis:
    image: redis:7-alpine
    container_name: voute_redis
    restart: unless-stopped
    networks: [voute_net]
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5

  # ── Ollama (servidor LLM local) ──────────────────────────────
  ollama:
    image: ollama/ollama:latest
    container_name: voute_ollama
    restart: unless-stopped
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    networks: [voute_net]
    # ── Para GPU NVIDIA: descomenta estas lineas ──
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: all
    #           capabilities: [gpu]

  # ── n8n (orquestador de agentes) ─────────────────────────────
  n8n:
    image: n8nio/n8n:latest
    container_name: voute_n8n
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - DB_POSTGRESDB_PORT=5432
      - DB_POSTGRESDB_DATABASE=voute_db
      - DB_POSTGRESDB_USER=voute_user
      - DB_POSTGRESDB_PASSWORD=${POSTGRES_PASSWORD}
      - N8N_ENCRYPTION_KEY=${N8N_ENCRYPTION_KEY}
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - WEBHOOK_URL=http://localhost:5678
      - OLLAMA_HOST=http://ollama:11434
      - EXECUTIONS_DATA_SAVE_ON_SUCCESS=all
      - EXECUTIONS_DATA_SAVE_ON_ERROR=all
      - N8N_LOG_LEVEL=info
    volumes:
      - n8n_data:/home/node/.n8n
      - ./voute_data:/voute_data
      - ./prompts:/prompts:ro
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      ollama:
        condition: service_started
    networks: [voute_net]

  # ── Biblioteca Web ───────────────────────────────────────────
  biblioteca:
    image: nginx:alpine
    container_name: voute_biblioteca
    restart: unless-stopped
    ports:
      - "8080:80"
    volumes:
      - ./biblioteca:/usr/share/nginx/html:ro
    networks: [voute_net]

  # ── Pandoc (conversor Markdown a PDF) ────────────────────────
  pandoc:
    image: pandoc/extra:latest
    container_name: voute_pandoc
    restart: unless-stopped
    volumes:
      - ./voute_data:/voute_data
    networks: [voute_net]
    entrypoint: ["tail", "-f", "/dev/null"]
'@

$composeContent | Out-File -FilePath "$ProjectDir\docker-compose.yml" -Encoding UTF8
Log "docker-compose.yml creado"

# ══════════════════════════════════════════════════════════════════
Section "8. Crear scripts de gestion (.bat)"
# ══════════════════════════════════════════════════════════════════

# voute-start.bat
@"
@echo off
title La Voute d'Anais - Iniciando...
cd /d "%~dp0"
echo Iniciando La Voute d'Anais...
docker compose up -d
echo.
echo Servicios disponibles:
echo   n8n (flujos):    http://localhost:5678
echo   Biblioteca:      http://localhost:8080
echo   Ollama API:      http://localhost:11434
echo.
pause
"@ | Out-File -FilePath "$ProjectDir\voute-start.bat" -Encoding ASCII

# voute-stop.bat
@"
@echo off
title La Voute d'Anais - Deteniendo...
cd /d "%~dp0"
echo Deteniendo servicios...
docker compose down
echo Servicios detenidos.
pause
"@ | Out-File -FilePath "$ProjectDir\voute-stop.bat" -Encoding ASCII

# voute-logs.bat
@"
@echo off
title La Voute d'Anais - Logs
cd /d "%~dp0"
docker compose logs -f
"@ | Out-File -FilePath "$ProjectDir\voute-logs.bat" -Encoding ASCII

# voute-status.bat
@"
@echo off
title La Voute d'Anais - Estado
cd /d "%~dp0"
echo Estado de contenedores:
docker compose ps
echo.
echo Modelos en Ollama:
docker exec voute_ollama ollama list 2>nul || echo Ollama no disponible aun
echo.
pause
"@ | Out-File -FilePath "$ProjectDir\voute-status.bat" -Encoding ASCII

# voute-modelos.bat
@"
@echo off
title La Voute d'Anais - Descargar Modelos
cd /d "%~dp0"
echo Descargando modelos LLM...
echo Esto puede tardar 30-90 minutos segun tu conexion.
echo Espacio necesario: ~35GB
echo.

echo [1/3] dolphin-mixtral (escritura principal, ~26GB)...
docker exec voute_ollama ollama pull dolphin-mixtral

echo [2/3] dolphin-llama3 (edicion, ~5GB)...
docker exec voute_ollama ollama pull dolphin-llama3

echo [3/3] llama3.1:8b (coordinacion, ~5GB)...
docker exec voute_ollama ollama pull llama3.1:8b

echo.
echo Modelos descargados. Verificando...
docker exec voute_ollama ollama list
echo.
pause
"@ | Out-File -FilePath "$ProjectDir\voute-modelos.bat" -Encoding ASCII

# voute-modelos-lite.bat (para PCs con poca RAM)
@"
@echo off
title La Voute d'Anais - Modelos Ligeros
cd /d "%~dp0"
echo Descargando modelos LIGEROS (Q4 cuantizados, ~10GB total)...
echo Recomendado si tienes menos de 16GB de RAM.
echo.

echo [1/2] dolphin-llama3:8b-q4_0 (~4GB)...
docker exec voute_ollama ollama pull dolphin-llama3:8b-q4_0

echo [2/2] llama3.1:8b (~5GB)...
docker exec voute_ollama ollama pull llama3.1:8b

echo.
echo Modelos ligeros descargados.
docker exec voute_ollama ollama list
echo.
pause
"@ | Out-File -FilePath "$ProjectDir\voute-modelos-lite.bat" -Encoding ASCII

# voute-test.bat
@"
@echo off
title La Voute d'Anais - Test
cd /d "%~dp0"
echo Verificando servicios...
echo.

curl -s -o nul -w "n8n:        HTTP %%{http_code}\n"        http://localhost:5678
curl -s -o nul -w "Ollama:     HTTP %%{http_code}\n"        http://localhost:11434
curl -s -o nul -w "Biblioteca: HTTP %%{http_code}\n"        http://localhost:8080

echo.
echo Test de generacion Ollama:
docker exec voute_ollama ollama run llama3.1:8b "Responde solo: Sistema OK" 2>nul
echo.
pause
"@ | Out-File -FilePath "$ProjectDir\voute-test.bat" -Encoding ASCII

# voute-backup.bat
@"
@echo off
title La Voute d'Anais - Backup
cd /d "%~dp0"
set DATE=%date:~6,4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%
set DATE=%DATE: =0%
set BACKUP=backups\%DATE%

echo Haciendo backup en %BACKUP%...
mkdir "%BACKUP%" 2>nul
xcopy /E /I /Q voute_data "%BACKUP%\voute_data" >nul

docker exec voute_n8n n8n export:workflow --all --output=/tmp/workflows.json 2>nul
docker cp voute_n8n:/tmp/workflows.json "%BACKUP%\n8n_workflows.json" 2>nul

echo Backup completado en: %BACKUP%
pause
"@ | Out-File -FilePath "$ProjectDir\voute-backup.bat" -Encoding ASCII

Log "Scripts .bat creados"

# ══════════════════════════════════════════════════════════════════
Section "9. Crear Archivos Base del Canon"
# ══════════════════════════════════════════════════════════════════

# Filosofia del universo
@"
# Filosofia de La Voute d'Anais

## Principios Fundamentales

### 1. La Superficie es Esencia
El exterior no oculta el interior: lo crea.
Brillo, gloss, perfeccion plastica como manifestacion de poder.

### 2. El Poder Requiere Sacrificio
Toda transformacion tiene un costo.
La identidad anterior debe morir para que nazca la nueva.

### 3. La Rendicion es Liberacion
Dejar de luchar es encontrar paz.
La sumision total libera de la carga de decidir.

### 4. Los Errores son Puertas
No hay casualidades, solo destinos.
La puerta equivocada abre el camino verdadero.

## Frases Canonicas

- "Superficie es todo. Brillo es poder." - Miss Doll
- "El poder requiere un sacrificio." - La Voute
- "Los errores son puertas." - La Mucama
- "La rendicion no es derrota. Es revelacion." - Anais
"@ | Out-File -FilePath "$ProjectDir\voute_data\00_Canon\filosofia.md" -Encoding UTF8

# Reglas de transformacion
@"
# Reglas de Transformacion de La Voute

## Reglas Narrativas

1. Toda transformacion es gradual, tiene etapas definidas
2. La resistencia interna precede siempre a la rendicion
3. El momento de quiebre debe ser inevitable, no forzado
4. La nueva identidad emerge, no se impone desde fuera
5. Cada transformacion deja una marca permanente

## Tipos de Rendicion

- Por reconocimiento: descubrir que siempre fue asi
- Por seduccion: el deseo vence a la resistencia
- Por agotamiento: la lucha se vuelve imposible
- Por revelacion: una verdad externa cambia todo

## Niveles de Explicitud

- sugerente: insinuaciones, sin descripcion directa
- sensual: escenas intimas con metaforas
- erotico: descripcion directa pero elegante
- erotico explicito: sin restricciones descriptivas
"@ | Out-File -FilePath "$ProjectDir\voute_data\00_Canon\reglas_transformacion.md" -Encoding UTF8

# Memoria inicial
@"
# Memoria de Sesiones - La Voute d'Anais

## Estado Actual del Universo

Fecha de ultimo relato: pendiente
Relatos publicados: 0 (sistema recien iniciado)
Personajes activos: Helena (etapa 3/5), Lilith (etapa 0/5)

## Proximos Pasos Narrativos

- Helena: avanzar hacia etapa 4 - El Reconocimiento
- Lilith: iniciar etapa 1 - La Puerta Equivocada
"@ | Out-File -FilePath "$ProjectDir\voute_data\04_Memoria\memoria_sesiones.md" -Encoding UTF8

Log "Archivos base del canon creados"

# ══════════════════════════════════════════════════════════════════
Section "10. Crear Biblioteca Web"
# ══════════════════════════════════════════════════════════════════

@"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>La Voute d'Anais - Biblioteca</title>
  <style>
    body { background:#0a0709; color:#f0e6d3; font-family:Georgia,serif;
           display:flex; align-items:center; justify-content:center;
           min-height:100vh; margin:0; text-align:center; }
    h1 { font-size:2.5rem; color:#f0e6d3; margin-bottom:0.5rem; }
    h1 span { color:#c8965a; }
    p { color:#7a6a75; font-style:italic; }
    .ok { color:#5a9e6f; margin-top:2rem; font-size:0.9rem; }
  </style>
</head>
<body>
  <div>
    <div style="color:#c8965a;font-size:1.5rem;margin-bottom:1rem">⬡ ✦ ⬡</div>
    <h1>La Voute <span>d'Anais</span></h1>
    <p>Biblioteca del Universo · Sistema activo</p>
    <div class="ok">✓ Servidor en linea</div>
  </div>
</body>
</html>
"@ | Out-File -FilePath "$ProjectDir\biblioteca\index.html" -Encoding UTF8

Log "Biblioteca web creada"

# ══════════════════════════════════════════════════════════════════
Section "11. Levantar Contenedores Docker"
# ══════════════════════════════════════════════════════════════════

Set-Location $ProjectDir

# Verificar que Docker esté corriendo
$dockerRunning = $false
$maxWait = 60
$waited = 0

Write-Host "  Esperando que Docker Desktop esté listo..." -ForegroundColor Yellow

while (-not $dockerRunning -and $waited -lt $maxWait) {
    try {
        $result = docker info 2>&1
        if ($LASTEXITCODE -eq 0) {
            $dockerRunning = $true
        }
    } catch { }

    if (-not $dockerRunning) {
        Write-Host "  Docker no está listo aún, esperando... ($waited/$maxWait seg)" -ForegroundColor Gray

        # Intentar iniciar Docker Desktop si no está corriendo
        if ($waited -eq 0) {
            $dockerDesktopPath = "${env:ProgramFiles}\Docker\Docker\Docker Desktop.exe"
            if (Test-Path $dockerDesktopPath) {
                Write-Host "  Iniciando Docker Desktop..." -ForegroundColor Yellow
                Start-Process $dockerDesktopPath
            }
        }

        Start-Sleep -Seconds 5
        $waited += 5
    }
}

if (-not $dockerRunning) {
    Warn "Docker Desktop no inició automáticamente."
    Warn "Por favor:"
    Warn "  1. Abre Docker Desktop manualmente"
    Warn "  2. Espera que aparezca 'Docker Desktop is running'"
    Warn "  3. Vuelve a ejecutar: voute-start.bat"
    Write-Host ""
} else {
    Log "Docker Desktop está corriendo"

    Write-Host "  Descargando imágenes Docker (primera vez ~2-5 min)..." -ForegroundColor Yellow
    docker compose pull

    Write-Host "  Iniciando servicios..." -ForegroundColor Yellow
    docker compose up -d

    Start-Sleep -Seconds 15

    Log "Contenedores iniciados"
    docker compose ps
}

# ══════════════════════════════════════════════════════════════════
Section "12. Abrir en el Navegador"
# ══════════════════════════════════════════════════════════════════

if ($dockerRunning) {
    Start-Sleep -Seconds 5
    Write-Host "  Abriendo n8n en el navegador..." -ForegroundColor Yellow
    Start-Process "http://localhost:5678"
    Start-Sleep -Seconds 2
    Write-Host "  Abriendo Biblioteca web..." -ForegroundColor Yellow
    Start-Process "http://localhost:8080"
}

# ══════════════════════════════════════════════════════════════════
Section "Instalacion Completada"
# ══════════════════════════════════════════════════════════════════

Write-Host ""
Write-Host "  Proyecto instalado en: $ProjectDir" -ForegroundColor White
Write-Host ""
Write-Host "  Credenciales generadas (guardalas):" -ForegroundColor Yellow
Write-Host "  POSTGRES_PASSWORD : $POSTGRES_PASSWORD" -ForegroundColor Gray
Write-Host "  N8N_ENCRYPTION_KEY: $N8N_KEY" -ForegroundColor Gray
Write-Host "  (guardadas en $ProjectDir\.env)" -ForegroundColor DarkGray
Write-Host ""
Write-Host "  Servicios:" -ForegroundColor White
Write-Host "  → n8n (flujos):   http://localhost:5678" -ForegroundColor Cyan
Write-Host "  → Biblioteca:     http://localhost:8080" -ForegroundColor Cyan
Write-Host "  → Ollama API:     http://localhost:11434" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Scripts en $ProjectDir\" -ForegroundColor White
Write-Host "  → voute-start.bat        Iniciar todos los servicios" -ForegroundColor Gray
Write-Host "  → voute-stop.bat         Detener todos los servicios" -ForegroundColor Gray
Write-Host "  → voute-status.bat       Ver estado de contenedores" -ForegroundColor Gray
Write-Host "  → voute-modelos.bat      Descargar modelos LLM (~35GB)" -ForegroundColor Gray
Write-Host "  → voute-modelos-lite.bat Modelos ligeros Q4 (~10GB)" -ForegroundColor Gray
Write-Host "  → voute-test.bat         Verificar que todo funciona" -ForegroundColor Gray
Write-Host "  → voute-backup.bat       Backup del universo" -ForegroundColor Gray
Write-Host "  → voute-logs.bat         Ver logs en tiempo real" -ForegroundColor Gray
Write-Host ""
Write-Host "  Proximo paso — Descargar modelos LLM:" -ForegroundColor Yellow
Write-Host "  Ejecuta voute-modelos.bat     (si tienes 16GB+ RAM)" -ForegroundColor White
Write-Host "  Ejecuta voute-modelos-lite.bat (si tienes menos de 16GB)" -ForegroundColor White
Write-Host ""

if ($needsRestart) {
    Write-Host ""
    Warn "Se activaron componentes del sistema que requieren reinicio."
    Warn "Reinicia Windows y luego ejecuta voute-start.bat para continuar."
    Write-Host ""
}

Write-Host "  `"La rendicion no es derrota. Es revelacion.`" - Anais" -ForegroundColor DarkYellow
Write-Host ""
Read-Host "  Presiona Enter para cerrar"
