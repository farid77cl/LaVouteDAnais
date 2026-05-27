import json
from pathlib import Path

# Chunk 06 - Personajes Secundarios & Transformados
chunk_06 = {
    "nodes": [
        {"id": "roxy", "label": "Roxy (Secondary)", "file_type": "document", "source_file": "02_Personajes/02_Secundarios/ficha_roxy.md"},
        {"id": "vera", "label": "Vera (Secondary)", "file_type": "document", "source_file": "02_Personajes/02_Secundarios/ficha_vera.md"},
        {"id": "sebastian_alex", "label": "Alex/Sebastian (Transformed)", "file_type": "document", "source_file": "02_Personajes/03_Transformados/ficha_alex_sebastian.md"},
        {"id": "elixir_violeta", "label": "Elixir Violeta", "file_type": "rationale", "source_file": "03_Literatura/02_Finalizadas/la_dulce_aniquilacion/La_Dulce_Aniquilación.md"}
    ],
    "edges": [
        {"source": "miss_doll", "target": "sebastian_alex", "relation": "transformed", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "elixir_violeta", "target": "sebastian_alex", "relation": "enabled_transformation_of", "confidence": "INFERRED", "confidence_score": 0.9}
    ],
    "hyperedges": [],
    "input_tokens": 15000,
    "output_tokens": 700
}

# Chunks 13, 14, 15 - Antología de Historias
chunk_lit_anthology = {
    "nodes": [
        {"id": "smart_home_stepford", "label": "Smart Home Stepford (Project)", "file_type": "document", "source_file": "03_Literatura/02_Finalizadas/smart_home_stepford/smart_home_stepford_completo.md"},
        {"id": "perfume_ruina", "label": "Perfume de Ruina", "file_type": "document", "source_file": "03_Literatura/02_Finalizadas/perfume_de_ruina/Perfume_de_Ruina.md"},
        {"id": "gloss_trance", "label": "Gloss: El Trance de Miss Doll", "file_type": "document", "source_file": "03_Literatura/02_Finalizadas/gloss_trance_miss_doll/Gloss_El_Trance_de_Miss_Doll.md"},
        {"id": "hr_repurposing", "label": "HR: Human Repurposing", "file_type": "document", "source_file": "03_Literatura/02_Finalizadas/hr_human_repurposing/hr_human_repurposing_completo.md"}
    ],
    "edges": [
        {"source": "miss_doll", "target": "gloss_trance", "relation": "features", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "smart_home_stepford", "target": "voute_anais", "relation": "belongs_to", "confidence": "EXTRACTED", "confidence_score": 1.0}
    ],
    "hyperedges": [],
    "input_tokens": 45000,
    "output_tokens": 1500
}

output_dir = Path('graphify-out')
output_dir.mkdir(exist_ok=True)
(output_dir / '.graphify_chunk_06.json').write_text(json.dumps(chunk_06, indent=2, ensure_ascii=False), encoding='utf-8')
(output_dir / '.graphify_chunk_13_15.json').write_text(json.dumps(chunk_lit_anthology, indent=2, ensure_ascii=False), encoding='utf-8')
