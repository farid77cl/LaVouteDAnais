@echo off
title La Voute d'Anais - Deteniendo...
cd /d "%~dp0"
echo Deteniendo servicios...
docker compose down
echo Servicios detenidos.
pause
