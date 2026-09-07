import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8818197058:AAGDAuczc-VYj90zgo0g2WwtttKvW_mHA3M"

app = Flask(__name__)

telegram_app = Application.builder().token(TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    await update.message.reply_text(
        f"أهلاً {user.first_name} 👋\n\n"
        "🚀 أهلاً بك في Exchange Referrals\n\n"
        "اضغط الزر بالأسفل لفتح التطبيق.",
    )


telegram_app.add_handler(CommandHandler("start", start))


@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"


@app.route("/webhook", methods=["POST"])
async def webhook():

    data = request.get_json(force=True)

    update = Update.de_json(data, telegram_app.bot)

    await telegram_app.process_update(update)

    return "OK"


if __name__ == "__main__":

    import asyncio

    async def main():

        await telegram_app.initialize()
        await telegram_app.start()

        print("Bot started")

        while True:
            await asyncio.sleep(3600)

    asyncio.run(main())# exchange-referrals
