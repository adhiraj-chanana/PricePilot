import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from database import SessionLocal, Product, CompetitorPrice

# Load data from database
def load_training_data():
    db = SessionLocal()
    products = db.query(Product).all()
    competitor_prices = db.query(CompetitorPrice).all()
    db.close()

    data = []

    # Map competitor prices to products
    competitor_map = {}
    for competitor in competitor_prices:
        if competitor.product_id not in competitor_map:
            competitor_map[competitor.product_id] = []
        competitor_map[competitor.product_id].append(competitor.competitor_price)

    for product in products:
        competitor_price_avg = np.mean(competitor_map.get(product.id, [product.current_price]))

        # Convert demand level into a numerical value
        demand_value = {"low": 0, "medium": 1, "high": 2}.get(product.demand, 1)

        data.append([product.current_price, competitor_price_avg, demand_value])

    return np.array(data)

# Train the Random Forest model
def train_model():
    data = load_training_data()

    if len(data) == 0:
        return None

    X = data[:, :3]  # Features: current_price, competitor_price_avg, demand_value
    y = data[:, 0]   # Target: optimized price

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model

# Predict optimized price using Random Forest
def predict_price(current_price, competitor_prices, demand):
    model = train_model()
    
    if model is None:
        return {"error": "Not enough data to train model"}

    competitor_price_avg = np.mean(competitor_prices) if competitor_prices else current_price
    demand_value = {"low": 0, "medium": 1, "high": 2}.get(demand, 1)

    optimized_price = model.predict([[current_price, competitor_price_avg, demand_value]])[0]

    return {"optimized_price": round(optimized_price, 2)}
