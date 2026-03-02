Write-Host "Iniciando instalacion del entorno virtual La Voûte..." -ForegroundColor Cyan

# Create venv if not exists
if (-Not (Test-Path -Path "voute_env")) {
    Write-Host "Creando voute_env..." -ForegroundColor Yellow
    python -m venv voute_env
}

# Execute pip using the venv's python directly rather than trying to activate and calling global pip
Write-Host "Instalando dependencias en el entorno virtual..." -ForegroundColor Yellow
.\voute_env\Scripts\python.exe -m pip install -r web_interface\requirements.txt

Write-Host "Setup completado exitosamente!" -ForegroundColor Green
Write-Host "Ya puedes abrir voute-editor.bat" -ForegroundColor Cyan
pause
