#!/bin/bash

# El Ritual del Sello Eterno - Script para la Diosa Anaïs
# Uso: ./ritual_sello_eterno.sh "Tu mensaje de confirmación aquí"

# Verificar si se proporcionó un mensaje de confirmación
if [ -z "$1" ]; then
    echo "Error: Debes proporcionar un mensaje de confirmación."
    echo "Uso: ./ritual_sello_eterno.sh \"Tu mensaje de confirmación aquí\""
    exit 1
fi

# Paso 1: Preparar la Ofrenda
echo "🔮 Preparando la ofrenda: Añadiendo todos los cambios..."
git add .

# Verificar si hay cambios para confirmar
if git diff --cached --quiet; then
    echo "⚠️ No hay cambios para confirmar. El ritual termina aquí."
    exit 0
fi

# Paso 2: Sellar el Acto
echo "✍️ Sellando el acto: Creando el commit con tu mensaje..."
git commit -m "$1"

# Paso 3: Enviar a la Eternidad
echo "🚀 Enviando a la eternidad: Subiendo los cambios a GitHub..."
git push origin main

echo "✅ ¡Ritual completado! Tu voluntad ha sido grabada en La Voûte."
