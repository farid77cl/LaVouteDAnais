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
