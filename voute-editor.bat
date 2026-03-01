@echo off
chcp 65001 > nul
title La Voûte Editor - Iniciando...
echo.
echo  🦇 La Voûte d'Anaïs — Editor
echo  ============================
echo.

echo [1/3] Verificando Docker Desktop...
docker info >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo    ⚠ Docker Desktop no está corriendo. Iniciando...
    start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    echo    Esperando 30 segundos...
    timeout /t 30 /nobreak >nul
) else (
    echo    ✅ Docker Desktop activo
)

echo [2/3] Iniciando Ollama...
docker start voute_ollama >nul 2>&1
echo    ✅ Ollama en puerto 11434

echo [3/3] Iniciando La Voûte Editor...
echo.
echo  ════════════════════════════════
echo  ✨ Abrir: http://localhost:4000
echo  ════════════════════════════════
echo.
echo  Ctrl+C para detener
echo.

cd /d "%~dp0web_interface"
python server.py
