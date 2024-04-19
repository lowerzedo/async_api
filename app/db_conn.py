from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from dotenv import load_dotenv
import os
from helpers import parse_datetime

# from income_model import *
from models.order import *
from models.sale import *

load_dotenv() 

DATABASE_URL = os.getenv("DB_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def save_data(session, data, model):
    for item in data:
        if 'date' in item and isinstance(item['date'], str):
            item['date'] = parse_datetime(item['date'])
        if 'lastChangeDate' in item and isinstance(item['lastChangeDate'], str):
            item['lastChangeDate'] = parse_datetime(item['lastChangeDate'])
        if 'cancel_dt' in item and isinstance(item['cancel_dt'], str):
            item['cancel_dt'] = parse_datetime(item['cancel_dt'])
        
        stmt = select(model).where(model.incomeID == item['incomeID'])
        result = await session.execute(stmt)
        existing_record = result.scalar()

        if existing_record:
            # Update existing record
            for key, value in item.items():
                setattr(existing_record, key, value)
        else:
            # Insert new record
            record = model(**item)
            session.add(record)
    await session.commit()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
