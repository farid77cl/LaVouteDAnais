Write-Host "Iniciando formateo forzado del Disco 1 (7.37 GB - SD Card)" -ForegroundColor Yellow
Clear-Disk -Number 1 -RemoveData -Confirm:$false
New-Partition -DiskNumber 1 -UseMaximumSize -IsActive -AssignDriveLetter | Format-Volume -FileSystem FAT32 -NewFileSystemLabel "SDCARD" -Confirm:$false
Write-Host "Formateo exitoso. La tarjeta SD está lista en FAT32." -ForegroundColor Green
