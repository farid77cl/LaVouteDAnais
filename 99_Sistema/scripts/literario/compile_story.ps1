# Compile Story Script
$source = 'c:\Users\fabara\LaVouteDAnais\04_Historias\en_progreso\eres_de_los_hombres_que_continuacion'
$dest = 'C:\Users\fabara\LaVouteDAnais\04_Historias\terminadas\eres_de_los_hombres_que_II\historia_completa.md'

$cap1 = Get-Content "$source\capitulo_01.md" -Raw
$cap2 = Get-Content "$source\capitulo_02.md" -Raw
$cap3 = Get-Content "$source\capitulo_03.md" -Raw
$cap4 = Get-Content "$source\capitulo_04.md" -Raw
$cap5 = Get-Content "$source\capitulo_05.md" -Raw

$full = $cap1 + "`n`n" + $cap2 + "`n`n" + $cap3 + "`n`n" + $cap4 + "`n`n" + $cap5

# Clean up
$full = $full -replace '## Capítulo \d+:.*\r?\n', ''
$full = $full -replace '### Escena \d+:.*\r?\n', ''
$full = $full -replace '\*\*\[Continuará\.\.\.\]\*\*\r?\n?', ''
$full = $full -replace '\*Palabras:.*\*\r?\n?', ''
$full = $full -replace '\*Palabras totales.*\*\r?\n?', ''
$full = $full -replace '## Epílogo:.*\r?\n', ''

$full | Set-Content $dest -Force
Write-Host "Done!"
