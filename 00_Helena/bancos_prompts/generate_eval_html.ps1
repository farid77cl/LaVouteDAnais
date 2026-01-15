# Script para generar HTMLs de evaluación desde bancos de prompts MD
# Uso: .\generate_eval_html.ps1

$bancoPath = "C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts"

# Template HTML base
$htmlTemplate = @'
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <style>
        :root { --bg: #0d1117; --card: #161b22; --border: #30363d; --text: #c9d1d9; --pink: #ff69b4; --green: #3fb950; --yellow: #d29922; --red: #f85149; --purple: #a371f7; }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: var(--bg); color: var(--text); padding: 20px; max-width: 1200px; margin: 0 auto; }
        h1 { color: var(--pink); margin-bottom: 10px; }
        .stats { background: var(--card); padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; gap: 20px; flex-wrap: wrap; }
        .stat { display: flex; align-items: center; gap: 5px; }
        .stat-dot { width: 12px; height: 12px; border-radius: 50%; }
        .prompt-card { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 15px; margin-bottom: 15px; }
        .prompt-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
        .prompt-title { color: var(--pink); font-weight: bold; }
        .prompt-text { background: #0d1117; padding: 10px; border-radius: 4px; font-family: monospace; font-size: 12px; max-height: 100px; overflow-y: auto; margin-bottom: 10px; }
        .eval-row { display: flex; gap: 15px; flex-wrap: wrap; align-items: center; }
        .eval-option { display: flex; align-items: center; gap: 5px; cursor: pointer; padding: 5px 10px; border-radius: 4px; border: 1px solid var(--border); transition: all 0.2s; }
        .eval-option:hover { border-color: var(--pink); }
        .eval-option.selected { border-color: var(--pink); background: rgba(255,105,180,0.2); }
        .copy-btn { background: var(--purple); color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; }
        .copy-btn:hover { opacity: 0.8; }
        .bueno { color: var(--green); } .normal { color: var(--yellow); } .malo { color: var(--red); } .rechazado { color: #666; text-decoration: line-through; }
    </style>
</head>
<body>
    <h1>{{TITLE}}</h1>
    <p style="margin-bottom: 20px; opacity: 0.7;">Haz clic en una evaluación para guardarla. Los datos se almacenan en tu navegador.</p>
    <div class="stats" id="stats">
        <div class="stat"><span class="stat-dot" style="background: var(--green)"></span> Bueno: <span id="count-bueno">0</span></div>
        <div class="stat"><span class="stat-dot" style="background: var(--yellow)"></span> Normal: <span id="count-normal">0</span></div>
        <div class="stat"><span class="stat-dot" style="background: var(--red)"></span> Malo: <span id="count-malo">0</span></div>
        <div class="stat"><span class="stat-dot" style="background: #666"></span> Rechazado: <span id="count-rechazado">0</span></div>
        <div class="stat">Sin evaluar: <span id="count-pending">0</span></div>
        <button class="copy-btn" style="margin-left: auto; background: var(--pink);" onclick="exportEvals()">📤 Exportar</button>
    </div>
    <div id="export-box" style="display: none; background: var(--card); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
        <p style="margin-bottom: 10px;">📋 Copia este texto y pégalo a Helena:</p>
        <textarea id="export-text" style="width: 100%; height: 150px; background: #0d1117; color: var(--text); border: 1px solid var(--border); border-radius: 4px; padding: 10px; font-family: monospace;" readonly></textarea>
        <button class="copy-btn" style="margin-top: 10px;" onclick="copyExport()">📋 Copiar</button>
    </div>
    <div id="prompts"></div>
    <script>
        const prompts = {{PROMPTS}};
        const STORAGE_KEY = '{{STORAGE_KEY}}';
        function getEvals() { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); }
        function setEval(id, value) { const evals = getEvals(); evals[id] = value; localStorage.setItem(STORAGE_KEY, JSON.stringify(evals)); updateStats(); renderPrompts(); }
        function updateStats() {
            const evals = getEvals();
            const counts = {bueno: 0, normal: 0, malo: 0, rechazado: 0, pending: 0};
            prompts.forEach(p => { const val = evals[p.id]; if (val === 'bueno') counts.bueno++; else if (val === 'normal') counts.normal++; else if (val === 'malo') counts.malo++; else if (val === 'rechazado') counts.rechazado++; else counts.pending++; });
            document.getElementById('count-bueno').textContent = counts.bueno;
            document.getElementById('count-normal').textContent = counts.normal;
            document.getElementById('count-malo').textContent = counts.malo;
            document.getElementById('count-rechazado').textContent = counts.rechazado;
            document.getElementById('count-pending').textContent = counts.pending;
        }
        function copyPrompt(text) { navigator.clipboard.writeText(text); alert('✅ Prompt copiado!'); }
        function renderPrompts() {
            const evals = getEvals();
            const container = document.getElementById('prompts');
            container.innerHTML = prompts.map(p => {
                const currentEval = evals[p.id] || '';
                return `<div class="prompt-card"><div class="prompt-header"><span class="prompt-title">Prompt ${p.id}: ${p.title}</span><button class="copy-btn" onclick="copyPrompt(\`${p.text.replace(/`/g, '\\`').replace(/\\/g, '\\\\')}\`)">📋 Copiar</button></div><div class="prompt-text">${p.text}</div><div class="eval-row"><label class="eval-option ${currentEval === 'bueno' ? 'selected' : ''}" onclick="setEval(${p.id}, 'bueno')"><span class="bueno">✓ Bueno</span></label><label class="eval-option ${currentEval === 'normal' ? 'selected' : ''}" onclick="setEval(${p.id}, 'normal')"><span class="normal">~ Normal</span></label><label class="eval-option ${currentEval === 'malo' ? 'selected' : ''}" onclick="setEval(${p.id}, 'malo')"><span class="malo">✗ Malo</span></label><label class="eval-option ${currentEval === 'rechazado' ? 'selected' : ''}" onclick="setEval(${p.id}, 'rechazado')"><span class="rechazado">⊘ Rechazado</span></label></div></div>`;
            }).join('');
        }
        function exportEvals() {
            const evals = getEvals();
            const lines = ['EVALUACION {{BANCO_NAME}}', '========================', ''];
            prompts.forEach(p => { const val = evals[p.id] || '_'; const symbol = val === 'bueno' ? '+' : val === 'normal' ? '~' : val === 'malo' ? '-' : val === 'rechazado' ? 'X' : '_'; lines.push(`Prompt ${p.id}: [${symbol}] ${p.title}`); });
            lines.push('', '========================');
            lines.push(`Bueno: ${document.getElementById('count-bueno').textContent}`);
            lines.push(`Normal: ${document.getElementById('count-normal').textContent}`);
            lines.push(`Malo: ${document.getElementById('count-malo').textContent}`);
            lines.push(`Rechazado: ${document.getElementById('count-rechazado').textContent}`);
            document.getElementById('export-text').value = lines.join('\n');
            document.getElementById('export-box').style.display = 'block';
        }
        function copyExport() { navigator.clipboard.writeText(document.getElementById('export-text').value); alert('✅ Evaluaciones copiadas!'); }
        renderPrompts(); updateStats();
    </script>
