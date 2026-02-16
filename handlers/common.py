from telegram import (
    Update,
)
from telegram.ext import (
    ContextTypes,
)

from db.user_crud import get_user, create_user
from config.states import MAINMENU


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = await get_user(telegram_id=update.effective_user.id)
    if not user:
        user = await create_user(update.effective_user.id, update.effective_user.username)
    telegram_user = update.effective_user
    

    await context.bot.send_message(
        chat_id=telegram_user.id,
        text="Тестовый бот"
        )
    return MAINMENU