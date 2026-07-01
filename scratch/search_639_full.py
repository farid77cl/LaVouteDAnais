import json

log_path = r"C:\Users\farid\.gemini\antigravity\brain\c89cd2ec-3ece-41f1-8aec-258837cfed3f\.system_generated\logs\transcript.jsonl"

steps = []
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            steps.append(data)
        except Exception as e:
            pass

print(f"Total steps: {len(steps)}")
for i, step in enumerate(steps[-10:]):
    print(f"Index {len(steps)-10+i} (Step {step.get('step_index')}): Source={step.get('source')}, Type={step.get('type')}")
    content = str(step.get('content'))
    print(f"  Content snippet: {content[:300]}")
