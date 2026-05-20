import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔐 TOKEN (Railway / Render env)
TOKEN = os.getenv("8946221626:AAHz0oF5SgGeg9LT_0xiGLVq0q3ZgSLS19Q")

# 📲 WireGuard iOS
WIREGUARD_IOS_URL = "https://apps.apple.com/app/wireguard/id1441195209"

# 👨‍💻 SUPPORT
SUPPORT_USERNAME = "@Takeda_7878"


# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📲 Установить VPN (iOS)", callback_data="install_vpn")],
        [InlineKeyboardButton("💳 Тарифы", callback_data="tariffs")],
        [InlineKeyboardButton("👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton("🆘 Поддержка", callback_data="support")]
    ]

    await update.message.reply_text(
        "👋 Добро пожаловать в *RichVPN*\n\n"
        "🔐 Ваш личный VPN сервис",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ================= CALLBACK =================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    # 📲 VPN INSTALL
    if data == "install_vpn":
        await query.edit_message_text(
            "📲 Установите WireGuard на iPhone:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📲 Открыть App Store", url=WIREGUARD_IOS_URL)],
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ])
        )

    # 💳 TARIFFS
    elif data == "tariffs":
        await query.edit_message_text(
            "💳 Тарифы RichVPN:\n\n"
            "• 1 месяц — 150₽\n"
            "• 3 месяца — 390₽\n"
            "• 7 месяцев — 1190₽\n\n"
            "💡 Оплата скоро будет доступна",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ])
        )

    # 👤 PROFILE
    elif data == "profile":
        user = query.from_user

        await query.edit_message_text(
            f"👤 Профиль\n\n"
            f"ID: {user.id}\n"
            f"Имя: {user.first_name}\n"
            f"Статус: ❌ Нет подписки",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ])
        )

    # 🆘 SUPPORT
    elif data == "support":
        await query.edit_message_text(
            f"🆘 Поддержка:\n{SUPPORT_USERNAME}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ])
        )

    # 🔙 BACK
    elif data == "back":
        keyboard = [
            [InlineKeyboardButton("📲 Установить VPN (iOS)", callback_data="install_vpn")],
            [InlineKeyboardButton("💳 Тарифы", callback_data="tariffs")],
            [InlineKeyboardButton("👤 Профиль", callback_data="profile")],
            [InlineKeyboardButton("🆘 Поддержка", callback_data="support")]
        ]

        await query.edit_message_text(
            "🏠 Главное меню",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# ================= MAIN =================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("🔥 RichVPN bot started")
    app.run_polling()


if __name__ == "__main__":
    main()