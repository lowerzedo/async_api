from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import TIMESTAMP

Base = declarative_base()


class Sale(Base):
    __tablename__ = 'sales'

    incomeID = Column(Integer, primary_key=True)
    date = Column(TIMESTAMP)
    lastChangeDate = Column(TIMESTAMP)
    warehouseName = Column(String)
    countryName = Column(String)
    oblastOkrugName = Column(String)
    regionName = Column(String)
    supplierArticle = Column(String)
    nmId = Column(Integer)
    barcode = Column(String)
    category = Column(String)
    subject = Column(String)
    brand = Column(String)
    techSize = Column(String)
    isSupply = Column(Boolean)
    isRealization = Column(Boolean)
    totalPrice = Column(Float)
    discountPercent = Column(Integer)
    spp = Column(Integer)
    paymentSaleAmount = Column(Float)
    forPay = Column(Float)
    finishedPrice = Column(Float)
    priceWithDisc = Column(Float)
    saleID = Column(String)
    orderType = Column(String)
    sticker = Column(String)
    gNumber = Column(String)
    odid = Column(BigInteger)
    srid = Column(String)
