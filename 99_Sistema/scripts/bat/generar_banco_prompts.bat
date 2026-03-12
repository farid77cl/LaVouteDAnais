@echo off
set "PYTHON_PATH=python"
set "SCRIPT_PATH=C:\Users\fabara\LaVouteDAnais\99_Sistema\scripts\visual\prompt_factory\factory.py"
set "OUTPUT_DIR=C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts"

echo ========================================================
echo       FACTORY DE PROMPTS - LA VOUTE D'ANAIS
echo ========================================================
echo.
echo Seleccione un archivo de configuracion (99_Sistema/scripts/visual/prompt_factory/configs/):
echo.

set "CONFIG_DIR=C:\Users\fabara\LaVouteDAnais\99_Sistema\scripts\visual\prompt_factory\configs"

dir "%CONFIG_DIR%\*.json" /b

echo.
set /p CONFIG_FILE="Escriba el nombre del archivo (ej. v75_celestial_body.json): "

if not exist "%CONFIG_DIR%\%CONFIG_FILE%" (
    echo.
    echo ❌ ERROR: El archivo no existe.
    pause
    exit /b
)

echo.
set /p COUNT="Cantidad de prompts (Enter para usar default del JSON): "

echo.
echo Generando banco...
echo.

if "%COUNT%"=="" (
    "%PYTHON_PATH%" "%SCRIPT_PATH%" --config "%CONFIG_DIR%\%CONFIG_FILE%" --output "%OUTPUT_DIR%"
) else (
    "%PYTHON_PATH%" "%SCRIPT_PATH%" --config "%CONFIG_DIR%\%CONFIG_FILE%" --output "%OUTPUT_DIR%" --count %COUNT%
)

echo.
if %ERRORLEVEL% EQU 0 (
    echo ✅ Proceso finalizado correctamente.
) else (
    echo ❌ Ocurrio un error.
)
pause
