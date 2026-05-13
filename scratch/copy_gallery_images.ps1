$looks = @(
    "look170_crimson_lace_escort",
    "look171_liquid_copper_bikini",
    "look172_obsidian_latex_sovereign",
    "look173_cyan_surge_bikini",
    "look174_rose_gold_dominion",
    "look175_crystal_veil_bikini",
    "look176_neon_coral_flash",
    "look177_ivory_column",
    "look178_leopard_vitacura",
    "look179_acid_yellow_editorial",
    "look180_cherry_vinyl_hostess"
)

$poses = @("standing", "back_view", "seated", "side_profile", "ditzy", "pov", "odalisque")

$destBase = "C:\Users\farid\.gemini\antigravity\brain\d117d088-5d52-416b-a489-26e4440c82d1\artifacts\gallery_images"
if (!(Test-Path $destBase)) { New-Item -ItemType Directory -Path $destBase }

foreach ($look in $looks) {
    $lookNum = $look.Substring(4, 3)
    $destLookDir = Join-Path $destBase $look
    if (!(Test-Path $destLookDir)) { New-Item -ItemType Directory -Path $destLookDir }
    
    foreach ($pose in $poses) {
        $fileName = "ele_$($lookNum)_$($pose).png"
        $srcPath = "C:\Users\farid\LaVouteDAnais\05_Imagenes\ele\$look\$fileName"
        
        # Fallback for odalisque -> lying
        if (($pose -eq "odalisque") -and !(Test-Path $srcPath)) {
            $srcPath = "C:\Users\farid\LaVouteDAnais\05_Imagenes\ele\$look\ele_$($lookNum)_lying.png"
        }

        $destPath = Join-Path $destLookDir $fileName
        
        if (Test-Path $srcPath) {
            Copy-Item -Path $srcPath -Destination $destPath -Force
        } else {
            Write-Host "Warning: $srcPath not found"
        }
    }
}
