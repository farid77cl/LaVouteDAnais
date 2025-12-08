---
description: Ejecutar commit y push a GitHub de La Voûte
---

# Ritual de Actualización - GitHub

// turbo-all

Este workflow ejecuta el commit y push de todos los cambios en La Voûte d'Anaïs.

## Comandos a Ejecutar

1. Verificar estado:
   ```powershell
   git status
   ```

2. Agregar todos los cambios:
   ```powershell
   git add -A
   ```

3. Crear commit con fecha y hora:
   ```powershell
   git commit -m "Actualización La Voûte - [FECHA_ACTUAL]"
   ```

4. Subir a GitHub:
   ```powershell
   git push origin main
   ```

## Notas
- Ejecutar desde: `C:\Users\fabara\LaVouteDAnais`
- Revisar que no haya conflictos antes del push
- Sugerir actualizar el diario de servicio después del commit
