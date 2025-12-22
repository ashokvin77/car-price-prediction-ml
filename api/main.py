from fastapi import FastAPI, Query
from typing import Literal
import joblib
import pandas as pd

# Load model
model = joblib.load("lightgbm_car_price.joblib")
categorical_cols = ['VehicleType', 'Gearbox', 'Model', 'FuelType', 'Brand', 'NotRepaired']

app = FastAPI(title="Car Price Prediction API")


@app.get("/")
def home():
    return {"message": "Car Price Prediction API is running!"}


@app.post("/predict")
def predict(
    VehicleType: Literal['bus', 'convertible', 'coupe', 'other', 'sedan', 'small', 'suv', 'wagon', 'unknown'] = Query(...),
    Gearbox: Literal['manual', 'auto', 'unknown'] = Query(...),
    Power: int = Query(..., ge=50, le=1000, description="Engine power in HP"),
    Model: str = Query(..., description="e.g., golf, 3er, passat, a4, corsa"),
    Mileage: int = Query(..., ge=5000, le=150000, description="Mileage in km"),
    FuelType: Literal['petrol', 'lpg', 'cng', 'hybrid', 'electric', 'other', 'unknown'] = Query(...),
    Brand: str = Query(..., description="e.g., volkswagen, bmw, audi, mercedes_benz, opel"),
    NotRepaired: Literal['yes', 'no', 'unknown'] = Query(...),
    Age: int = Query(..., ge=0, le=60, description="Car age in years")
):
    data = pd.DataFrame([{
        'VehicleType': VehicleType,
        'Gearbox': Gearbox,
        'Power': Power,
        'Model': Model,
        'Mileage': Mileage,
        'FuelType': FuelType,
        'Brand': Brand,
        'NotRepaired': NotRepaired,
        'Age': Age
    }])
    
    for col in categorical_cols:
        data[col] = data[col].astype('category')
    
    predicted_price = model.predict(data)[0]
    predicted_price = max(0, predicted_price)  # No negative prices
    
    return {"predicted_price_euros": round(predicted_price, 2)}
