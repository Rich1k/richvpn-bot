from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "8946221626:AAHz0oF5SgGeg9LT_0xiGLVq0q3ZgSLS19Q"
SUPPORT = "@Takeda_7878"


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 Тарифы", callback_data="tariffs")],
        [InlineKeyboardButton("👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton("🆘 Поддержка", callback_data="support")],
        [InlineKeyboardButton("💰 Оплата", callback_data="payment")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Добро пожаловать в RichVPN\n\n"
        "🔐 Быстрый и безопасный VPN\n\n"
        "Выберите действие:",
        reply_markup=reply_markup,
    )


# кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    # тарифы
    if data == "tariffs":
        keyboard = [
            [InlineKeyboardButton("1 месяц — 150₽", callback_data="buy_1")],
            [InlineKeyboardButton("3 месяца — 390₽", callback_data="buy_3")],
            [InlineKeyboardButton("1 год — 2000₽", callback_data="buy_12")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")],
        ]

        await query.edit_message_text(
            "💳 Тарифы RichVPN\n\nВыберите план:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    # профиль
    elif data == "profile":
        user = query.from_user

        await query.edit_message_text(
            f"👤 Профиль\n\n"
            f"ID: {user.id}\n"
            f"Имя: {user.first_name}\n"
            f"Статус: ❌ Нет подписки",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ]),
        )

    # поддержка
    elif data == "support":
        await query.edit_message_text(
            f"🆘 Поддержка RichVPN\n\n"
            f"Писать сюда:\n{SUPPORT}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ]),
        )

    # оплата
    elif data == "payment":
        await query.edit_message_text(
            "💰 Способы оплаты\n\n"
            "🇷🇺 ЮKassa / карты\n"
            "💎 Telegram Stars\n"
            "₿ Crypto (USDT)\n\n"
            "Авто-оплата скоро будет подключена.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ]),
        )

    # покупка
    elif data.startswith("buy_"):
        plan = data.split("_")[1]

        plans = {
            "1": "1 месяц — 150₽",
            "3": "3 месяца — 390₽",
            "12": "1 год — 2000₽",
        }

        await query.edit_message_text(
            f"🛒 Вы выбрали:\n{plans.get(plan)}\n\n"
            "💰 Оплата пока в разработке\n"
            "🔐 После оплаты будет выдан VPN-конфиг",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="tariffs")]
            ]),
        )

    # назад
    elif data == "back":
        keyboard = [
            [InlineKeyboardButton("💳 Тарифы", callback_data="tariffs")],
            [InlineKeyboardButton("👤 Профиль", callback_data="profile")],
            [InlineKeyboardButton("🆘 Поддержка", callback_data="support")],
            [InlineKeyboardButton("💰 Оплата", callback_data="payment")],
        ]

        await query.edit_message_text(
            "🏠 Главное меню",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()