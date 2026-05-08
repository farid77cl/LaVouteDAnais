import json
from pathlib import Path

# Cargar el grafo consolidado
extract_path = Path('graphify-out/.graphify_extract.json')
if not extract_path.exists():
    print("Error: Grafo no encontrado.")
    exit(1)

graph = json.loads(extract_path.read_text(encoding='utf-8'))

def find_paths(start_node, end_node, depth=3):
    # Implementación simplificada de búsqueda de rutas
    results = []
    edges = graph.get("edges", [])
    
    # Buscar aristas directas o de segundo nivel
    for edge in edges:
        if edge["source"] == start_node:
            results.append(f"{start_node} --({edge['relation']})--> {edge['target']}")
            # Buscar el siguiente salto
            for next_edge in edges:
                if next_edge["source"] == edge["target"]:
                    results.append(f"  └─ {edge['target']} --({next_edge['relation']})--> {next_edge['target']}")
    return results

print("--- RESULTADOS DE LA CONSULTA SEMÁNTICA ---")
paths = find_paths("elixir_violeta", "miss_doll")
for path in paths:
    print(path)

# Buscar impacto en interactivos
print("\n--- IMPACTO EN NARRATIVA INTERACTIVA ---")
for edge in graph.get("edges", []):
    if "dollhouse" in edge["target"] or "dollhouse" in edge["source"]:
        print(f"Relación detectada: {edge['source']} --({edge['relation']})--> {edge['target']}")
