$root = "C:\Users\fabara\LaVouteDAnais\05_Imagenes"
$folders = Get-ChildItem -Path $root -Directory -Recurse

foreach ($folder in $folders) {
    if ($folder.Name -eq "comics") { continue }
    
    # Correction: Use wildcards for the path when using -Include
    $images = Get-ChildItem -Path "$($folder.FullName)\*" -Include *.png, *.jpg, *.jpeg, *.webp -File
    
    if ($images) {
        $galleryPath = Join-Path $folder.FullName "GALERIA.md"
        $content = "# Galería de Imágenes: $($folder.Name)`n`n"
        $content += "> **Total Imágenes:** $($images.Count)`n`n"
        
        foreach ($img in $images) {
            $content += "### $($img.Name)`n`n"
            $content += "![$($img.Name)]($($img.Name))`n`n"
            $content += "---`n`n"
        }
        
        $content += "*Generado automáticamente el $(Get-Date -Format 'yyyy-MM-dd HH:mm')*"
        Set-Content -Path $galleryPath -Value $content -Encoding UTF8
        Write-Host "✅ Galería creada: $galleryPath"
    }
    else {
        Write-Host "⚠️ No hay imágenes en: $($folder.Name)"
    }
}
