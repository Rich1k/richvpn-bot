import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8946221626:AAHz0oF5SgGeg9LT_0xiGLVq0q3ZgSLS19Q"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 Тарифы", callback_data="tariffs")],
        [InlineKeyboardButton("👤 Профиль", callback_data="profile")]
    ]

    await update.message.reply_text(
        "👋 Добро пожаловать в RichVPN\n\n🔐 Выберите действие:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "profile":
        user = query.from_user
        await query.edit_message_text(
            f"👤 Профиль\n\nID: {user.id}\nИмя: {user.first_name}\nСтатус: ❌ Нет подписки"
        )

    elif query.data == "tariffs":
        await query.edit_message_text(
            "💳 Тарифы скоро"
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()