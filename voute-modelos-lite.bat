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
