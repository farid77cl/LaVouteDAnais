# -*- coding: utf-8 -*-
"""
Recorta el header del blog de Tumblr a su banda ancha, midiendo en vez de adivinar.

POR QUE EXISTE (07/09/2026)
---------------------------
El header de @lavoutedeanais se genera en Gemini en 16:9 y el blog lo muestra como
una banda ancha (~3:1). Tres generaciones seguidas se le pidio al generador que
dejara el quinto superior e inferior vacios y que la figura cupiera en los tres
quintos centrales. Las tres veces fallo, y de tres formas distintas:

  v1  dibujo la sala como panel inset y dejo a la figura salirse: cabeza arriba
      del panel, tacones abajo.
  v2  entendio "franjas vacias" como VIÑETAS y devolvio tres paneles apilados,
      cada uno con su propio marco. La figura seguia cruzando los dos bordes.
  v3  ya salio con un solo marco -lo unico que si se arreglo por texto- pero la
      figura seguia ocupando ~85% del alto en vez del 60% pedido.

La conclusion es geometrica y no de redaccion: **un generador de imagenes no
cuenta quintos**, y ademas una figura de cuerpo entero DE PIE dentro de una banda
3:1 obliga a dibujarla diminuta, que es un header debil. El encuadre se resuelve
despues, cortando con numeros.

Y la regla de composicion que sale de esto: **una cabeza cortada arruina un
header; unos pies cortados no los echa de menos nadie.** Por eso el anclaje por
defecto es ARRIBA y no al centro.

DUEÑO
-----
Spec del flujo: `99_Sistema/specs/2026-09-07-publicacion-tumblr-design.md` §6.
Estilo de la imagen: `01_Canon/Guias_Especializadas/estilo_comic_pop_v1.md`.

FECHA DE MUERTE
---------------
Vive mientras el blog use un header generado en 16:9. Si algun dia el generador
entrega la banda ancha directa, este script se archiva.

USO
---
    python 99_Sistema/scripts/rrss/recortar_header_tumblr.py <entrada.png>
    python ... <entrada.png> --anclaje centro
    python ... <entrada.png> --anclaje fraccion --desde 0.08
    python ... <entrada.png> --ratio 2.844 --ancho-final 3000
    python ... <entrada.png> --salida ruta/explicita.png

No escribe nada hasta haber impreso la banda exacta que va a cortar.
"""
import argparse
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # la consola de Windows es cp1252

try:
    from PIL import Image
except ImportError:
    sys.exit("Falta Pillow. Instalar con: python -m pip install Pillow")


def banda(alto, alto_banda, anclaje, desde):
    """Devuelve (y0, y1) de la banda a recortar, ya recortada a los bordes."""
    if alto_banda >= alto:
        return 0, alto
    if anclaje == "arriba":
        y0 = 0
    elif anclaje == "centro":
        y0 = (alto - alto_banda) // 2
    elif anclaje == "abajo":
        y0 = alto - alto_banda
    else:  # fraccion
        y0 = int(round(desde * alto))
    y0 = max(0, min(y0, alto - alto_banda))
    return y0, y0 + alto_banda


def main():
    ap = argparse.ArgumentParser(description="Recorta un header a banda ancha para Tumblr.")
    ap.add_argument("entrada", help="PNG de origen (normalmente 16:9)")
    ap.add_argument("--ratio", type=float, default=3.0,
                    help="ancho/alto de la banda final (3.0 por defecto; Tumblr recomienda 3000x1055 = 2.844)")
    ap.add_argument("--anclaje", choices=["arriba", "centro", "abajo", "fraccion"], default="arriba",
                    help="donde se apoya la banda. 'arriba' protege la cabeza y es el default a proposito")
    ap.add_argument("--desde", type=float, default=0.0,
                    help="con --anclaje fraccion: borde superior de la banda como fraccion del alto (0.0-1.0)")
    ap.add_argument("--ancho-final", type=int, default=None,
                    help="si se pasa, reescala la banda a este ancho conservando la proporcion")
    ap.add_argument("--salida", default=None, help="ruta de salida (por defecto <entrada>_<ratio>.png)")
    args = ap.parse_args()

    src = Path(args.entrada)
    if not src.exists():
        sys.exit("No existe: %s" % src)
    if args.ratio <= 0:
        sys.exit("--ratio tiene que ser mayor que 0")

    with Image.open(src) as im:
        ancho, alto = im.size
        alto_banda = int(round(ancho / args.ratio))

        if alto_banda > alto:
            sys.exit(
                "La imagen es demasiado baja para esa banda: %dx%d da %d px de alto y solo hay %d.\n"
                "Se necesita una fuente mas alta o un --ratio menos ancho." % (ancho, alto, alto_banda, alto)
            )

        y0, y1 = banda(alto, alto_banda, args.anclaje, args.desde)

        print("=" * 66)
        print("RECORTE DE HEADER — %s" % src.name)
        print("=" * 66)
        print("  origen        : %d x %d  (ratio %.3f)" % (ancho, alto, ancho / alto))
        print("  banda pedida  : ratio %.3f  ->  %d x %d" % (args.ratio, ancho, alto_banda))
        print("  anclaje       : %s" % args.anclaje)
        print("  corte en Y    : %d .. %d   (se descarta %d px arriba y %d px abajo)"
              % (y0, y1, y0, alto - y1))
        print("  conserva      : %.1f%% del alto original" % (100.0 * alto_banda / alto))

        out = im.crop((0, y0, ancho, y1))

        if args.ancho_final:
            nuevo_alto = int(round(args.ancho_final / args.ratio))
            out = out.resize((args.ancho_final, nuevo_alto), Image.LANCZOS)
            print("  reescalado a  : %d x %d" % (args.ancho_final, nuevo_alto))

        dest = Path(args.salida) if args.salida else src.with_name(
            "%s_%sx1%s" % (src.stem, ("%.3f" % args.ratio).rstrip("0").rstrip("."), src.suffix))
        dest.parent.mkdir(parents=True, exist_ok=True)
        out.save(dest)
        print("-" * 66)
        print("  escrito       : %s  (%d x %d)" % (dest, out.size[0], out.size[1]))
        print("=" * 66)
        print("Revisar A OJO que la cabeza quedo entera antes de subirlo al blog.")


if __name__ == "__main__":
    main()
