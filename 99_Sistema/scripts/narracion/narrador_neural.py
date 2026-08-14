import asyncio
import os
import re
import subprocess
import sys
import edge_tts

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

DEFAULT_MD = r"c:\Users\farid\LaVouteDAnais\03_Literatura\01_En_Progreso\cafe_con_piernas\capitulo_01_el_turno_de_prueba_v0.13.md"
DEFAULT_VOICE = "es-ES-ElviraNeural"

def clean_markdown_text(text: str) -> str:
    # Eliminar títulos markdown y separadores
    text = re.sub(r"#+\s*", "", text)
    text = re.sub(r"\*{3,}", "", text)
    text = re.sub(r"\*{1,2}", "", text)
    text = re.sub(r"—", ", ", text)
    text = re.sub(r"`.*?`", "", text)
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    # Reemplazar saltos de línea múltiples por puntos o pausas naturales
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    return "\n\n".join(paragraphs)

async def generate_audio(md_path: str, voice: str, output_mp3: str):
    print(f"📖 Leyendo texto de: {md_path}")
    with open(md_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned = clean_markdown_text(raw_text)
    print(f"🎙️ Generando audio neural con voz '{voice}' ({len(cleaned.split())} palabras)...")
    print("⏳ Conectando con Edge Neural TTS service...")
    
    communicate = edge_tts.Communicate(
        text=cleaned,
        voice=voice,
        rate="-2%",
        pitch="+0Hz"
    )
    
    await communicate.save(output_mp3)
    print(f"✅ Audiolibro MP3 generado exitosamente en:\n   {output_mp3}")

def play_audio(mp3_path: str):
    print(f"🔊 Iniciando reproducción en vivo por los parlantes...")
    # Abrir el reproductor predeterminado de Windows o iniciar reproducción
    try:
        # Abre el archivo MP3 con el reproductor del sistema
        os.startfile(mp3_path)
    except Exception as e:
        print(f"Aviso al iniciar reproductor: {e}")
        subprocess.Popen(["powershell", "-c", f'(New-Object -ComObject WMPlayer.OCX).openPlayer("{mp3_path}")'])

async def main():
    md_file = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MD
    voice = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_VOICE
    
    # Nombre del archivo MP3 de salida
    base_name = os.path.splitext(os.path.basename(md_file))[0]
    out_dir = os.path.dirname(md_file)
    output_mp3 = os.path.join(out_dir, f"{base_name}_{voice.split('-')[-1].replace('Neural','')}.mp3")

    await generate_audio(md_file, voice, output_mp3)
    play_audio(output_mp3)

if __name__ == "__main__":
    asyncio.run(main())
