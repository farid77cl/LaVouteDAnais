@echo off
title La Voute d'Anais - Backup
cd /d "%~dp0"
set DATE=%date:~6,4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%
set DATE=%DATE: =0%
set BACKUP=backups\%DATE%

echo Haciendo backup en %BACKUP%...
mkdir "%BACKUP%" 2>nul
xcopy /E /I /Q voute_data "%BACKUP%\voute_data" >nul

docker exec voute_n8n n8n export:workflow --all --output=/tmp/workflows.json 2>nul
docker cp voute_n8n:/tmp/workflows.json "%BACKUP%\n8n_workflows.json" 2>nul

echo Backup completado en: %BACKUP%
pause
