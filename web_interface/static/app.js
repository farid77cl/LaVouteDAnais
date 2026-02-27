const btnGenerate = document.getElementById('btn-generate');
const btnApprove = document.getElementById('btn-approve');
const btnReject = document.getElementById('btn-reject');
const userPromptArea = document.getElementById('user-prompt');
const agentOutputArea = document.getElementById('agent-output');
const loader = document.querySelector('.loader');
const btnText = document.querySelector('.btn-text');
const checkpointControls = document.getElementById('checkpoint-controls');
const promptLabel = document.getElementById('prompt-label');

const steps = ['ideador', 'arquitecto', 'personajes', 'escritor', 'critico', 'editor', 'contador'];
let currentStepIndex = 0;
let storyContext = {
    premisa: '',
    arco: '',
    personajes: '',
    capitulo: '',
    critica: '',
    final: '',
    metricas: ''
};

// Update UI based on current agent
function updateUIForStep(index) {
    const agent = steps[index];
    
    // Update progress tracker
    document.querySelectorAll('.step').forEach(el => el.classList.remove('active'));
    if (index === 0) document.getElementById('step-ideador').classList.add('active');
    else if (index <= 2) document.getElementById('step-arquitecto').classList.add('active');
    else if (index <= 5) document.getElementById('step-escritor').classList.add('active');
    else document.getElementById('step-critico').classList.add('active');

    // Update active card
    document.querySelectorAll('.agent-card').forEach(el => el.classList.remove('active'));
    if (index === 0) document.getElementById('card-ideador').classList.add('active');
    else if (index === 1 || index === 2) document.getElementById('card-arquitecto').classList.add('active');
    else if (index === 3) document.getElementById('card-escritor').classList.add('active');
    else document.getElementById('card-critico').classList.add('active');

    // Update button text
    btnText.textContent = `Generar (${agent.charAt(0).toUpperCase() + agent.slice(1)})`;
    
    // Reset output area
    agentOutputArea.value = '';
    checkpointControls.classList.add('hidden');
    btnGenerate.classList.remove('hidden');
    agentOutputArea.readOnly = false;
}

// Build the prompt for the current agent based on previous context
function buildAgentPrompt(agent) {
    let basePrompt = userPromptArea.value;

    switch(agent) {
        case 'ideador':
            return basePrompt;
        case 'arquitecto':
            return `Premisa original: ${storyContext.premisa}\n\nPropuesta del Ideador: ${storyContext.ideador}\n\nCon esto en mente, genera la estructura narrativa.`;
        case 'personajes':
            return `Premisa original: ${storyContext.premisa}\n\nArcos argumentales propuestos por el Arquitecto:\n${storyContext.arquitecto}\n\nCrea las fichas detalladas de los personajes para esta historia.`;
        case 'escritor':
            return `TÍTULO / PREMISA: ${storyContext.premisa}\n\nARCO: \n${storyContext.arquitecto}\n\nPERSONAJES: \n${storyContext.personajes}\n\nINSTRUCCIÓN: Basado absolutamente en esto, escribe el capítulo completo de principio a fin.`;
        case 'critico':
            return `Pautas de personajes y arco: \n${storyContext.arquitecto}\n${storyContext.personajes}\n\nCAPÍTULO A EVALUAR:\n${storyContext.escritor}`;
        case 'editor':
            return `NOTAS DEL CRÍTICO:\n${storyContext.critica}\n\nCAPÍTULO ORIGINAL:\n${storyContext.escritor}\n\nINSTRUCCIÓN: Aplica las correcciones y reescribe el capítulo mejorado.`;
        case 'contador':
            return `Evalúa este capítulo final:\n\n${storyContext.editor}`;
    }
}

async function callAgent(agent) {
    const prompt = buildAgentPrompt(agent);
    
    try {
        btnGenerate.disabled = true;
        loader.classList.remove('hidden');
        btnText.textContent = 'Procesando...';

        const response = await fetch(`/api/agent/${agent}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: prompt })
        });

        const data = await response.json();
        
        if (data.error) {
            agentOutputArea.value = data.error;
        } else {
            agentOutputArea.value = data.output;
            
            // Checkpoints: Ideador (0), Arquitecto (1), Personajes (2), Escritor (3), Critico (4), Editor (5), Contador (6)
            // Show checkpoints for human approval
            btnGenerate.classList.add('hidden');
            checkpointControls.classList.remove('hidden');
            
            if (agent === 'contador') {
                btnApprove.textContent = "Finalizar y Guardar";
            } else {
                btnApprove.textContent = "Aprobar & Continuar";
            }
        }
    } catch (error) {
        agentOutputArea.value = "Error de red: No se pudo conectar con el servidor Flask. " + error;
    } finally {
        btnGenerate.disabled = false;
        loader.classList.add('hidden');
        btnText.textContent = `Generar (${agent.charAt(0).toUpperCase() + agent.slice(1)})`;
    }
}

btnGenerate.addEventListener('click', () => {
    const currentAgent = steps[currentStepIndex];
    if (currentStepIndex === 0 && userPromptArea.value.trim() === '') {
        alert("Por favor, ingrese una premisa inicial antes de comenzar.");
        return;
    }
    
    // Guardo la premisa inicial si es el primer paso
    if (currentStepIndex === 0) {
        storyContext.premisa = userPromptArea.value;
    }

    callAgent(currentAgent);
});

btnReject.addEventListener('click', () => {
    // Regenerate current step
    callAgent(steps[currentStepIndex]);
});

btnApprove.addEventListener('click', () => {
    const currentAgent = steps[currentStepIndex];
    
    // Save the (potentially edited) output into context
    storyContext[currentAgent] = agentOutputArea.value;
    
    if (currentStepIndex < steps.length - 1) {
        // Move to next step
        currentStepIndex++;
        
        // Hide the editable input if we are past ideador, show it as context
        if (currentStepIndex === 1) {
            userPromptArea.value = "Contexto guardado. Avanzando por el pipeline...";
            userPromptArea.disabled = true;
            promptLabel.textContent = "Estado:";
        }
        
        updateUIForStep(currentStepIndex);
        
        // Auto-trigger next steps up to Writer to minimize clicking
        if (['arquitecto', 'personajes', 'critico', 'contador'].includes(steps[currentStepIndex])) {
            callAgent(steps[currentStepIndex]);
        }
        
    } else {
        alert("¡Pipeline Completado! El documento final está listo para ser guardado en La Voûte.");
        // Here we could add a save to disk feature
    }
});

// Init UI
updateUIForStep(0);
