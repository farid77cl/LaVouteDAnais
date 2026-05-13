
$brainDir = "C:\Users\farid\.gemini\antigravity\brain\d117d088-5d52-416b-a489-26e4440c82d1"
$targetDirBase = "c:\Users\farid\LaVouteDAnais\05_Imagenes\Ele"

$files = Get-ChildItem -Path $brainDir -Filter "*.png"

foreach ($file in $files) {
    if ($file.Name -match "ele_179_(\w+)_png_") {
        $pose = $matches[1]
        $targetDir = Join-Path $targetDirBase "look179_acid_yellow_editorial"
        $newName = "ele_179_$pose.png"
        $targetPath = Join-Path $targetDir $newName
        Move-Item -Path $file.FullName -Destination $targetPath -Force
        Write-Host "Moved $($file.Name) to $targetPath"
    }
    elseif ($file.Name -match "ele_180_(\w+)_png_") {
        $pose = $matches[1]
        $targetDir = Join-Path $targetDirBase "look180_cherry_vinyl_hostess"
        $newName = "ele_180_$pose.png"
        $targetPath = Join-Path $targetDir $newName
        Move-Item -Path $file.FullName -Destination $targetPath -Force
        Write-Host "Moved $($file.Name) to $targetPath"
    }
}
