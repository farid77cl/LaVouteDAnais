@echo off
echo.
echo ==================================================
echo      La Voute d'Anais Editor (VS LM STUDIO)
echo ==================================================
echo.

:: 1. Activar Entorno Virtual
echo [1/3] Activando entorno Python...
call voute_env\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] No se pudo activar voute_env. Ejecute setup_env.bat primero.
    pause
    exit /b 1
)

:: 2. Levantar Servidor Web
echo [2/3] Iniciando servidor web (http://localhost:8080)...
start "La Voute Web Server" python web_interface\server.py

:: 3. Esperar e Inicializar Frontend
timeout /t 5 /nobreak >nul
echo [3/3] Abriendo Interfaz en el navegador...
start http://localhost:8080

echo.
echo ==================================================
echo      [!] RECUERDE: Inicie LM Studio 
echo      y encienda el Local Server (Port 1234)
echo ==================================================
echo.
pause
