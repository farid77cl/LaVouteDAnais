import json
from pathlib import Path

# 1. Load AST
ast_path = Path('.graphify_ast.json')
if ast_path.exists():
    ast_data = json.loads(ast_path.read_text(encoding='utf-8'))
else:
    ast_data = {"nodes": [], "edges": [], "hyperedges": []}

# 2. Load Semantic Chunks
nodes = ast_data.get("nodes", [])
edges = ast_data.get("edges", [])
hyperedges = ast_data.get("hyperedges", [])

chunk_files = sorted(Path('graphify-out').glob('.graphify_chunk_*.json'))
for chunk_file in chunk_files:
    chunk_data = json.loads(chunk_file.read_text(encoding='utf-8'))
    nodes.extend(chunk_data.get("nodes", []))
    edges.extend(chunk_data.get("edges", []))
    hyperedges.extend(chunk_data.get("hyperedges", []))

# 3. Final Extract
extract_data = {
    "nodes": nodes,
    "edges": edges,
    "hyperedges": hyperedges
}

# 4. Save
(Path('graphify-out') / '.graphify_extract.json').write_text(json.dumps(extract_data, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"Merge completado. {len(nodes)} nodos y {len(edges)} aristas consolidados.")
