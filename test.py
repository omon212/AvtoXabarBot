from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.messages import SendMessageRequest
import logging
from config import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

client = TelegramClient('anon', API_ID, API_HASH)
client.start()


async def get_specific_group(user_id, group_name):
    async for dialog in client.iter_dialogs():
        if dialog.is_group and dialog.entity.title == group_name:
            participants = await client(GetParticipantsRequest(
                channel=dialog.entity,
                filter=ChannelParticipantsSearch(''),
                offset=0,
                limit=1,
                hash=0
            ))
            for participant in participants.participants:
                if participant.user_id == user_id:
                    return dialog.entity
    return None


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    group_name = "LEADER BRAINS"
    group = await get_specific_group(user_id, group_name)

    if group:
        await message.reply(f"Siz '{group_name}' guruhiga qo'shilgansiz va unga salom yuborildi.",
                            parse_mode=ParseMode.MARKDOWN)
        await client(SendMessageRequest(
            peer=group,
            message="Salom"
        ))
    else:
        await message.reply(f"Siz '{group_name}' guruhiga qo'shilmagansiz.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
