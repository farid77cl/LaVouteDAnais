@echo off
title La Voute d'Anais - Logs
cd /d "%~dp0"
docker compose logs -f
