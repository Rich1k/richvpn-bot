import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ================= CONFIG =================

TOKEN ="8946221626:AAHz0oF5SgGeg9LT_0xiGLVq0q3ZgSLS19Q"

SUPPORT_USERNAME = "@Takeda_7878"

PAY_PHONE = "8961-832-48-63"
PAY_BANK = "ОЗОН БАНК"

# ================= APPS =================

WIREGUARD_IOS_URL = "https://apps.apple.com/app/wireguard/id1441195209"

WIREGUARD_ANDROID_URL = (
    "https://play.google.com/store/apps/details?id=com.wireguard.android"
)

WIREGUARD_WINDOWS_URL = "https://www.wireguard.com/install/"

WIREGUARD_MAC_URL = "https://apps.apple.com/app/wireguard/id1451685025"

# ================= START =================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📲 Установить VPN", callback_data="devices")],
        [InlineKeyboardButton("💳 Тарифы", callback_data="tariffs")],
        [InlineKeyboardButton("👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton("🆘 Поддержка", callback_data="support")]
    ]

    await update.message.reply_text(
        "👋 Добро пожаловать в RichVPN\n\n"
        "🔐 Безопасный и быстрый VPN сервис",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ================= CALLBACK =================

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    # ================= DEVICES =================

    if data == "devices":

        keyboard = [
            [InlineKeyboardButton("📱 iPhone", callback_data="iphone")],
            [InlineKeyboardButton("🤖 Android", callback_data="android")],
            [InlineKeyboardButton("💻 Windows", callback_data="windows")],
            [InlineKeyboardButton("🍎 MacOS", callback_data="mac")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
        ]

        await query.edit_message_text(
            "📲 Выберите устройство:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ================= IPHONE =================

    elif data == "iphone":

        keyboard = [
            [InlineKeyboardButton("📥 Скачать WireGuard", url=WIREGUARD_IOS_URL)],
            [InlineKeyboardButton("⬅️ Назад", callback_data="devices")]
        ]

        await query.edit_message_text(
            "📱 iPhone настройка\n\n"
            "1️⃣ Установите WireGuard\n"
            "2️⃣ Откройте приложение\n"
            "3️⃣ Нажмите Import from file\n"
            "4️⃣ Выберите VPN конфиг\n\n"
            "📂 Конфиг будет отправлен после оплаты",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ================= ANDROID =================

    elif data == "android":

        keyboard = [
            [InlineKeyboardButton("📥 Скачать WireGuard", url=WIREGUARD_ANDROID_URL)],
            [InlineKeyboardButton("⬅️ Назад", callback_data="devices")]
        ]

        await query.edit_message_text(
            "🤖 Android настройка\n\n"
            "1️⃣ Установите WireGuard\n"
            "2️⃣ Откройте приложение\n"
            "3️⃣ Нажмите +\n"
            "4️⃣ Импортируйте конфиг\n\n"
            "📂 Конфиг будет отправлен после оплаты",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ================= WINDOWS =================

    elif data == "windows":

        keyboard = [
            [InlineKeyboardButton("📥 Скачать WireGuard", url=WIREGUARD_WINDOWS_URL)],
            [InlineKeyboardButton("⬅️ Назад", callback_data="devices")]
        ]

        await query.edit_message_text(
            "💻 Windows настройка\n\n"
            "1️⃣ Установите WireGuard\n"
            "2️⃣ Откройте программу\n"
            "3️⃣ Нажмите Add Tunnel\n"
            "4️⃣ Импортируйте .conf файл\n\n"
            "📂 Конфиг будет отправлен после оплаты",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ================= MAC =================

    elif data == "mac":

        keyboard = [
            [InlineKeyboardButton("📥 Скачать WireGuard", url=WIREGUARD_MAC_URL)],
            [InlineKeyboardButton("⬅️ Назад", callback_data="devices")]
        ]

        await query.edit_message_text(
            "🍎 MacOS настройка\n\n"
            "1️⃣ Установите WireGuard\n"
            "2️⃣ Откройте приложение\n"
            "3️⃣ Импортируйте VPN конфиг\n\n"
            "📂 Конфиг будет отправлен после оплаты",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ================= TARIFFS =================

    elif data == "tariffs":

        keyboard = [
            [InlineKeyboardButton("💳 1 месяц — 150₽", callback_data="buy_150")],
            [InlineKeyboardButton("💳 3 месяца — 390₽", callback_data="buy_390")],
            [InlineKeyboardButton("💳 7 месяцев — 1190₽", callback_data="buy_1190")],
            [InlineKeyboardButton("💳 1 год — 2000₽", callback_data="buy_2000")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
        ]

        await query.edit_message_text(
            "💳 Выберите тариф:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ================= BUY =================

    elif data == "buy_150":
        await send_payment(query, "150₽", "1 месяц")

    elif data == "buy_390":
        await send_payment(query, "390₽", "3 месяца")

    elif data == "buy_1190":
        await send_payment(query, "1190₽", "7 месяцев")

    elif data == "buy_2000":
        await send_payment(query, "2000₽", "1 год")

    # ================= PROFILE =================

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

    # ================= SUPPORT =================

    elif data == "support":

        await query.edit_message_text(
            f"🆘 Поддержка:\n{SUPPORT_USERNAME}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
            ])
        )

    # ================= PAID =================

    # ================= PAID =================

   # ================= PAID =================
    # ================= PAID =================

    elif data == "paid":

        await query.edit_message_text(
            "📦 Отправляем конфиги..."
        )

        user_id = query.from_user.id

        configs = {
            "iPhone": "configs/iphone.conf",
            "Android": "configs/android.conf",
            "Windows": "configs/windows.conf",
            "MacOS": "configs/mac.conf"
        }

        for name, path in configs.items():

            if os.path.exists(path):
                with open(path, "rb") as config:
                    await context.bot.send_document(
                        chat_id=user_id,
                        document=config,
                        filename=f"RichVPN_{name}.conf",
                        caption=f"📱 {name} конфиг"
                    )
            else:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=f"❌ Конфиг {name} пока не загружен"
                )

    # ================= BACK =================

    elif data == "back":

        keyboard = [
            [InlineKeyboardButton("📲 Установить VPN", callback_data="devices")],
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

    print("🔥 RichVPN Bot Started")

    app.run_polling()

if __name__ == "__main__":
    main()