from sqlalchemy import Column, Integer, String, Float, DateTime, BigInteger, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import TIMESTAMP

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    incomeID = Column(Integer, primary_key=True)
    date = Column(TIMESTAMP)
    lastChangeDate = Column(TIMESTAMP)
    supplierArticle = Column(String)
    techSize = Column(String)
    barcode = Column(String)
    totalPrice = Column(Float)
    discountPercent = Column(Integer)
    warehouseName = Column(String)
    oblast = Column(String)
    odid = Column(BigInteger)
    nmId = Column(Integer)
    subject = Column(String)
    category = Column(String)
    brand = Column(String)
    isCancel = Column(Boolean)
    cancel_dt = Column(TIMESTAMP)
    gNumber = Column(String)
    sticker = Column(String)
    orderType = Column(String)
