const $ = id => document.getElementById(id);
const btnGenerate = $('btn-generate');
const btnApprove = $('btn-approve');
const btnReject = $('btn-reject');
const btnStop = $('btn-stop');
const btnSave = $('btn-save');
const btnFeedback = $('btn-feedback');
const btnLoad = $('btn-load');
const userPrompt = $('user-prompt');
const agentOutput = $('agent-output');
const loader = document.querySelector('.loader');
const btnText = document.querySelector('.btn-text');
const checkpointControls = $('checkpoint-controls');
const promptLabel = $('prompt-label');
const streamStatus = $('stream-status');
const streamAgentName = $('stream-agent-name');
const tokenCountEl = $('token-count');

const AGENTS = [
    { key: 'ideador',    label: 'El Ideador',    verb: 'Invocar al Ideador' },
    { key: 'arquitecto', label: 'El Arquitecto', verb: 'Invocar al Arquitecto' },
    { key: 'personajes', label: 'Los Personajes', verb: 'Invocar Personajes' },
    { key: 'escritor',   label: 'El Escritor',   verb: 'Invocar al Escritor' },
    { key: 'critico',    label: 'El Crítico',    verb: 'Invocar al Crítico' },
    { key: 'editor',     label: 'El Editor',     verb: 'Invocar al Editor' },
    { key: 'contador',   label: 'El Contador',   verb: 'Invocar al Contador' }
];

let step = 0;
let ctx = {};
let tokenCount = 0;
let abortController = null;

function updateUI() {
    for (let i = 0; i < AGENTS.length; i++) {
        $(`step-${i}`).className = 'step' + (i === step ? ' active' : i < step ? ' done' : '');
        $(`card-${i}`).className = 'agent-card' + (i === step ? ' active' : i < step ? ' done' : '');
    }
    btnText.textContent = AGENTS[step].verb;
    agentOutput.value = '';
    checkpointControls.classList.add('hidden');
    btnGenerate.classList.remove('hidden');
    btnStop.classList.add('hidden');
    btnGenerate.disabled = false;
    agentOutput.readOnly = false;
    tokenCount = 0;
    tokenCountEl.textContent = '0 tokens';
}

function buildPrompt() {
    const a = AGENTS[step].key;
    const p = ctx.premisa || userPrompt.value;
    switch (a) {
        case 'ideador':    return userPrompt.value;
        case 'arquitecto': return `PREMISA: ${p}\n\nPROPUESTA DEL IDEADOR:\n${ctx.ideador}\n\nGenera la estructura narrativa completa.`;
        case 'personajes': return `PREMISA: ${p}\n\nARCO DEL ARQUITECTO:\n${ctx.arquitecto}\n\nCrea fichas detalladas de personajes.`;
        case 'escritor':   return `PREMISA: ${p}\n\nARCO:\n${ctx.arquitecto}\n\nPERSONAJES:\n${ctx.personajes}\n\nEscribe el capítulo completo.`;
        case 'critico':    return `ARCO:\n${ctx.arquitecto}\nPERSONAJES:\n${ctx.personajes}\n\nCAPÍTULO:\n${ctx.escritor}`;
        case 'editor':     return `NOTAS DEL CRÍTICO:\n${ctx.critico}\n\nCAPÍTULO ORIGINAL:\n${ctx.escritor}\n\nAplica correcciones y reescribe.`;
        case 'contador':   return `Evalúa este capítulo final:\n\n${ctx.editor}`;
    }
}

function finishStream(agent) {
    streamStatus.classList.add('hidden');
    btnStop.classList.add('hidden');
    btnGenerate.classList.add('hidden');
    checkpointControls.classList.remove('hidden');
    loader.classList.add('hidden');
    btnText.textContent = agent.verb;
    btnApprove.textContent = step === AGENTS.length - 1 ? '✦ Finalizar' : 'Aprobar & Continuar →';
}

