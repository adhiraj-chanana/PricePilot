from sqlalchemy import create_engine, Column, Integer, Float, ForeignKey, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./pricepilot.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()

# Product Table
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    current_price = Column(Float)
    demand = Column(String)

# Updated Competitor Prices Table (Removing URL)
class CompetitorPrice(Base):
    __tablename__ = "competitor_prices"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))  # Link to our product
    competitor_price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
