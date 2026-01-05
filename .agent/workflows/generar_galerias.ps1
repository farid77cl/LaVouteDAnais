$root = "C:\Users\fabara\LaVouteDAnais\05_Imagenes"
$folders = Get-ChildItem -Path $root -Directory

foreach ($folder in $folders) {
    # Skip certain folders
    if ($folder.Name -eq "comics" -or $folder.Name -eq "historias") { continue }
    
    # Get images in this folder (not recursive, just this level)
    $images = Get-ChildItem -Path "$($folder.FullName)\*" -Include *.png, *.jpg, *.jpeg, *.webp -File
    
    if ($images) {
        # Use galeria_visual format
        $galleryPath = Join-Path $folder.FullName "galeria_visual_$($folder.Name).md"
        
        # Build header
        $folderTitle = (Get-Culture).TextInfo.ToTitleCase($folder.Name.Replace("_", " "))
        $content = "# Galeria Visual de $folderTitle`n`n"
        $content += "*Coleccion de imagenes organizadas por categoria*`n`n"
        $content += "---`n`n"
        $content += "## Estadisticas`n`n"
        $content += "| Metrica | Valor |`n"
        $content += "|---------|-------|`n"
        $content += "| **Total Imagenes** | $($images.Count) |`n"
        $content += "| **Ultima Actualizacion** | $(Get-Date -Format 'yyyy-MM-dd HH:mm') |`n`n"
        $content += "---`n`n"
        $content += "## Imagenes`n`n"
        
        # Table of images
        $content += "| # | Nombre | Vista Previa |`n"
        $content += "|---|--------|--------------|`n"
        
        $counter = 1
        foreach ($img in $images | Sort-Object Name) {
            $content += "| $counter | ``$($img.Name)`` | ![$($img.BaseName)]($($img.Name)) |`n"
            $counter++
        }
        
        $content += "`n---`n`n"
        $content += "*Generado automaticamente por Helena el $(Get-Date -Format 'yyyy-MM-dd HH:mm')*"
        
        Set-Content -Path $galleryPath -Value $content -Encoding UTF8
        Write-Host "Galeria creada: galeria_visual_$($folder.Name).md"
    }
    else {
        Write-Host "No hay imagenes en: $($folder.Name)"
    }
}

Write-Host "Proceso completado."
