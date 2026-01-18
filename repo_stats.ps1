# Script de Estadísticas - La Voute d'Anais
# Ejecutar con: .\repo_stats.ps1

Write-Host "ESTADISTICAS DE LA VOUTE D'ANAIS" -ForegroundColor Magenta
Write-Host "=================================" -ForegroundColor Magenta
Write-Host ""

$repoPath = $PSScriptRoot
if (-not $repoPath) { $repoPath = "C:\Users\fabara\LaVouteDAnais" }

# Contar archivos markdown
$mdFiles = Get-ChildItem -Path $repoPath -Recurse -Filter "*.md" -File | Where-Object { $_.FullName -notlike "*\.git*" }
Write-Host "[MD] Archivos Markdown: $($mdFiles.Count)" -ForegroundColor Cyan

# Contar imagenes
$imgPaths = @(
    "$repoPath\05_Imagenes\helena",
    "$repoPath\05_Imagenes\miss_doll",
    "$repoPath\05_Imagenes\anais"
)

$totalImages = 0
foreach ($path in $imgPaths) {
    if (Test-Path $path) {
        $images = Get-ChildItem -Path $path -File | Where-Object { $_.Extension -match "\.(png|jpg|jpeg|webp)$" }
        $count = $images.Count
        $folderName = Split-Path $path -Leaf
        Write-Host "  [IMG] $folderName : $count imagenes" -ForegroundColor Yellow
        $totalImages += $count
    }
}
Write-Host "[IMG] Total Imagenes: $totalImages" -ForegroundColor Cyan

# Contar historias finalizadas
$finalizadasPath = "$repoPath\03_Literatura\finalizadas"
if (Test-Path $finalizadasPath) {
    $finalizadas = Get-ChildItem -Path $finalizadasPath -Filter "*.md" -File | Where-Object { $_.Name -ne "README.md" }
    Write-Host "[HIST] Historias Finalizadas: $($finalizadas.Count)" -ForegroundColor Cyan
} else {
    $finalizadas = @()
    Write-Host "[HIST] Historias Finalizadas: 0" -ForegroundColor Cyan
}

# Contar historias en progreso
$enProgresoPath = "$repoPath\03_Literatura\en_progreso"
if (Test-Path $enProgresoPath) {
    $enProgreso = Get-ChildItem -Path $enProgresoPath -Directory
    Write-Host "[WIP] Historias En Progreso: $($enProgreso.Count)" -ForegroundColor Cyan
} else {
    Write-Host "[WIP] Historias En Progreso: 0" -ForegroundColor Cyan
}

# Contar palabras aproximadas (basado en tamanio de archivo)
$totalBytes = ($finalizadas | Measure-Object -Property Length -Sum).Sum
$approxWords = [math]::Round($totalBytes / 6)  # ~6 bytes por palabra en espaniol
Write-Host "[WORDS] Palabras Aprox (finalizadas): ~$($approxWords.ToString('N0'))" -ForegroundColor Cyan

# Bancos de prompts
$promptsPath = "$repoPath\00_Helena\bancos_prompts"
if (Test-Path $promptsPath) {
    $promptFiles = Get-ChildItem -Path $promptsPath -Filter "banco_prompts*.md" -File
    Write-Host "[PROMPTS] Bancos de Prompts: $($promptFiles.Count)" -ForegroundColor Cyan
} else {
    Write-Host "[PROMPTS] Bancos de Prompts: 0" -ForegroundColor Cyan
}

# Tamanio total del repo (sin .git)
$repoSize = (Get-ChildItem -Path $repoPath -Recurse -File | Where-Object { $_.FullName -notlike "*\.git*" } | Measure-Object -Property Length -Sum).Sum
$repoSizeMB = [math]::Round($repoSize / 1MB, 2)
Write-Host "[SIZE] Tamanio del Repositorio: $repoSizeMB MB" -ForegroundColor Cyan

Write-Host ""
Write-Host "[OK] Estadisticas generadas: $(Get-Date -Format 'yyyy-MM-dd HH:mm')" -ForegroundColor Green
Write-Host "Helena de Anais" -ForegroundColor Magenta
