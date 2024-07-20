from bot import dp, bot, FSMContext, defaultdict
from aiogram import types
from Keyboards.inline import *
from state import Admin
from databace import *
from config import ADMINS

fake_db = defaultdict(dict)


@dp.message_handler(commands="admin")
async def adminn(message: types.Message):
    user = str(message.from_user.id)
    if user in ADMINS:
        await message.answer("<b>Siz Adminsiz 👤</b>", reply_markup=admin_btn)
    else:
        print(False)


@dp.callback_query_handler(text='gruppa_qoshish')
async def grupaaqoshish(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("📤 Guruh ID raqamini kiriting", reply_markup=orqaga)
    await Admin.group_id.set()


@dp.message_handler(state=Admin.group_id)
async def group_namee(message: types.Message, state: FSMContext):
    groups = await get_group()
    print(groups)
    if groups == []:
        fake_db[message.chat.id]['group_id'] = message.text
        await message.answer("📤 Guruh nomini kiriting", reply_markup=orqaga)
        await Admin.group_name.set()
    else:
        for i in groups:
            if message.text in str(i[1]):
                await message.answer("Bu ID raqam mavjud ❌", reply_markup=admin_btn)
                await state.finish()
            else:
                fake_db[message.chat.id]['group_id'] = message.text
                await message.answer("📤 Guruh nomini kiriting", reply_markup=orqaga)
                await Admin.group_name.set()


@dp.message_handler(state=Admin.group_name)
async def groupnamee(message: types.Message, state: FSMContext):
    fake_db[message.chat.id]['group_name'] = message.text
    print(fake_db)
    await save_group_data(fake_db[message.chat.id]['group_id'], fake_db[message.chat.id]['group_name'])
    await message.answer("Guruh qo'shildi ✅", reply_markup=admin_btn)
    await state.finish()


@dp.callback_query_handler(text='gruppa_ochirish')
async def grupaochrsh(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("📤 Guruh ID raqamini kiriting", reply_markup=orqaga)
    await Admin.delete_id.set()


@dp.message_handler(state=Admin.delete_id)
async def group_id(message: types.Message, state: FSMContext):
    await delete_group(message.text)
    await message.answer("Guruh o'chirildi ✅", reply_markup=admin_btn)
    await state.finish()
