@echo off
echo.
echo ==================================================
echo      La Voute d'Anais Editor (VS LM STUDIO)
echo ==================================================
echo.

:: ── Verificar que LM Studio este corriendo ──
echo [PASO 1/4] Verificando LM Studio en puerto 1234...
curl -s http://127.0.0.1:1234/v1/models >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo  ╔══════════════════════════════════════════════╗
    echo  ║  [!] LM STUDIO NO DETECTADO EN PUERTO 1234  ║
    echo  ║                                              ║
    echo  ║  Abra LM Studio y cargue un modelo:         ║
    echo  ║                                              ║
    echo  ║  RECOMENDADO (sin censura):                  ║
    echo  ║   - dolphin-2.9.4-llama3.1-8b (GGUF Q4)     ║
    echo  ║   - dolphin-mistral-7b (GGUF Q4)             ║
    echo  ║   - dolphin-phi-2.7b (GGUF, rapido)          ║
    echo  ║                                              ║
    echo  ║  Luego inicie el Local Server (puerto 1234)  ║
    echo  ║  y vuelva a ejecutar este script.            ║
    echo  ╚══════════════════════════════════════════════╝
    echo.
    pause
    exit /b 1
)
echo    [OK] LM Studio detectado!

:: ── Activar Entorno Virtual ──
echo [PASO 2/4] Activando entorno Python...
call voute_env\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] No se pudo activar voute_env. Ejecute setup_env.bat primero.
    pause
    exit /b 1
)
echo    [OK] Entorno virtual activado!

:: ── Levantar Servidor Web ──
echo [PASO 3/4] Iniciando servidor web en http://localhost:6666 ...
start "La Voute Web Server" python web_interface\server.py

:: ── Esperar e Inicializar Frontend ──
timeout /t 5 /nobreak >nul
echo [PASO 4/4] Abriendo interfaz en el navegador...
start http://localhost:6666

echo.
echo ==================================================
echo   La Voute d'Anais Editor esta corriendo!
echo   Web UI:    http://localhost:6666
echo   LM Studio: http://localhost:1234
echo.
echo   MODELOS RECOMENDADOS PARA LM STUDIO:
echo   ────────────────────────────────────
echo   Sin censura (escritura erotica):
echo     dolphin-2.9.4-llama3.1-8b-GGUF
echo     dolphin-mistral-7b-GGUF
echo.
echo   Rapido y ligero:
echo     dolphin-phi-2.7b-GGUF
echo     qwen2.5-3b-GGUF
echo.
echo   Mejor calidad (requiere +16GB RAM):
echo     dolphin-llama3-70b-GGUF (Q2_K)
echo ==================================================
echo.
echo Presione cualquier tecla para cerrar esta ventana.
echo El servidor seguira corriendo en segundo plano.
pause
