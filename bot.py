import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔐 токен берём из переменных среды (Railway / Render)
TOKEN = os.getenv("8946221626:AAHz0oF5SgGeg9LT_0xiGLVq0q3ZgSLS19Q")

# 📲 WireGuard iOS
WIREGUARD_IOS_URL = "https://apps.apple.com/app/wireguard/id1441195209"


# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📲 Установить VPN (iOS)", callback_data="install_vpn")],
        [InlineKeyboardButton("💳 Тарифы", callback_data="tariffs")],
        [InlineKeyboardButton("👤 Профиль", callback_data="profile")]
    ]

    await update.message.reply_text(
        "👋 Добро пожаловать в *RichVPN*\n\n"
        "🔐 Выберите действие:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ================= CALLBACK =================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    # 📲 УСТАНОВКА VPN
    if data == "install_vpn":
        keyboard = [
            [InlineKeyboardButton("📲 WireGuard в App Store", url=WIREGUARD_IOS_URL)],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
        ]

        await query.edit_message_text(
            "📲 Установите VPN приложение на iPhone:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # 💳 ТАРИФЫ
    elif data == "tariffs":
        keyboard = [
            [InlineKeyboardButton("1 месяц — 150₽", callback_data="buy_1")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
        ]

        await query.edit_message_text(
            "💳 Тарифы RichVPN:\n\n"
            "• 1 месяц — 150₽\n"
            "• 3 месяца — 390₽\n"
            "• 7 месяцев — 1190₽\n",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # 👤 ПРОФИЛЬ
    elif data == "profile":
        user = query.from_user

        await query.edit_message_text(
            f"👤 Профиль\n\n"
            f"ID: {user.id}\n"
            f"Имя: {user.first_name}\n"
            f"Статус: ❌ Нет подписки"
        )

    # 🔙 НАЗАД
    elif data == "back":
        keyboard = [
            [InlineKeyboardButton("📲 Установить VPN (iOS)", callback_data="install_vpn")],
            [InlineKeyboardButton("💳 Тарифы", callback_data="tariffs")],
            [InlineKeyboardButton("👤 Профиль", callback_data="profile")]
        ]

        await query.edit_message_text(
            "🏠 Главное меню:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# ================= MAIN =================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()