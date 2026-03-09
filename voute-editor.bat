@echo off
cd /d "%~dp0"
echo.
echo ==================================================
echo      La Voute d'Anais Editor (VS LM STUDIO)
echo ==================================================
echo.

:: ── Verificar que LM Studio este corriendo ──
echo [PASO 1/4] Verificando LM Studio en puerto 1234...
curl -s -o nul http://127.0.0.1:1234/v1/models
if %errorlevel% neq 0 (
    echo.
    echo  [ADVERTENCIA] LM Studio NO detectado en puerto 1234.
    echo  El editor web igual va a abrir, pero los agentes no funcionaran
    echo  hasta que abra LM Studio y cargue un modelo.
    echo.
) else (
    echo    [OK] LM Studio detectado!
)

:: ── Activar Entorno Virtual ──
echo [PASO 2/4] Activando entorno Python...
if not exist "voute_env\Scripts\activate.bat" (
    echo [ERROR] No se encontro voute_env. Ejecute setup_env.bat primero.
    pause
    exit /b 1
)
call voute_env\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] No se pudo activar voute_env.
    pause
    exit /b 1
)
echo    [OK] Entorno virtual activado!

:: ── Verificar Flask instalado ──
echo [PASO 2.5/4] Verificando Flask...
python -c "import flask" 2>nul
if %errorlevel% neq 0 (
    echo [INFO] Flask no encontrado. Instalando dependencias...
    pip install -r web_interface\requirements.txt
    if %errorlevel% neq 0 (
        echo [ERROR] No se pudo instalar dependencias.
        pause
        exit /b 1
    )
)
echo    [OK] Flask disponible!

:: ── Levantar Servidor Web (ventana visible para ver errores) ──
echo [PASO 3/4] Iniciando servidor web en puerto 8666...
start "La Voute Web Server" cmd /k "cd /d "%~dp0" && call voute_env\Scripts\activate.bat && python web_interface\server.py"

:: ── Esperar e Inicializar Frontend ──
echo    Esperando que el servidor arranque...
timeout /t 4 /nobreak >nul
echo [PASO 4/4] Abriendo interfaz en el navegador...
start "" "http://localhost:8666"

echo.
echo ==================================================
echo   La Voute esta corriendo en puerto 8666
echo   LM Studio escuchando en puerto 1234
echo ==================================================
echo.
echo   Si el navegador muestra error, revise la ventana
echo   "La Voute Web Server" para ver el mensaje de error.
echo.
pause
