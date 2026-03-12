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
