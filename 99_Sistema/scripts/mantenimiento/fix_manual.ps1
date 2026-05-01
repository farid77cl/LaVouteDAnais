$replacements_outfit = @{
    "Ãƒ³" = "ó"; "Ãƒ­" = "í"; "Ãƒ¡" = "á"; "Ãƒ©" = "é"; "Ãƒ±" = "ñ"; "Ãƒº" = "ú";
    "ó" = "ó"; "í" = "í"; "á" = "á"; "é" = "é"; "ñ" = "ñ"; "ú" = "ú";
    "Ã" = "í"; "ðŸ¦‡" = "🦉"; "ðŸŒ™" = "🌙"; "ðŸ’€" = "💀"; "ðŸ©¸" = "🩸";
    "ðŸ•¸ï¸" = "🕷️"; "ðŸŒ‘" = "🌑"; "ðŸ”®" = "🔮"; "â¤ï¸" = "❤️";
    "ðŸ’Ž" = "💎"; "ðŸ’™" = "💙"; "ðŸ" = "💚"; "ðŸ·" = "🍷"; "ðŸ’œ" = "💜"; "ðŸ¥‚" = "🥂";
    "â›“ï¸" = "⛓️"
}

$replacements_prompt = @{
    "CANNICAS" = "CANÓNICAS"; "fsicos" = "físicos"; "especficos" = "específicos";
    "ANAS" = "ANAÏS"; "Ana s" = "Anaïs"; "??" = ""; "CANNICAS" = "CANÓNICAS"; "fsicos" = "físicos"; "especficos" = "específicos"
}
# Added replacements for replacement characters in case view_file representation was literal

$files = @(
    @{ Path = "C:\Users\fabara\LaVouteDAnais\00_Helena\galeria_outfits.md"; Map = $replacements_outfit },
    @{ Path = "C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v01_basico.md"; Map = $replacements_prompt }
)

foreach ($item in $files) {
    if (Test-Path $item.Path) {
        Write-Host "Reading $($item.Path)..."
        try {
            $content = [System.IO.File]::ReadAllText($item.Path, [System.Text.Encoding]::UTF8)
            $newContent = $content
            foreach ($key in $item.Map.Keys) {
                if ($key -ne "") {
                   $newContent = $newContent.Replace($key, $item.Map[$key])
                }
            }
            if ($newContent -ne $content) {
                [System.IO.File]::WriteAllText($item.Path, $newContent, [System.Text.Encoding]::UTF8)
                Write-Host "Fixed $($item.Path)"
            } else {
                Write-Host "No changes for $($item.Path)"
            }
        } catch {
            Write-Host "Error processing $($item.Path): $_"
        }
    }
}
