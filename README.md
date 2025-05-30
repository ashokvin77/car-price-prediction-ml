# Used Car Price Prediction

## Overview

This project focuses on developing an app for Rusty Bargain, a used car sales service. Their main goal is to attract customers by offering features like instantly determining the market value of used cars. They aim to achieve this by building models based on historical data, including technical specifications, trim versions, and prices. This project tests different models and evaluates their performance based on RMSE, training time, and prediction speed to identify the best model for the app.

---

## Objectives

- Perform exploratory data analysis and data preprocessing.
- Train and evaluate multiple models: Linear Regression (sanity check), Random Forest, LightGBM, CatBoost, and XGBoost, with hyperparameter tuning for tree-based models.
- Evaluate models based on prediction quality (RMSE), prediction speed, and training time.
Provide recommendations for Rusty Bargain's car valuation app.

---

## Data Description

The dataset `car_data.csv` includes the following features:

- **DateCrawled** — Date when the listing was crawled from the website.
- **VehicleType** — Type of the vehicle body (e.g., sedan, SUV, convertible).
- **RegistrationYear** — Year the vehicle was registered.
- **Gearbox** — Type of gearbox (e.g., manual, automatic).
- **Power** — Engine power in horsepower (hp).
- **Model** — Vehicle model name.
- **Mileage** — Mileage of the vehicle in kilometers.
- **RegistrationMonth** — Month the vehicle was registered.
- **FuelType** — Type of fuel used (e.g., gasoline, diesel, electric).
- **Brand** — Brand of the car (e.g., BMW, Audi).
- **NotRepaired** — Indicates whether the vehicle has been repaired (`yes`, `no`, or `unknown`).
- **DateCreated** — Date when the listing was created.
- **NumberOfPictures** — Number of pictures uploaded for the vehicle (typically 0).
- **PostalCode** — Postal code of the listing owner.
- **LastSeen** — Date when the user last interacted with the listing.
- **Price** *(Target)* — Listed price of the vehicle in Euros.

---

## Modeling Approach

- **Models Trained**:
  - **Linear Regression**:  
    Used as a **sanity check**, no hyperparameter tuning.
  - **Random Forest**:  
    Tuned key hyperparameters (e.g., `n_estimators`, `max_depth`).
  - **LightGBM**:  
    Tuned parameters such as `learning_rate` and `n_estimators`.
  - **CatBoost**:  
    Tuned parameters including `depth` and `iterations`.
  - **XGBoost**:  
    Tuned a few default parameters for quick comparison.

- **Evaluation Metrics**:
  - **RMSE (Euros)**: To evaluate prediction quality.
  - **Training Time (s)**: Time to train the model.
  - **Prediction Time (s)**: Time to make predictions.

---

## Model Performance Summary

| Model           | RMSE (Euros) | Training Time (s) | Prediction Time (s) |
|----------------|--------------|-------------------|----------------------|
| LinearRegression | 2657         | 4.58              | 0.20                 |
| RandomForest     | 1959         | 188.32            | 0.64                 |
| LightGBM         | 1675         | 0.65              | 0.16                 |
| CatBoost         | 1781         | 7.86              | 0.03                 |
| XGBoost          | 1727         | 2.55              | 0.17                 |

---

## Key Insights

- **Linear Regression** served as an effective **sanity check** with an RMSE of **2657 euros**, confirming that more complex models provided substantial improvements.
- **Random Forest** improved performance significantly (**RMSE: 1959**) but had the **slowest training time** at **188.32 seconds**.
- **LightGBM** emerged as the **optimal choice** with the **lowest RMSE (1675 euros)** and **fastest training time** of just **0.65 seconds**.
- **CatBoost** demonstrated excellent performance (**RMSE: 1781**) and had the **fastest prediction time** of **0.03 seconds**.
- **XGBoost** provided strong results (**RMSE: 1727**) with a **balanced training time** of **2.55 seconds**, making it a competitive alternative.
- **Recommendation**: LightGBM is recommended for Rusty Bargain’s app due to its superior balance of prediction quality, training speed, and prediction speed.

---

## Tools and Technologies

- Python 3.12.10
- Pandas 2.2.3
- NumPy  2.2.5
- Scikit-learn 1.6.1
- LightGBM  4.6.0 
- CatBoost  1.2.8
- XGBoost   3.0.0

---



