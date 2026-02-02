$files = @(
    "C:\Users\fabara\LaVouteDAnais\00_Helena\galeria_outfits.md",
    "C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v01_basico.md"
)

foreach ($path in $files) {
    Write-Host "Processing $path..."
    if (!(Test-Path $path)) {
        Write-Host "File not found: $path"
        continue
    }
    
    Copy-Item $path "$path.bak" -Force
    
    $fixed = $false

    # Try 1: Fix Mojibake (UTF8 interpreted as ANSI, saved as UTF8)
    try {
        $content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
        
        # Heuristic for Mojibake: Contains "Ã" paired with other chars
        if ($content -match "Ã") {
            try {
                # Reverse: String -> ANSI Bytes -> UTF8 String
                $ansiBytes = [System.Text.Encoding]::GetEncoding(1252).GetBytes($content)
                $realText = [System.Text.Encoding]::UTF8.GetString($ansiBytes)
                
                # Check signature of successful fix (Spanish chars)
                if ($realText -match "ó" -or $realText -match "í" -or $realText -match "ñ") {
                    [System.IO.File]::WriteAllText($path, $realText, [System.Text.Encoding]::UTF8)
                    Write-Host "Fixed Mojibake in $path"
                    $fixed = $true
                }
            } catch {
                Write-Host "Mojibake check failed gracefully."
            }
        }
    } catch {
        Write-Host "UTF8 Read failed (likely invalid bytes for UTF8). Proceeding to ANSI check..."
    }

    if (-not $fixed) {
        # Try 2: Fix CP1252 (ANSI) file that needs to be UTF-8
        try {
            $content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::GetEncoding(1252))
            
            # Use heuristic to confirm it decoded correctly (Spanish chars)
            if ($content -match "ó" -or $content -match "í" -or $content -match "ñ" -or $content -match "Á" -or $content -match "É") {
                [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
                Write-Host "Converted CP1252 to UTF8 for $path"
                $fixed = $true
            }
        } catch {
            Write-Host "CP1252 Read failed: $_"
        }
    }

    if ($fixed) {
        Write-Host "SUCCESS: $path corrected."
    } else {
        Write-Host "NO CHANGE: $path (already correct or unknown encoding)."
    }
}
