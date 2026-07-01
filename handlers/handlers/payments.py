import asyncio
from database import activate_user

async def pago(update, context):
    await update.message.reply_text("📲 Paga por Yape S/25")

async def recibir_pago(update, context):
    if update.message.photo:
        await update.message.reply_text("⏳ Validando...")
        await asyncio.sleep(2)

        activate_user(update.effective_user.id)

        await update.message.reply_text("✅ Acceso activado")
