$oldText = @"
Glamorous woman with platinum blonde bob haircut with straight bangs,
flawless porcelain skin (NO rosy cheeks),
HEAVY GLAMOUR MAKEUP: dramatic smokey eyes, thick winged eyeliner, long false lashes, arched brows, full glossy RED lips,
human realistic face (NOT CGI, NOT plastic, NOT doll-like),
feminine hourglass silhouette,
PLEASER platform heels 16-18cm (7-8"), visible external corset over clothing.
"@

$newText = @"
Glamorous woman with platinum blonde bob haircut with straight bangs,
flawless porcelain skin with satin finish (NO rosy cheeks),
delicate refined nose, high cheekbones with soft contour,
HEAVY GLAMOUR MAKEUP: bronze/champagne smokey eyes with shimmer inner corners, thick cat-eye winged liner, mega volume wispy false lashes, defined arched brows, ULTRA PLUMP overlined glossy RED lips (bee-stung bimbo lips),
human realistic face with parted lips and dreamy seductive expression (NOT CGI, NOT plastic),
EXTREME hourglass silhouette with large round high-profile breast implants creating prominent cleavage, tiny cinched waist,
PLEASER platform heels 16-18cm (7-8"), visible external corset over clothing.
"@

$files = Get-ChildItem -Path "C:\Users\fabara\LaVouteDAnais\00_Helena" -Filter "banco_prompts_v*.md"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    if ($content -match [regex]::Escape($oldText)) {
        $newContent = $content -replace [regex]::Escape($oldText), $newText
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
        Write-Host "✅ Actualizado: $($file.Name)"
    }
    else {
        Write-Host "⚠️ No encontrado en: $($file.Name)"
    }
}

Write-Host "`nProceso completado."
