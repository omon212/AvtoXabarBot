import logging, asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from Keyboards.inline import *
from state import Xabar
from collections import defaultdict
from databace import *

API_TOKEN = "7185696251:AAF7cdn3UtElCkxQ-KfvikNS5z3f9bi55jc"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

fake_db = defaultdict(dict)


@dp.message_handler(commands=['start'])
async def startt(message: types.Message):
    await message.answer(f"<b>Assalomu aleykum {message.from_user.full_name}</b> ", reply_markup=menu_btn)


@dp.callback_query_handler(text='xabar_jadvali')
async def xabar_jadvalii(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Assalomu aleykum</b>", reply_markup=xabar_reja)


@dp.callback_query_handler(text="xabar_rejalashtirish")
async def xabar_rejaa(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("📤 Xabar rejalashtirish\n\n<b>Xabaringizni kiriting</b>", reply_markup=orqaga)
    await Xabar.text.set()


@dp.message_handler(state=Xabar.text)
async def xabar_text(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    fake_db[user_id]['xabar_text'] = str(message.text)
    print(fake_db)
    await message.answer("""
📤 Xabar rejalashtirish

<b>Xabaringizni jo'natish uchun vaqtni kiriting:</b>     
    """, reply_markup=vaqt)
    await state.finish()
    await Xabar.vaqt.set()


@dp.callback_query_handler(state=Xabar.vaqt)
async def xabar_vaqt(call: types.CallbackQuery, state: FSMContext):
    vaqti = str(call.data)
    fake_db[call.message.chat.id]['xabar_vaqt'] = vaqti
    print(fake_db)
    await call.message.delete()
    await call.message.answer(f"""
📤 Xabar rejalashtirish 

Vaqt: <b>{vaqti} daqiqa</b> 
-------------   
Tasdiqlang:
    """, reply_markup=rejalashtirish)
    await state.finish()


@dp.callback_query_handler(text='tasdiqlash')
async def tasdiqlash(call: types.CallbackQuery):
    await call.message.delete()
    user_id = call.message.chat.id
    await call.message.answer("Xabaringiz rejalashtirildi ✅", reply_markup=menu_btn)
    await save_all_data(
        user_id,
        fake_db[call.message.chat.id]['xabar_text'],
        fake_db[call.message.chat.id]['xabar_vaqt']
    )


@dp.callback_query_handler(text="orqaga", state="*")
async def orqagaaa(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Assalomu Aleykum</b>", reply_markup=menu_btn)
    await state.finish()


# --------------Xabar yuborish--------------#
@dp.callback_query_handler(text='xabar_yuborish')
async def xabar_yuborishh(call: types.CallbackQuery):
    user_id = call.message.chat.id
    groups = await get_group()
    xabar = await get_xabar(user_id)
    await call.message.delete()
    await call.message.answer("Xabaringiz muvofaqiyatli yuborilyapti ✅", reply_markup=menu_btn)

    while True:
        for i in groups:
            for d in xabar:
                if d[3] == '5':
                    print(5)
                    await call.bot.send_message(i[1], d[2])
                    await asyncio.sleep(300)
                elif d[3] == '10':
                    print(10)
                    await call.bot.send_message(i[1], d[2])
                    await asyncio.sleep(600)
                elif d[3] == '20':
                    print(20)
                    await call.bot.send_message(i[1], d[2])
                    await asyncio.sleep(1200)
                elif d[3] == '30':
                    print(30)
                    await call.bot.send_message(i[1], d[2])
                    await asyncio.sleep(1800)
                elif d[3] == '60':
                    print(60)
                    await call.bot.send_message(i[1], d[2])
                    await asyncio.sleep(3600)


#--------------Xabar qidirish--------------#




if __name__ == '__main__':
    from admin import dp
    executor.start_polling(dp, skip_updates=True)
