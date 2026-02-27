const $ = id => document.getElementById(id);
const btnGenerate = $('btn-generate');
const btnApprove = $('btn-approve');
const btnReject = $('btn-reject');
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
let ctx = {};   // accumulated context from each agent
let tokenCount = 0;

function updateUI() {
    // Progress tracker: highlight current, mark done
    for (let i = 0; i < AGENTS.length; i++) {
        const el = $(`step-${i}`);
        el.className = 'step' + (i === step ? ' active' : i < step ? ' done' : '');
    }
    // Agent cards
    for (let i = 0; i < AGENTS.length; i++) {
        const card = $(`card-${i}`);
        card.className = 'agent-card' + (i === step ? ' active' : i < step ? ' done' : '');
    }
    // Button
    btnText.textContent = AGENTS[step].verb;
    // Reset output
    agentOutput.value = '';
    checkpointControls.classList.add('hidden');
    btnGenerate.classList.remove('hidden');
    btnGenerate.disabled = false;
    agentOutput.readOnly = false;
    tokenCount = 0;
    tokenCountEl.textContent = '0 tokens';
}

function buildPrompt() {
    const a = AGENTS[step].key;
    const p = ctx.premisa || userPrompt.value;
    switch (a) {
        case 'ideador':
            return userPrompt.value;
        case 'arquitecto':
            return `PREMISA: ${p}\n\nPROPUESTA DEL IDEADOR:\n${ctx.ideador}\n\nGenera la estructura narrativa completa.`;
        case 'personajes':
            return `PREMISA: ${p}\n\nARCO DEL ARQUITECTO:\n${ctx.arquitecto}\n\nCrea fichas detalladas de personajes.`;
        case 'escritor':
            return `PREMISA: ${p}\n\nARCO:\n${ctx.arquitecto}\n\nPERSONAJES:\n${ctx.personajes}\n\nEscribe el capítulo completo.`;
        case 'critico':
            return `ARCO:\n${ctx.arquitecto}\nPERSONAJES:\n${ctx.personajes}\n\nCAPÍTULO:\n${ctx.escritor}`;
        case 'editor':
            return `NOTAS DEL CRÍTICO:\n${ctx.critico}\n\nCAPÍTULO ORIGINAL:\n${ctx.escritor}\n\nAplica correcciones y reescribe.`;
        case 'contador':
            return `Evalúa este capítulo final:\n\n${ctx.editor}`;
    }
}

async function callAgent() {
    const agent = AGENTS[step];
    const prompt = buildPrompt();

    btnGenerate.disabled = true;
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
            body: JSON.stringify({ prompt })
        });

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split('\n');
            buffer = lines.pop();   // keep incomplete line

            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    try {
                        const data = JSON.parse(line.slice(6));
                        if (data.token) {
                            agentOutput.value += data.token;
                            tokenCount++;
                            tokenCountEl.textContent = `${tokenCount} tokens`;
                            // Auto-scroll output
                            agentOutput.scrollTop = agentOutput.scrollHeight;
                        }
                        if (data.done) {
                            streamStatus.classList.add('hidden');
                            btnGenerate.classList.add('hidden');
                            checkpointControls.classList.remove('hidden');
                            loader.classList.add('hidden');
                            btnText.textContent = agent.verb;

                            if (step === AGENTS.length - 1) {
                                btnApprove.textContent = '✦ Finalizar';
                            } else {
                                btnApprove.textContent = 'Aprobar & Continuar →';
                            }
                        }
                    } catch (e) { /* skip malformed */ }
                }
            }
        }

        // In case stream ended without 'done' flag
        streamStatus.classList.add('hidden');
        loader.classList.add('hidden');
        if (!checkpointControls.classList.contains('hidden')) return;
        btnGenerate.classList.add('hidden');
        checkpointControls.classList.remove('hidden');

    } catch (err) {
        agentOutput.value = `[Error de conexión: ${err.message}]`;
        streamStatus.classList.add('hidden');
        loader.classList.add('hidden');
        btnGenerate.disabled = false;
        btnText.textContent = agent.verb;
    }
}

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

btnReject.addEventListener('click', () => {
    checkpointControls.classList.add('hidden');
    btnGenerate.classList.remove('hidden');
    callAgent();
});

btnApprove.addEventListener('click', () => {
    // Save edited output
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
        // Auto-fire non-interactive agents
        if (['arquitecto', 'personajes', 'critico', 'contador'].includes(AGENTS[step].key)) {
            callAgent();
        }
    } else {
        alert('¡Pipeline completado! El relato final está listo.');
    }
});

// Init
updateUI();
