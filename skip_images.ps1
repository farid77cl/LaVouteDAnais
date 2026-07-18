$files = git ls-files "05_Imagenes/ele/**/*.png"
$count = 0
foreach ($f in $files) {
    git update-index --skip-worktree $f
    $count++
}
Write-Output "Applied skip-worktree to $count files."
