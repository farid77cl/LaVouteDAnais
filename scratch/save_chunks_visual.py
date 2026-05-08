import json
from pathlib import Path

# Chunks 17, 18, 19, 20 - Motor de Imagen & Interactivos
chunk_visual_engine = {
    "nodes": [
        {"id": "prompts_ele_v3_master", "label": "Prompts Ele V3 Master", "file_type": "code", "source_file": "05_Imagenes/ele/prompts_ele_v3_master.md"},
        {"id": "dollhouse_master", "label": "The Dollhouse (Interactive Master)", "file_type": "document", "source_file": "04_Interactivo/the_dollhouse/MASTER_DOLLHOUSE.md"},
        {"id": "guion_comic_nancy", "label": "Guion Cómic: El Collar de Nancy", "file_type": "document", "source_file": "05_Imagenes/comics/el_collar_de_nancy/guion_comic.md"},
        {"id": "collection_latex", "label": "Collection: Latex Fetish", "file_type": "folder", "source_file": "05_Imagenes/ele/collection_latex_fetish/Readme.md"}
    ],
    "edges": [
        {"source": "ele", "target": "prompts_ele_v3_master", "relation": "defined_by", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "guion_comic_nancy", "target": "el_collar_de_nancy", "relation": "adapts", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "miss_doll", "target": "dollhouse_master", "relation": "hosts", "confidence": "INFERRED", "confidence_score": 0.85},
        {"source": "prompts_ele_v3_master", "target": "collection_latex", "relation": "governs", "confidence": "EXTRACTED", "confidence_score": 0.95}
    ],
    "hyperedges": [],
    "input_tokens": 40000,
    "output_tokens": 1200
}

output_dir = Path('graphify-out')
output_dir.mkdir(exist_ok=True)
(output_dir / '.graphify_chunk_17_20.json').write_text(json.dumps(chunk_visual_engine, indent=2, ensure_ascii=False), encoding='utf-8')
