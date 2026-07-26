# 📱 Prompt #20 · LV-App 2.0 — PASO 6: Consola Ops + Git Live Sync

> **Requiere P2/P3 verdes** (LookRepository) y P2 (GitRepository).
> **Este paso:** dashboard de operaciones — estado de la flota L200-L800, siguiente pendiente, y sync Git en vivo.
> **Si aterriza roto:** patch como **Prompt #20.6.x**.

---

## ⚠️ REGLAS
1. Genera SOLO los archivos listados. Reutiliza LookRepository y GitRepository.
2. Debe compilar: el dashboard muestra métricas reales y el botón de sync hace pull.

---

```markdown
PASO 6 de LV-App 2.0. Llena la pestaña CONSOLA OPS (pestaña 4).

## ARCHIVOS A GENERAR (SOLO ESTOS)
1. domain/FleetStats.kt + data/FleetStatsUseCase.kt
   - Calcula desde LookRepository: total de looks, % materializado (poses con imagen / poses esperadas),
     looks incompletos, y el "siguiente pendiente" (primer look con poses faltantes) con qué poses le faltan.
   - Desglose por tramos (L200-L299, L300-L499, L500-L699, L700-L800).

2. data/git/GitStatus.kt (extiende GitRepository)
   - Expone branch actual, último commit (hash + mensaje), y ahead/behind respecto al remoto.
   - `suspend fun pull()` con resultado (ok / conflicto / error) sin crashear.

3. ui/screens/ops/OpsScreen.kt (reemplaza placeholder)
   - Tarjetas dashboard: % flota materializada (con barra por tramo), tarjeta "Siguiente pendiente"
     (nº de look + poses faltantes, con acción "ir a Visual"), y tarjeta Git (branch, último commit,
     estado de sync) con botón "Sincronizar ahora" (Git Live).
   - Indicador de estado de sync (idle / sincronizando / ok / error).

4. ui/screens/ops/OpsViewModel.kt — estado de métricas + git.

5. FleetStatsTest.kt — test real: dado un set de looks de ejemplo, calcula % y siguiente pendiente correctos.

## CRITERIO DE ÉXITO
Compila · el dashboard muestra el % real de flota y el desglose por tramo · "Siguiente pendiente" apunta
al look correcto y navega a Visual · la tarjeta Git muestra branch+commit y "Sincronizar ahora" hace pull.

Entrega SOLO estos 5 puntos. Siguiente: P7 (EVE Core).
```
