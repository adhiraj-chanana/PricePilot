from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, Product
from database import CompetitorPrice 
import crud
import scraper
import ml_model

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)




# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add a new product
@app.post("/products/")
def add_product(name: str, category: str, current_price: float, demand: str, db: Session = Depends(get_db)):
    return crud.create_product(db, name, category, current_price, demand)

# Get all products
@app.get("/products/")
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

# Get a single product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if product:
        return product
    return {"error": "Product not found"}


@app.get("/competitor-price/")
def competitor_price(url: str):
    return scraper.get_competitor_price(url)


# Store a competitor price for a product
@app.post("/competitor-price/")
def add_competitor_price(product_id: int, competitor_url: str, competitor_price: float, db: Session = Depends(get_db)):
    return crud.store_competitor_price(db, product_id, competitor_url, competitor_price)

# Get competitor prices for a product
@app.get("/competitor-price/{product_id}")
def get_competitor_price(product_id: int, db: Session = Depends(get_db)):
    return crud.get_competitor_prices(db, product_id)

@app.get("/fetch-competitor-prices/")
def fetch_competitor_prices(product_id: int, db: Session = Depends(get_db)):
    """
    Fetches multiple competitor prices from eBay and stores them in the database.
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return {"error": "Product not found"}

    # Fetch competitor prices
    competitor_prices = scraper.search_competitors(product.name)

    if not competitor_prices or "error" in competitor_prices:
        return {"error": "Could not find competitor prices"}

    # Store in database
    return crud.store_multiple_competitor_prices(db, product_id, competitor_prices)

@app.get("/optimized-price/")
def get_optimized_price(product_id: int, db: Session = Depends(get_db)):
    """
    Uses ML to recommend the best price for a product.
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return {"error": "Product not found"}

    competitor_entries = db.query(CompetitorPrice).filter(CompetitorPrice.product_id == product_id).all()

    competitor_prices = [c.competitor_price for c in competitor_entries]

    return ml_model.predict_price(product.current_price, competitor_prices, product.demand)
