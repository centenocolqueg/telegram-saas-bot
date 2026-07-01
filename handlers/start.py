from database import has_access

async def start(update, context):
    user_id = update.effective_user.id

    if not has_access(user_id):
        await update.message.reply_text("🔒 Acceso bloqueado /pago")
    else:
        await update.message.reply_text("🟢 Sistema activo")
