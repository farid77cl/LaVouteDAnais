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
