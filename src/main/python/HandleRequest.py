import tempfile
import logging
import os

from telegram import Update
from telegram.error import BadRequest
from telegram.ext import ContextTypes
from VideoMaker import make_circle_video

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        video_file = await update.message.video.get_file()
    except BadRequest as e:
        logger.error(f"Ошибка при вызове метода get_file: {e}")
        await update.message.reply_text(
            "Я получил от тебя слишком тяжелое видео. Постарайся сжать его до 20МБ"
        )
        return

    await update.message.reply_text("Твое видео я получил, осталось немного подождать и все будет")
    tmp_dir = tempfile.gettempdir()
    input_path = os.path.join(tmp_dir, f"{video_file.file_unique_id}.mp4")
    output_path = os.path.join(tmp_dir, f"circle_{video_file.file_unique_id}.mp4")

    await video_file.download_to_drive(input_path)
    logger.info(f"Видео скачано: {input_path}")

    make_circle_video(input_path, output_path)
    await update.message.reply_video_note(video_note=open(output_path, 'rb'),
                                          duration=60)
    await update.message.reply_text("Держи видос")

    for path in [input_path, output_path]:
        if os.path.exists(path):
            os.remove(path)
            logger.info("Удален временный файл из: " + path)