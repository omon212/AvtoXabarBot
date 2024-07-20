from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✉️ Xabar yuborish", callback_data="xabar_yuborish"),
        ],
        [
            InlineKeyboardButton(text="📅 Xabarlar jadvali", callback_data="xabar_jadvali"),
        ],
        [
            InlineKeyboardButton(text="🔍 Xabar qidirish", callback_data="xabar_qidirish")
        ]
    ]
)

xabar_reja = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📤 Xabar rejalashtirish", callback_data="xabar_rejalashtirish")
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="orqaga")
        ]
    ]
)

orqaga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="orqaga")
        ]
    ]
)

vaqt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="5 daqiqa", callback_data="5"),
            InlineKeyboardButton(text="10 daqiqa", callback_data="10"),
            InlineKeyboardButton(text="20 daqiqa", callback_data="20")
        ],
        [
            InlineKeyboardButton(text="30 daqiqa", callback_data="30"),
            InlineKeyboardButton(text="60 daqiqa", callback_data="60"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="orqaga")
        ]
    ]
)

rejalashtirish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✉️ Rejalashtirish", callback_data="tasdiqlash")
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="orqaga")
        ]
    ]
)

xabar_yuborish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Barcha guruhlarga yuborish", callback_data="barcha_guruhlarga_yuborish"),
        ],
        [
            InlineKeyboardButton(text="Tanlangan guruhlarga yuborish", callback_data="tanlangan_guruhlarga_yuborish"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="orqaga")
        ]
    ]
)

admin_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Gruppa qo'shish ➕", callback_data="gruppa_qoshish"),
        ],
        [
            InlineKeyboardButton(text="Gruppa o'chirish ➖", callback_data='gruppa_ochirish')
        ],
    ]
)
