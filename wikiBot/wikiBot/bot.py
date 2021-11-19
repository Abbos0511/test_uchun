import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2081721003:AAGtkO82xyTqUSzenik4KgpVTT8zfC_fAvw'

logging.basicConfig(level=logging.INFO)
wikipedia.set_lang('uz')

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def echoBot(message: types.Message):
    try:
        respond= wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu maqola topilmadi:')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)