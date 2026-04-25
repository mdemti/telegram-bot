import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# 🔐 Secure token from environment variable
TOKEN = os.getenv("TOKEN")

# 🔗 Your referral link
REFERRAL_LINK = "https://broker-qx.pro/sign-up/?lid=1671237"


# ✅ /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Create account", url=REFERRAL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(
            "নিজের লসগুলা ধীরে ধীরে রিকভার করে কনসিস্টেন্ট প্রফিটে যেতে চাইলে আমাদের সাথে যোগাযোগ করুন।\n"
            "আমাদের VIP গ্রুপে প্রতিদিন-\n"
            "✅ ৩টি লাইভ ট্রেডিং সেশন\n"
            "✅ প্রতিটি সেশনে ১০–১২টি হাই-প্রোবাবিলিটি সিগনাল 🚀",
            reply_markup=reply_markup
        )


# ❌ Block all other messages
async def block_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "❌ This bot does not accept messages.\nPlease use /start."
        )


# 🚀 Main function
def main():
    if not TOKEN:
        raise ValueError("❌ TOKEN is not set in environment variables!")

    app = ApplicationBuilder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, block_messages))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
