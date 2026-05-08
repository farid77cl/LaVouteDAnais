import json
from pathlib import Path

# Chunk 0
chunk_0 = {
    "nodes": [
        {"id": "voute_anais", "label": "La Voûte d'Anaïs", "file_type": "document", "source_file": "README.md"},
        {"id": "ele_v3_5", "label": "Ele (V3.5 Hard-Sync)", "file_type": "document", "source_file": "00_Ele/identidad_ele.md"},
        {"id": "miss_doll_v5", "label": "Miss Doll (V5.0)", "file_type": "document", "source_file": "ele_master_audit_v3_7.md"},
        {"id": "hard_sync_protocol", "label": "V3.5 Hard-Sync Protocol", "file_type": "rationale", "source_file": "00_Ele/identidad_ele.md"},
        {"id": "stiletto_rule", "label": "Stiletto Rule (9-11 in)", "file_type": "rationale", "source_file": "00_Ele/galeria_outfits.md"},
        {"id": "bimbofication", "label": "Bimbofication Theme", "file_type": "document", "source_file": "00_Ele/identidad_ele.md"}
    ],
    "edges": [
        {"source": "ele_v3_5", "target": "hard_sync_protocol", "relation": "implements", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "ele_v3_5", "target": "stiletto_rule", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "miss_doll_v5", "target": "voute_anais", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "ele_v3_5", "target": "bimbofication", "relation": "conceptually_related_to", "confidence": "INFERRED", "confidence_score": 0.95}
    ],
    "hyperedges": [],
    "input_tokens": 15000,
    "output_tokens": 800
}

# Chunk 1
chunk_1 = {
    "nodes": [
        {"id": "prompt_bank_v04", "label": "Banco Prompts V04 (Fetish)", "file_type": "document", "source_file": "00_Ele/bancos_prompts/banco_prompts_v04_fetish.md"},
        {"id": "prompt_bank_v11", "label": "Banco Prompts V11 (Office)", "file_type": "document", "source_file": "00_Ele/bancos_prompts/banco_prompts_v11_office.md"},
        {"id": "high_gloss_material", "label": "High-Gloss Materials (Vinyl/PVC)", "file_type": "document", "source_file": "00_Ele/galeria_outfits.md"}
    ],
    "edges": [
        {"source": "prompt_bank_v04", "target": "high_gloss_material", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "prompt_bank_v11", "target": "ele_v3_5", "relation": "references", "confidence": "EXTRACTED", "confidence_score": 1.0}
    ],
    "hyperedges": [],
    "input_tokens": 12000,
    "output_tokens": 600
}

output_dir = Path('graphify-out')
output_dir.mkdir(exist_ok=True)
(output_dir / '.graphify_chunk_00.json').write_text(json.dumps(chunk_0, indent=2, ensure_ascii=False), encoding='utf-8')
(output_dir / '.graphify_chunk_01.json').write_text(json.dumps(chunk_1, indent=2, ensure_ascii=False), encoding='utf-8')
