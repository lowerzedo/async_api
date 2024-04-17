import aiohttp
import asyncio
from datetime import datetime, timedelta
from db_conn import save_data, Order, Sale 
from dotenv import load_dotenv
from db_conn import *

load_dotenv()


# Constants
API_KEY = os.getenv("WB_API_KEY")
HEADERS = {
    'Authorization': f'Bearer {API_KEY}'
}
BASE_URL = 'https://suppliers-stats.wildberries.ru/api/v1/supplier'

async def fetch_data(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    now = datetime.utcnow()
    date_from = (now - timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
    date_to = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    params = {
        'dateFrom': date_from,
        'dateTo': date_to,
        'flag': '0'  # Ensure this flag is correct as per API documentation
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
    async with engine:  
        if data:
            await save_data(engine, data, model)
        else:
            print("No data to save")

async def scheduler():
    while True:
        orders_data = await fetch_data('orders')
        sales_data = await fetch_data('sales')
        await save_fetched_data(Order, orders_data)
        await save_fetched_data(Sale, sales_data)
        await asyncio.sleep(1800)  # Wait for 30 minutes

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scheduler())
