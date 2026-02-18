from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
)
from config.logger import logger
from config.states import GET_POST
from config.cp_config import ADMIN_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegram_user = update.effective_user

    await context.bot.send_message(
        chat_id=telegram_user.id,
        text="Предложка канала.\nНапиши пост и я отправлю его на модерацию"
        )
    return GET_POST

async def get_post(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    logger.info()
    await context.bot.send_message(
        chat_id=update.effective_user.id,
        text="Пост отправлен на модерацию админу"
        )
    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=message.photo,
        text=message.text
    )
    return GET_POST