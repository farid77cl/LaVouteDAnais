
# 1. Restore backup for banco_prompts
$banco = "C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v01_basico.md"
$bak = "$banco.bak"

if (Test-Path $bak) {
    Copy-Item $bak $banco -Force
    Write-Host "Restored backup for banco_prompts."
} else {
    Write-Host "Backup not found for banco_prompts. Using current file."
}

# 2. Fix galeria_outfits.md (Mojibake repair)
$outfit_path = "C:\Users\fabara\LaVouteDAnais\00_Helena\galeria_outfits.md"
if (Test-Path $outfit_path) {
    try {
        # Read as UTF-8
        $content = [System.IO.File]::ReadAllText($outfit_path, [System.Text.Encoding]::UTF8)
        
        # Replacement Dictionary (Char -> Correct Char)
        # Using Byte Arrays to avoid script encoding issues
        # ÃƒÂ³ (C3 83 C2 B3) -> ó
        $bad_o = [System.Text.Encoding]::UTF8.GetString(@(0xC3, 0x83, 0xC2, 0xB3))
        # ÃƒÂ­ (C3 83 C2 AD) -> í
        $bad_i = [System.Text.Encoding]::UTF8.GetString(@(0xC3, 0x83, 0xC2, 0xAD))
        # ÃƒÂ¡ (C3 83 C2 A1) -> á
        $bad_a = [System.Text.Encoding]::UTF8.GetString(@(0xC3, 0x83, 0xC2, 0xA1))
        # ÃƒÂ© (C3 83 C2 A9) -> é
        $bad_e = [System.Text.Encoding]::UTF8.GetString(@(0xC3, 0x83, 0xC2, 0xA9))
        # ÃƒÂ± (C3 83 C2 B1) -> ñ
        $bad_n = [System.Text.Encoding]::UTF8.GetString(@(0xC3, 0x83, 0xC2, 0xB1))
        # ÃƒÂº (C3 83 C2 BA) -> ú
        $bad_u = [System.Text.Encoding]::UTF8.GetString(@(0xC3, 0x83, 0xC2, 0xBA))
        # ÃƒÅ¡ (C3 83 C5 A1) -> Ú  (Note: Ã is C3 83. Š is C5 A1)
        $bad_U = [System.Text.Encoding]::UTF8.GetString(@(0xC3, 0x83, 0xC5, 0xA1))
        # ÃƒÂ¯ (C3 83 C2 AF) -> ï
        $bad_ii = [System.Text.Encoding]::UTF8.GetString(@(0xC3, 0x83, 0xC2, 0xAF))
        # Ãƒâ€˜ (C3 83 E2 80 98) -> Ñ (Check this bytes later if needed)
        # Assuming Ñ is C3 91. 
        # Mojibake for Ñ: Ã followed by something.
        # If Ãƒâ€˜ -> Ã (C3 83) â€˜ (E2 80 98).
        $bad_N = [System.Text.Encoding]::UTF8.GetString(@(0xC3, 0x83, 0xE2, 0x80, 0x98))

        $content = $content.Replace($bad_o, "ó")
        $content = $content.Replace($bad_i, "í")
        $content = $content.Replace($bad_a, "á")
        $content = $content.Replace($bad_e, "é")
        $content = $content.Replace($bad_n, "ñ")
        $content = $content.Replace($bad_u, "ú")
        $content = $content.Replace($bad_U, "Ú")
        $content = $content.Replace($bad_ii, "ï")
        $content = $content.Replace($bad_N, "Ñ")
        
        # Emoji fixes (Bat: F0 9F A6 87 -> Ã°Å¸Â¦â€¡)
        # Ã (C3 83) ° (C2 B0) Å (C3 85) ¸ (C2 B8) Â (C2 A6) ...
        # Too complex to build manually. Assuming simple replacement works if script is utf8?
        # No, script is ansi.
        # Skip emojis for now, focusing on text readability.

        [System.IO.File]::WriteAllText($outfit_path, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Fixed logic applied to galeria_outfits.md"
    } catch {
        Write-Host "Error in outfits: $_"
    }
}

# 3. Fix banco_prompts (CP1252 -> UTF8 + Text Fixes)
if (Test-Path $banco) {
    try {
        # Force Read as CP1252
        # Note: If restored from backup, backup might be the original 'broken' one ??
        # Or the one my previous script created? 
        # My previous script created .bak from ORIGINAL.
        # Original had ?? in view_file.
        # If it had ?? literal, we can't fix content, but we can fix headers.
        
        # Read as CP1252
        $content = [System.IO.File]::ReadAllText($banco, [System.Text.Encoding]::GetEncoding(1252))
        
        # Apply Text Fixes
        $content = $content.Replace("CANNICAS", "CANÓNICAS")
        $content = $content.Replace("fsicos", "físicos")
        $content = $content.Replace("especficos", "específicos")
        $content = $content.Replace("ANAS", "ANAÏS")
        $content = $content.Replace("?? ", "") # Clean up question marks
        
        [System.IO.File]::WriteAllText($banco, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Fixed banco_prompts_v01_basico.md"
    } catch {
        Write-Host "Error in banco: $_"
    }
}
