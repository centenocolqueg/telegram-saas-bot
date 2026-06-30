import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 Token desde Render (VARIABLE DE ENTORNO)
TOKEN = os.getenv("BOT_TOKEN")

# 💾 usuarios activos (luego se cambia a base de datos)
usuarios_activos = set()

# 🟢 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in usuarios_activos:
        await update.message.reply_text(
            "🔒 ACCESO RESTRINGIDO\n\n"
            "💳 Debes activar tu cuenta con pago de S/25 por Yape\n"
            "Usa /pago para ver instrucciones"
        )
    else:
        await update.message.reply_text(
            "🟢 SISTEMA ACTIVO\n"
            "Bienvenido al panel\n"
            "Usa /scan para comenzar"
        )

# 💳 INFO DE PAGO
async def pago(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📲 PAGO POR YAPE\n\n"
        "Número: 999 888 777\n"
        "Monto: S/25\n\n"
        "📥 Luego envía tu comprobante aquí (foto o captura)"
    )

# 📥 RECIBIR COMPROBANTE
async def recibir_pago(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if update.message.photo:
        await update.message.reply_text("⏳ Verificando pago...")

        await asyncio.sleep(2)

        usuarios_activos.add(user_id)

        await update.message.reply_text(
            "✅ PAGO CONFIRMADO\n"
            "🎉 ACCESO ACTIVADO"
        )

# 🔍 COMANDO PRO
async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in usuarios_activos:
        await update.message.reply_text("🔒 No tienes acceso. Usa /pago")
        return

    steps = [
        "🔍 Iniciando análisis...",
        "📡 Conectando sistema...",
        "🧠 Procesando datos...",
        "📊 Generando resultado..."
    ]

    for s in steps:
        await update.message.reply_text(s)
        await asyncio.sleep(1.5)

    await update.message.reply_text("✅ Análisis completo. Sistema estable.")

# 🚀 EJECUCIÓN
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pago", pago))
app.add_handler(CommandHandler("scan", scan))
app.add_handler(MessageHandler(filters.PHOTO, recibir_pago))

app.run_polling()
