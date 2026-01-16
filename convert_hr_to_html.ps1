# Convierte capítulos MD de HR a HTML estilo Dollhouse 2026
# Formato: Plain HTML sin DOCTYPE, estilos inline mínimos

$sourceDir = "C:\Users\fabara\LaVouteDAnais\03_Literatura\en_progreso\hr_human_repurposing"
$targetDir = "C:\Users\fabara\LaVouteDAnais\03_Literatura\finalizadas\html"

$chapters = @(
    @{source="capitulo_01.md"; target="hr_cap1_la_marca.html"; title="Capítulo I: La Marca"},
    @{source="capitulo_02.md"; target="hr_cap2_el_proceso.html"; title="Capítulo II: El Proceso"},
    @{source="capitulo_03.md"; target="hr_cap3_dahlia.html"; title="Capítulo III: Dahlia"},
    @{source="capitulo_04.md"; target="hr_cap4_la_propiedad.html"; title="Capítulo IV: La Propiedad"},
    @{source="epilogo.md"; target="hr_epilogo_el_ciclo.html"; title="Epílogo: El Ciclo"}
)

foreach ($ch in $chapters) {
    $content = Get-Content "$sourceDir\$($ch.source)" -Raw -Encoding UTF8
    
    # Remover frontmatter markdown
    $content = $content -replace "^#.*?\r?\n", ""
    $content = $content -replace "\*\*Estado:\*\*.*?\r?\n", ""
    $content = $content -replace "\*\*Palabras:\*\*.*?\r?\n", ""
    $content = $content -replace "\*\*Fecha:\*\*.*?\r?\n", ""
    $content = $content -replace "^---\r?\n", ""
    
    # Convertir encabezados markdown a HTML
    $content = $content -replace "## (.*?)\r?\n", "<hr>`n<p align=`"center`"><strong>`$1</strong></p>`n<hr>`n`n"
    
    # Convertir blockquotes a cajas de cita
    $content = $content -replace "> \*(.+?)\*\r?\n", "<p align=`"center`" style=`"background-color: #f8f0ff; padding: 10px; border-left: 3px solid #9370db; font-style: italic;`">`$1</p>`n`n"
    
    # Convertir líneas horizontales
    $content = $content -replace "^---$", "<hr>"
    
    # Convertir énfasis y negritas
    $content = $content -replace "\*\*(.+?)\*\*", "<strong>`$1</strong>"
    $content = $content -replace "\*(.+?)\*", "<em>`$1</em>"
    
    # Convertir párrafos (líneas no vacías que no empiezan con <)
    $lines = $content -split "`n"
    $htmlLines = @()
    foreach ($line in $lines) {
        $trimmed = $line.Trim()
        if ($trimmed -and -not $trimmed.StartsWith("<") -and -not $trimmed.StartsWith("#")) {
            $htmlLines += "<p>$trimmed</p>"
        } else {
            $htmlLines += $line
        }
    }
    $content = $htmlLines -join "`n"
    
    # Crear estructura HTML con encabezado
    $header = @"
<!-- HR: HUMAN REPURPOSING - $($ch.title) -->
<p align="center" style="border: 2px solid #ff1493; padding: 10px;">
    <strong>HR: HUMAN REPURPOSING</strong><br>
    <strong>$($ch.title)</strong><br><br>
    #Feminization #MindControl #CorporateHorror #Transformation #Femdom
</p>

"@

    $footer = @"

<hr>
<p align="center" style="font-size: 0.8em; color: #888;">
    HR: Human Repurposing © 2026 La Voûte d'Anaïs
</p>
"@

    $finalHtml = $header + $content + $footer
    Set-Content "$targetDir\$($ch.target)" -Value $finalHtml -Encoding UTF8
    Write-Host "Generado: $($ch.target)"
}

Write-Host "`n✅ Conversión completada. Archivos en: $targetDir"
