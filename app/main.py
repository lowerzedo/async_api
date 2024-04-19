import aiohttp
import asyncio
from datetime import datetime, timedelta
from db_conn import save_data, Order, Sale 
from dotenv import load_dotenv
from db_conn import *
from dummy_data import *
import json
from excel_generator import create_excel
from tg_bot import *

load_dotenv()

# Constants
API_KEY = os.getenv("WB_API_KEY")
HEADERS = {
    'Authorization': f'Bearer {API_KEY}'
}
BASE_URL = 'https://suppliers-stats.wildberries.ru/api/v1/supplier'

async def fetch_data(endpoint):
    #! To test without WB API keys by using dummy data from dummy_data folder
    # if endpoint == 'orders':
    #     orders = open("dummy_data/orders.json")
    #     orders_data = json.load(orders)
    #     return orders_data
    # else:
    #     sales = open("dummy_data/sales.json")
    #     sales_data = json.load(sales)
    #     return sales_data
    
    #! To use with WB API keys | Haven't tested since don't have API Keys
    url = f"{BASE_URL}/{endpoint}"
    now = datetime.utcnow()
    date_from = (now - timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
    date_to = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    params = {
        'dateFrom': date_from,
        'dateTo': date_to,
        'flag': '0'  
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS, params=params) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                print(f"Failed to fetch data from {endpoint}: {response.status}")
                return None

async def save_fetched_data(model, data):
    # Use async_session to create a context-managed session
    async with async_session() as session:
        if data:
            await save_data(session, data, model)
        else:
            print("No data to save")


async def scheduler():
    while True:
        orders_data = await fetch_data('orders')
        sales_data = await fetch_data('sales')
        await save_fetched_data(Order, orders_data)
        print("saved orders")
        await save_fetched_data(Sale, sales_data)
        print("saved sales")

        create_excel(orders_data, sales_data)
        # send_report()

        await asyncio.sleep(1800)  # Wait for 30 minutes


    
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await message.reply("Welcome! How can I help you today?")

def start_bot():
    executor.start_polling(dp, skip_updates=True)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # Schedule other tasks
    loop.create_task(scheduler())
    loop.create_task(start_bot())
    loop.run_forever()