async function callAgent() {
    const agent = AGENTS[step];
    const prompt = buildPrompt();
    abortController = new AbortController();

    btnGenerate.disabled = true;
    btnGenerate.classList.add('hidden');
    btnStop.classList.remove('hidden');
    loader.classList.remove('hidden');
    btnText.textContent = 'Conectando...';
    streamStatus.classList.remove('hidden');
    streamAgentName.textContent = `${agent.label} está escribiendo...`;
    agentOutput.value = '';
    tokenCount = 0;

    try {
        const response = await fetch(`/api/agent/${agent.key}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt }),
            signal: abortController.signal
        });
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split('\n');
            buffer = lines.pop();
            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    try {
                        const data = JSON.parse(line.slice(6));
                        if (data.token) {
                            agentOutput.value += data.token;
                            tokenCount++;
                            tokenCountEl.textContent = `${tokenCount} tokens`;
                            agentOutput.scrollTop = agentOutput.scrollHeight;
                        }
                        if (data.done) finishStream(agent);
                    } catch (e) { }
                }
            }
        }
        if (checkpointControls.classList.contains('hidden')) finishStream(agent);
    } catch (err) {
        if (err.name === 'AbortError') {
            finishStream(agent);
        } else {
            agentOutput.value = `[Error de conexión: ${err.message}]`;
            streamStatus.classList.add('hidden');
            btnStop.classList.add('hidden');
            loader.classList.add('hidden');
            btnGenerate.classList.remove('hidden');
            btnGenerate.disabled = false;
            btnText.textContent = agent.verb;
        }
    }
    abortController = null;
}

// ═══ Stop ═══
btnStop.addEventListener('click', () => { if (abortController) abortController.abort(); });

// ═══ Generate ═══
btnGenerate.addEventListener('click', () => {
    if (step === 0 && !userPrompt.value.trim()) {
        userPrompt.focus();
        userPrompt.style.borderColor = '#cc3333';
        setTimeout(() => userPrompt.style.borderColor = '', 2000);
        return;
    }
    if (step === 0) ctx.premisa = userPrompt.value;
    callAgent();
});

// ═══ Re-generate ═══
btnReject.addEventListener('click', () => { checkpointControls.classList.add('hidden'); callAgent(); });

// ═══ Approve ═══
btnApprove.addEventListener('click', () => {
    ctx[AGENTS[step].key] = agentOutput.value;
    if (step < AGENTS.length - 1) {
        step++;
        if (step === 1) {
            userPrompt.value = ctx.premisa;
            userPrompt.disabled = true;
            userPrompt.style.opacity = '0.5';
            promptLabel.textContent = 'Premisa (bloqueada)';
        }
        updateUI();
        if (['arquitecto', 'personajes', 'critico', 'contador'].includes(AGENTS[step].key)) callAgent();
    } else {
        saveState();
    }
});

// ═══ Save ═══
async function saveState() {
    ctx[AGENTS[step].key] = agentOutput.value;
    const payload = { step, agent: AGENTS[step].key, premisa: ctx.premisa || userPrompt.value, context: ctx };
    try {
        btnSave.disabled = true; btnSave.textContent = '⏳ Guardando...';
        const res = await fetch('/api/save', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
        const data = await res.json();
        btnSave.textContent = '✓ Guardado';
        setTimeout(() => { btnSave.textContent = '💾 Guardar'; btnSave.disabled = false; }, 2000);
    } catch (e) {
        btnSave.textContent = '✗ Error';
        setTimeout(() => { btnSave.textContent = '💾 Guardar'; btnSave.disabled = false; }, 2000);
    }
}
btnSave.addEventListener('click', () => saveState());

// ═══ Feedback Modal ═══
let feedbackType = 'like';
const feedbackModal = $('feedback-modal');
const fbComment = $('feedback-comment');

btnFeedback.addEventListener('click', () => { feedbackModal.classList.remove('hidden'); fbComment.focus(); });
$('fb-cancel').addEventListener('click', () => { feedbackModal.classList.add('hidden'); fbComment.value = ''; });

document.querySelectorAll('.fb-type').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.fb-type').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        feedbackType = btn.dataset.type;
    });
});

$('fb-submit').addEventListener('click', async () => {
    const comment = fbComment.value.trim();
    if (!comment) return;
    const sample = agentOutput.value.substring(0, 200);
    try {
        await fetch('/api/feedback', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ agent: AGENTS[step].key, type: feedbackType, comment, sample })
        });
        fbComment.value = '';
        feedbackModal.classList.add('hidden');
        btnFeedback.textContent = '✓ Aprendido';
        setTimeout(() => { btnFeedback.textContent = '🧠 Feedback'; }, 2000);
    } catch (e) {
        alert('Error guardando feedback');
    }
});

// ═══ Load Session Modal ═══
const loadModal = $('load-modal');
const sessionsList = $('saved-sessions-list');

btnLoad.addEventListener('click', async () => {
    loadModal.classList.remove('hidden');
    sessionsList.innerHTML = '<p class="modal-sub">Cargando sesiones...</p>';
    try {
        const res = await fetch('/api/sessions');
        const data = await res.json();
        if (data.sessions.length === 0) {
            sessionsList.innerHTML = '<p class="modal-sub">No hay sesiones guardadas.</p>';
            return;
        }
        sessionsList.innerHTML = '';
        data.sessions.forEach(s => {
            const btn = document.createElement('button');
            btn.className = 'session-item';
            btn.innerHTML = `<div class="session-name">${s.name}</div><div class="session-meta">${s.step} · ${s.date}</div>`;
            btn.addEventListener('click', () => loadSession(s.filename));
            sessionsList.appendChild(btn);
        });
    } catch (e) {
        sessionsList.innerHTML = '<p class="modal-sub">Error cargando sesiones.</p>';
    }
});

$('load-cancel').addEventListener('click', () => loadModal.classList.add('hidden'));

async function loadSession(filename) {
    try {
        const res = await fetch(`/api/sessions/${filename}`);
        const data = await res.json();
        if (data.error) { alert(data.error); return; }

        // Restore state
        ctx = data.context || {};
        step = data.step || 0;
        if (ctx.premisa) {
            userPrompt.value = ctx.premisa;
            if (step > 0) {
                userPrompt.disabled = true;
                userPrompt.style.opacity = '0.5';
                promptLabel.textContent = 'Premisa (bloqueada)';
            }
        }
        // Update UI to the right step
        for (let i = 0; i < AGENTS.length; i++) {
            $(`step-${i}`).className = 'step' + (i === step ? ' active' : i < step ? ' done' : '');
            $(`card-${i}`).className = 'agent-card' + (i === step ? ' active' : i < step ? ' done' : '');
        }
        btnText.textContent = AGENTS[step].verb;
        // Show last agent output if exists
        const currentKey = AGENTS[step].key;
        agentOutput.value = ctx[currentKey] || '';
        if (agentOutput.value) {
            checkpointControls.classList.remove('hidden');
            btnGenerate.classList.add('hidden');
        } else {
            checkpointControls.classList.add('hidden');
            btnGenerate.classList.remove('hidden');
            btnGenerate.disabled = false;
        }
        loadModal.classList.add('hidden');
    } catch (e) {
        alert('Error cargando sesión: ' + e.message);
    }
}

// Close modals on overlay click
document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) overlay.classList.add('hidden');
    });
});

// Init
updateUI();
