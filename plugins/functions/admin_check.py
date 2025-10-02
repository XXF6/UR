# plugins/functions/admin_check.py (مثلاً)
import logging
from pyrogram.types import Message
from pyrogram import Client


from plugins.config import Config

logger = logging.getLogger(__name__)

async def is_admin_check(client: Client, message: Message):
    user_id = message.from_user.id
    if user_id not in ADMIN_IDS:
        await message.reply_text(
            "🚫 **عذرًا هذا البوت تابع للزعيم للأفلام والمسلسلات لايمكن استخدامه الابإذنة  @X_XF8 .**",
            quote=True
        )
        logger.warning(f"Non-admin user {user_id} tried to access an admin-only command.")
        return False
    return True
