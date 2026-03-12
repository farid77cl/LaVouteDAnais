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