</body>
</html>
'@

# Procesar cada banco
Get-ChildItem -Path $bancoPath -Filter "banco_prompts_v*.md" | ForEach-Object {
    $mdFile = $_
    $baseName = $mdFile.BaseName -replace 'banco_prompts_', ''
    $htmlName = "evaluacion_$baseName.html"
    $htmlPath = Join-Path $bancoPath $htmlName
    
    # Leer contenido MD
    $content = Get-Content $mdFile.FullName -Raw -Encoding UTF8
    
    # Extraer título del banco (primera línea con #)
    $lines = $content -split "`n"
    $titleLine = $lines | Where-Object { $_ -match "^#\s+" } | Select-Object -First 1
    if ($titleLine) {
        # Remover # y caracteres no-ASCII (emojis)
        $bancoTitle = $titleLine -replace '^#\s*', '' -replace '[^\x00-\x7F]', '' -replace '\s+', ' '
        $bancoTitle = $bancoTitle.Trim()
    } else {
        $bancoTitle = "Banco $baseName"
    }
    
    # Extraer prompts (buscar bloques de código después de ### Prompt N:)
    $prompts = @()
    $promptMatches = [regex]::Matches($content, '###\s*Prompt\s*(\d+)[:\s]*([^\r\n]+)?[\r\n]+(?:\*\*Eval:\*\*[^\r\n]*[\r\n]+)?[\r\n]*```[^\r\n]*[\r\n]+([\s\S]+?)```')
    
    foreach ($match in $promptMatches) {
        $id = [int]$match.Groups[1].Value
        $title = if ($match.Groups[2].Value) { $match.Groups[2].Value.Trim() } else { "Prompt $id" }
        $text = $match.Groups[3].Value.Trim() -replace '"', '\"' -replace "`r`n", " " -replace "`n", " "
        
        $prompts += @{
            id = $id
            title = $title
            text = $text
        }
    }
    
    if ($prompts.Count -eq 0) {
        Write-Host "SKIP: $($mdFile.Name) - No prompts found"
        return
    }
    
    # Generar JSON de prompts
    $promptsJson = ($prompts | ForEach-Object {
        "{ id: $($_.id), title: `"$($_.title)`", text: `"$($_.text)`" }"
    }) -join ",`n            "
    $promptsJson = "[$promptsJson]"
    
    # Generar HTML
    $html = $htmlTemplate `
        -replace '{{TITLE}}', $bancoTitle `
        -replace '{{PROMPTS}}', $promptsJson `
        -replace '{{STORAGE_KEY}}', "banco_${baseName}_eval" `
        -replace '{{BANCO_NAME}}', $baseName.ToUpper()
    
    # Guardar HTML
    $html | Out-File -FilePath $htmlPath -Encoding UTF8
    Write-Host "CREATED: $htmlName ($($prompts.Count) prompts)"
}

Write-Host "`nDone! Generated HTML files for evaluation."
