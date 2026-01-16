# Genera HTML único de HR: Human Repurposing
# Solo cuerpo narrativo, sin metadatos ni firma

$sourcePath = "C:\Users\fabara\LaVouteDAnais\03_Literatura\finalizadas\hr_human_repurposing_completo.md"
$targetPath = "C:\Users\fabara\LaVouteDAnais\03_Literatura\finalizadas\html\hr_human_repurposing.html"

# Leer todo el contenido
$content = Get-Content $sourcePath -Raw -Encoding UTF8

# Eliminar el bloque de metadatos inicial (primeras ~25 líneas hasta "CUERPO DEL RELATO")
$content = $content -replace "(?s)^.*?CUERPO DEL RELATO\s*═+\s*", ""

# Eliminar encabezados de capítulos con metadatos:
# Patrón: "# HR: Human Repurposing - Capítulo X: Título" + Estado/Palabras/Fecha
$content = $content -replace "(?m)^#\s*HR:\s*Human\s*Repurposing.*$\s*\*\*Estado:\*\*.*$\s*\*\*Palabras:\*\*.*$\s*\*\*Fecha:\*\*.*$\s*---\s*", ""

# Eliminar firma final y nota de autora
$content = $content -replace "(?s)---\s*\*HR:\s*Human\s*Repurposing\*\s*\*Una historia de La Voûte d'Anaïs\*\s*\*2026\*\s*$", ""
$content = $content -replace "(?s)---\s*\*Helena de Anaïs\*.*?La Voûte d'Anaïs.*?$", ""

# Eliminar líneas "Continuará en Capítulo X"
$content = $content -replace "(?m)^>\s*\*Continuará en Capítulo.*$", ""

# Eliminar nota de autora final expandida
$content = $content -replace "(?s)---\s*┌─.*?Nota de la Autora.*?Anaïs Belland\s*---.*$", ""

# Convertir encabezados markdown a HTML
$content = $content -replace "(?m)^##\s+(.+)$", "<hr>`n<p align=`"center`"><strong>`$1</strong></p>`n<hr>"
$content = $content -replace "(?m)^#\s+(.+)$", "<h2 align=`"center`">`$1</h2>"

# Convertir blockquotes a cajas de cita
$content = $content -replace "(?m)^>\s*(.+)$", "<blockquote style=`"background: #f8f0ff; border-left: 3px solid #9370db; padding: 10px; font-style: italic;`">`$1</blockquote>"

# Convertir énfasis y negritas
$content = $content -replace "\*\*(.+?)\*\*", "<strong>`$1</strong>"
$content = $content -replace "\*(.+?)\*", "<em>`$1</em>"

# Convertir líneas horizontales simples
$content = $content -replace "(?m)^---$", "<hr>"

# Convertir párrafos (líneas que no están vacías y no empiezan con <)
$lines = $content -split "`n"
$htmlLines = @()
$inParagraph = $false

foreach ($line in $lines) {
    $trimmed = $line.Trim()
    if ($trimmed -eq "") {
        $htmlLines += ""
    } elseif ($trimmed -match "^<") {
        $htmlLines += $line
    } elseif ($trimmed -match "^—") {
        # Diálogos
        $htmlLines += "<p>$trimmed</p>"
    } else {
        $htmlLines += "<p>$trimmed</p>"
    }
}

$content = $htmlLines -join "`n"

# Limpiar múltiples saltos de línea
$content = $content -replace "(`n){3,}", "`n`n"

# Guardar
Set-Content $targetPath -Value $content -Encoding UTF8

Write-Host "✅ HTML único generado: $targetPath"
$size = (Get-Item $targetPath).Length / 1KB
Write-Host "   Tamaño: $([math]::Round($size, 1)) KB"
