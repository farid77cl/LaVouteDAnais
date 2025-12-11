# Script para convertir Markdown a HTML copy-paste
# Uso: .\md_to_html.ps1 -InputFile "ruta/archivo.md" -OutputFile "ruta/salida.html" -StartLine 20

param(
    [string]$InputFile,
    [string]$OutputFile,
    [int]$StartLine = 1
)

# Leer el archivo desde la línea especificada
$content = Get-Content $InputFile -Encoding UTF8 | Select-Object -Skip ($StartLine - 1)

$html = @()

foreach ($line in $content) {
    $trimmed = $line.Trim()
    
    # Saltar líneas vacías extras
    if ([string]::IsNullOrWhiteSpace($trimmed)) {
        continue
    }
    
    # Convertir separadores
    if ($trimmed -eq "---") {
        $html += "<hr>"
        continue
    }
    
    # Convertir negrita **texto**
    $trimmed = $trimmed -replace '\*\*([^*]+)\*\*', '<strong>$1</strong>'
    
    # Convertir cursiva *texto*
    $trimmed = $trimmed -replace '\*([^*]+)\*', '<em>$1</em>'
    
    # Agregar como párrafo
    $html += "<p>$trimmed</p>"
}

# Escribir archivo
$html -join "`n" | Set-Content $OutputFile -Encoding UTF8

Write-Host "Convertido: $InputFile -> $OutputFile"
Write-Host "Lineas HTML: $($html.Count)"
