import json
from pathlib import Path

# Chunk 05 - Personajes Principales
chunk_05 = {
    "nodes": [
        {"id": "miss_doll", "label": "Miss Doll (The Predator)", "file_type": "document", "source_file": "02_Personajes/01_Principales/miss_doll/ficha_miss_doll.md"},
        {"id": "anais_belland", "label": "Anaïs Belland", "file_type": "document", "source_file": "02_Personajes/01_Principales/anais/ficha_anais.md"},
        {"id": "bob_platinum", "label": "Platinum Asymmetric Bob", "file_type": "rationale", "source_file": "02_Personajes/01_Principales/miss_doll/ficha_miss_doll.md"},
        {"id": "stealth_protocol", "label": "Stealth Protocol", "file_type": "rationale", "source_file": "02_Personajes/01_Principales/miss_doll/ficha_miss_doll.md"}
    ],
    "edges": [
        {"source": "miss_doll", "target": "stealth_protocol", "relation": "implements", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "miss_doll", "target": "bob_platinum", "relation": "features", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "anais_belland", "target": "miss_doll", "relation": "allied_with", "confidence": "INFERRED", "confidence_score": 0.85}
    ],
    "hyperedges": [],
    "input_tokens": 18000,
    "output_tokens": 900
}

# Chunk 10 - Literatura en Progreso (La Piel Que Diseño)
chunk_10 = {
    "nodes": [
        {"id": "la_piel_que_diseno", "label": "La Piel Que Diseño (Project)", "file_type": "document", "source_file": "03_Literatura/01_En_Progreso/la_piel_que_diseno/borradores/arco/arco_maestro_v1_anterior.md"},
        {"id": "matias", "label": "Matías (Protagonist)", "file_type": "document", "source_file": "03_Literatura/01_En_Progreso/la_piel_que_diseno/borradores/arco/arco_maestro_v1_anterior.md"},
        {"id": "daniela", "label": "Daniela (Antagonist)", "file_type": "document", "source_file": "03_Literatura/01_En_Progreso/la_piel_que_diseno/borradores/arco/arco_maestro_v1_anterior.md"},
        {"id": "curva_rendicion", "label": "Curva de Rendición", "file_type": "rationale", "source_file": "03_Literatura/01_En_Progreso/la_piel_que_diseno/borradores/arco/arco_maestro_v1_anterior.md"}
    ],
    "edges": [
        {"source": "la_piel_que_diseno", "target": "matias", "relation": "features", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "la_piel_que_diseno", "target": "daniela", "relation": "features", "confidence": "EXTRACTED", "confidence_score": 1.0},
        {"source": "daniela", "target": "matias", "relation": "controls", "confidence": "EXTRACTED", "confidence_score": 0.9},
        {"source": "la_piel_que_diseno", "target": "curva_rendicion", "relation": "follows", "confidence": "EXTRACTED", "confidence_score": 1.0}
    ],
    "hyperedges": [],
    "input_tokens": 20000,
    "output_tokens": 1000
}

# Chunk 12 - Literatura Finalizada
chunk_12 = {
    "nodes": [
        {"id": "mandato_tacones", "label": "El Mandato de los Tacones", "file_type": "document", "source_file": "03_Literatura/02_Finalizadas/el_mandato_de_los_tacones/El_mandato_de_los_tacones.md"},
        {"id": "el_collar_de_nancy", "label": "El Collar de Nancy", "file_type": "document", "source_file": "03_Literatura/02_Finalizadas/el_collar_de_nancy/el_collar_de_nancy_substack_ready.md"}
    ],
    "edges": [
        {"source": "mandato_tacones", "target": "stiletto_rule", "relation": "references", "confidence": "INFERRED", "confidence_score": 0.9}
    ],
    "hyperedges": [],
    "input_tokens": 15000,
    "output_tokens": 700
}

output_dir = Path('graphify-out')
output_dir.mkdir(exist_ok=True)
(output_dir / '.graphify_chunk_05.json').write_text(json.dumps(chunk_05, indent=2, ensure_ascii=False), encoding='utf-8')
(output_dir / '.graphify_chunk_10.json').write_text(json.dumps(chunk_10, indent=2, ensure_ascii=False), encoding='utf-8')
(output_dir / '.graphify_chunk_12.json').write_text(json.dumps(chunk_12, indent=2, ensure_ascii=False), encoding='utf-8')
