from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from models.model import channel

def forced_channel():
    channels = channel.get_datas()
    btn = InlineKeyboardMarkup(row_width=2)
    for num, kanal in enumerate(channels, 1):
        btn.add(InlineKeyboardButton(f"{num}-kanal", url=kanal[1]))
    btn.add(InlineKeyboardButton("Tekshirish ✅", callback_data="channel_check"))
    return btn
