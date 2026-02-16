from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

from config.states import MAIN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data.clear()
    context.chat_data.clear()

    chat_id = update.effective_chat.id

    await context.bot.send_message(
        chat_id=chat_id,
        text="Привет, это бот предложки\nНапиши сюда свой пост и мы отправим его на модерацию"
    )
    return MAIN