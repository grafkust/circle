import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from HandleRequest import handle_video
from dotenv import load_dotenv

def main():
    load_dotenv()
    TOKEN = os.getenv("HTTP_TOKEN")

    if not TOKEN:
        raise RuntimeError("TOKEN не найден в .env")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.VIDEO, handle_video))

    print("Бот запущен. Нажми Ctrl+C для остановки.")
    app.run_polling()

if __name__ == "__main__":
    main()
