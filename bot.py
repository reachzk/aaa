from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8581238484:AAEMGjYjO3BgFPCD8PCYEkqy4QVBa-ij-GQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Get Payment Details", callback_data="payment")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome!\n\nClick below to receive payment details.",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "payment":
        await query.edit_message_text(
            "💎 Payment Details:\n\n"
            "Network: TRC20\n"
            "Coin: USDT\n"
            "Wallet:\n"
            "0x0E91C9A766f5197869859cc73F5D68c73674C657\n\n"
            "After payment, send the screenshot here."
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
