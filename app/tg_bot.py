from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime

TG_BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token='YOUR_TELEGRAM_BOT_TOKEN')
dp = Dispatcher(bot)

@dp.message_handler(commands=['report'])
async def send_report(message: types.Message):
    current_datetime = datetime.now()
    with open('report.xlsx', 'rb') as file:
        await message.answer_document(file, caption=f"The income report for {current_datetime}: is attached")

if __name__ == "__main__":
    executor.start_polling(dp)