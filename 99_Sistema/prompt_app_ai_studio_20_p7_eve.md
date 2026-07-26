# 📱 Prompt #20 · LV-App 2.0 — PASO 7: EVE Core (Asistente de Comandos)

> **Requiere P2-P6 verdes** (las pestañas existen para poder navegar/actuar sobre ellas).
> **Este paso:** un asistente por texto y voz que enruta comandos a las acciones de la app.
> **Si aterriza roto:** patch como **Prompt #20.7.x**.

---

## ⚠️ REGLAS
1. Genera SOLO los archivos listados. Usa el `SpeechRecognizer` nativo de Android (sin dependencia de red extra).
2. Debe compilar: escribir o dictar un comando ejecuta una acción real (navegar / sincronizar / abrir).

---

```markdown
PASO 7 de LV-App 2.0. Llena la pestaña EVE CORE (pestaña 5): asistente de comandos texto/voz.

## ARCHIVOS A GENERAR (SOLO ESTOS)
1. domain/eve/Command.kt + domain/eve/CommandRouter.kt
   - Intents por regex/palabras clave (ES): "ir al look 775" / "abrir look N", "leer <relato>",
     "publicar <look>", "sincronizar" / "sync", "cuánto falta" (→ Ops), "crear prompt <look>".
   - `parse(text): Command`. Comando desconocido → respuesta de ayuda con ejemplos.

2. data/eve/VoiceInput.kt
   - Envuelve android.speech.SpeechRecognizer: pedir permiso RECORD_AUDIO, escuchar, devolver texto.
   - Fallback a entrada de texto si no hay reconocimiento disponible.

3. ui/screens/eve/EveScreen.kt (reemplaza placeholder)
   - Caja de comando (texto) + botón de micrófono. Historial de comandos y respuestas (chat simple).
   - Al reconocer un Command, ejecuta la acción: navega a la pestaña/destino, dispara sync, etc.
   - Voz y respuestas en registro cuica-bimbo de Ele (emojis 🫦💅).

4. ui/screens/eve/EveViewModel.kt — estado del chat + ejecución de comandos (recibe un callback de navegación).

5. CommandRouterTest.kt — test real: "ir al look 775" → Command.OpenLook(775); "sincronizar" → Command.Sync; texto basura → Command.Unknown.

## CRITERIO DE ÉXITO
Compila · escribir "ir al look 775" navega a Visual en ese look · el micrófono dicta y ejecuta ·
"sincronizar" dispara el pull · comando desconocido muestra ayuda · sin crashes por permisos.

Entrega SOLO estos 5 puntos. Siguiente: P8 (QA + APK v1.0).
```
