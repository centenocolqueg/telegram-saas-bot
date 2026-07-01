import asyncio
from database import has_access

async def scan(update, context):
    user_id = update.effective_user.id

    if not has_access(user_id):
        await update.message.reply_text("🔒 No tienes acceso. Usa /pago")
        return

    steps = [
        "🔍 Iniciando análisis...",
        "📡 Conectando sistema...",
        "🧠 Procesando datos...",
        "📊 Generando reporte..."
    ]

    for step in steps:
        await update.message.reply_text(step)
        await asyncio.sleep(1.5)

    await update.message.reply_text("✅ Análisis completo")
