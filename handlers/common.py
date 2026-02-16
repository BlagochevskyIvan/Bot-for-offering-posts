from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
)

from config.states import MAINMENU


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    telegram_user = update.effective_user

    await context.bot.send_message(
        chat_id=telegram_user.id,
        text="Предложка канала.\nНапиши пост и я отправлю его на модерацию"
        )
    return MAINMENU