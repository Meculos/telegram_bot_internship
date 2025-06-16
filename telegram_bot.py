import os
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from asgiref.sync import sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intern_project.settings')
django.setup()

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

from telegram_bot_app.models import TelegramUsername

@sync_to_async
def save_user(telegram_id, telegram_username):
    TelegramUsername.objects.get_or_create(
        telegram_id=telegram_id,
        telegram_username=telegram_username
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username or "NoUsername"
    user_id = user.id

    await save_user(user_id, username)

    await context.bot.send_message(chat_id=user_id, text=f"Hi {username}, you've been registered!")

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    run_bot()
