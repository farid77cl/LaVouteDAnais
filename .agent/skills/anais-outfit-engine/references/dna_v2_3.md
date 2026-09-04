# ADN de Anais Belland (v2.3) — DOCUMENTO DERROGADO, ES UN PUNTERO

> ⛔ **Este archivo YA NO contiene el BLOQUE A.** Lo contuvo hasta el 04/09/2026 y por eso
> aparecia como divergencia permanente en `outfit.py adn`: era una copia que se quedaba vieja
> cada vez que el ADN real cambiaba, que es exactamente el modo de falla que la regla de
> dueno unico existe para matar (llego a haber tres flotas distintas en tres archivos).

## Dueno unico del BLOQUE A de Anais

`02_Personajes/_perfiles_visuales/anais.md` §2, dentro del fence `<!-- ADN:BLOQUE_A -->`.

Lo lee el motor por su cuenta (`PromptBuilder.bloque_a`); **no se copia a mano en ninguna parte.**
Verificable con `python 99_Sistema/scripts/visual/outfit.py adn`.

## Que habia aqui

El ADN v2.3 de la era en que Anais no tenia perfil visual ni motor generico. Su contenido vivo
esta en el perfil; su historia, en el git log de este archivo.
