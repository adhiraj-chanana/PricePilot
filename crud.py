from sqlalchemy.orm import Session
from database import Product
from sqlalchemy.orm import Session
from database import CompetitorPrice, Product

# Function to create a new product
def create_product(db: Session, name: str, category: str, current_price: float, demand: str):
    db_product = Product(name=name, category=category, current_price=current_price, demand=demand)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Function to get all products
def get_products(db: Session):
    return db.query(Product).all()

# Function to get a single product by ID
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()



# Function to store competitor price data
def store_competitor_price(db: Session, product_id: int, competitor_url: str, competitor_price: float):
    db_entry = CompetitorPrice(
        product_id=product_id,
        competitor_url=competitor_url,
        competitor_price=competitor_price
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

# Function to fetch competitor prices for a product
def get_competitor_prices(db: Session, product_id: int):
    return db.query(CompetitorPrice).filter(CompetitorPrice.product_id == product_id).all()

import requests
from bs4 import BeautifulSoup

def store_multiple_competitor_prices(db: Session, product_id: int, competitor_prices: list):
    """
    Stores multiple competitor prices in the database.
    """
    for price in competitor_prices:
        db_entry = CompetitorPrice(
            product_id=product_id,
            competitor_price=price
        )
        db.add(db_entry)

    db.commit()
    return {"message": f"Stored {len(competitor_prices)} competitor prices"}
