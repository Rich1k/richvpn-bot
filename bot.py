import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# 🔐 ENV (Render переменные)
TOKEN = os.getenv("8946221626:AAHz0oF5SgGeg9LT_0xiGLVq0q3ZgSLS19Q")
SHOP_ID = os.getenv("SHOP_ID")
SECRET_KEY = os.getenv("SECRET_KEY")

# 📲 WireGuard iOS
WIREGUARD_IOS_URL = "https://apps.apple.com/app/wireguard/id1441195209"

# 👨‍💻 SUPPORT
SUPPORT_USERNAME = "@Takeda_7878"

# 💳 СБП (пока вручную)
PAY_PHONE = "8924-077-71-00"
PAY_BANK = "Т-Банк"


# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📲 Установить VPN (iOS)", callback_data="install_vpn")],
        [InlineKeyboardButton("💳 Тарифы", callback_data="tariffs")],
        [InlineKeyboardButton("👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton("🆘 Поддержка", callback_data="support")]
    ]

    await update.message.reply_text(
        "👋 Добро пожаловать в RichVPN\n\n"
        "🔐 Ваш личный VPN сервис",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ================= CALLBACK =================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "install_vpn":
        await query.edit_message_text(
            "📲 Установите WireGuard на iPhone:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📲 Скачать WireGuard", url=WIREGUARD_IOS_URL)],
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ])
        )

    elif data == "tariffs":
        keyboard = [
            [InlineKeyboardButton("💳 1 месяц — 150₽", callback_data="buy_150")],
            [InlineKeyboardButton("💳 3 месяца — 390₽", callback_data="buy_390")],
            [InlineKeyboardButton("💳 7 месяцев — 1190₽", callback_data="buy_1190")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
        ]

        await query.edit_message_text(
            "💳 Выберите тариф:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == "buy_150":
        await send_payment(query, "150₽", "1 месяц")

    elif data == "buy_390":
        await send_payment(query, "390₽", "3 месяца")

    elif data == "buy_1190":
        await send_payment(query, "1190₽", "7 месяцев")

    elif data == "profile":
        user = query.from_user

        await query.edit_message_text(
            f"👤 Профиль\n\n"
            f"🆔 ID: {user.id}\n"
            f"👤 Имя: {user.first_name}\n"
            f"📡 Подписка: ❌ Нет",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ])
        )

    elif data == "support":
        await query.edit_message_text(
            f"🆘 Поддержка:\n{SUPPORT_USERNAME}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ])
        )

    elif data == "paid":
        await query.edit_message_text(
            "⏳ Платёж отправлен на проверку.\n\n"
            "После проверки вы получите VPN доступ 📲"
        )

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


# ================= PAYMENT =================
async def send_payment(query, amount, tariff):

    keyboard = [
        [InlineKeyboardButton("✅ Я оплатил", callback_data="paid")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="tariffs")]
    ]

    await query.edit_message_text(
        f"💳 Тариф: {tariff}\n"
        f"💰 Сумма: {amount}\n\n"
        f"📱 СБП номер:\n{PAY_PHONE}\n\n"
        f"🏦 Банк:\n{PAY_BANK}\n\n"
        "После оплаты нажмите кнопку: ✅ Я оплатил",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ================= MAIN =================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("🔥 Bot started")
    app.run_polling()


if __name__ == "__main__":
    main()