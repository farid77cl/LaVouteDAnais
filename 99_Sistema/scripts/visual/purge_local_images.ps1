# Script de Purga - La Voûte d'Anaïs
# Este script aplica 'assume-unchanged' a las imágenes y las borra localmente.

$ImagePath = "c:\Users\farid\LaVouteDAnais\05_Imagenes"
$Images = Get-ChildItem -Path $ImagePath -Recurse -Include *.png, *.jpg, *.jpeg

foreach ($Image in $Images) {
    $RelativePath = Resolve-Path $Image.FullName -Relative
    # Quitar el './' inicial si existe
    $GitPath = $RelativePath -replace "^\.\\", "" -replace "\\", "/"
    
    Write-Host "Procesando: $GitPath"
    
    # Marcar como 'assume-unchanged' para que Git no registre el borrado local
    git update-index --assume-unchanged $GitPath
    
    # Borrar archivo físico
    Remove-Item $Image.FullName -Force
}

Write-Host "Purga completada. Las imágenes ahora residen solo en el repo remoto."
