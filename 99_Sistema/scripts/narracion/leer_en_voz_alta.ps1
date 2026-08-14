# Script de lectura en voz alta para relatos de La Voûte d'Anaïs
param (
    [string]$FilePath = "c:\Users\farid\LaVouteDAnais\03_Literatura\01_En_Progreso\cafe_con_piernas\capitulo_01_el_turno_de_prueba_v0.13.md",
    [string]$VoiceName = "Microsoft Helena Desktop",
    [int]$Rate = -1,
    [int]$Volume = 100
)

Write-Host "Cargando archivo: $FilePath" -ForegroundColor Magenta
if (-not (Test-Path $FilePath)) {
    Write-Error "El archivo especificado no existe: $FilePath"
    exit 1
}

Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer

# Intentar seleccionar la voz en español
try {
    $synth.SelectVoice($VoiceName)
    Write-Host "Voz seleccionada: $VoiceName" -ForegroundColor Green
} catch {
    Write-Warning "No se pudo seleccionar '$VoiceName', usando voz predeterminada."
}

$synth.Rate = $Rate
$synth.Volume = $Volume

# Leer el texto y limpiar markdown
$rawText = Get-Content -Path $FilePath -Encoding UTF8 -Raw

# Limpieza ligera de sintaxis markdown para que suene natural
$cleanText = $rawText -replace '#+ ', '' `
                      -replace '\*\*\*', '' `
                      -replace '\*\*', '' `
                      -replace '\*', '' `
                      -replace '—', ', ' `
                      -replace '\[.*?\]\(.*?\)', '' `
                      -replace '`', ''

# Dividir por párrafos para lectura fluida
$paragraphs = $cleanText -split "(\r?\n){2,}"

Write-Host "Iniciando lectura en voz alta... Presiona Ctrl+C en la consola para detener." -ForegroundColor Cyan

foreach ($p in $paragraphs) {
    $trimmed = $p.Trim()
    if ($trimmed.Length -gt 0) {
        $synth.Speak($trimmed)
        Start-Sleep -Milliseconds 300
    }
}

Write-Host "Lectura completada." -ForegroundColor Green
