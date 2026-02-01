# 🏎️ Used Car Price Prediction API

![Project Banner](https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-EC2-232F3E?style=flat&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![LightGBM](https://img.shields.io/badge/Model-LightGBM-FF7043?style=flat)](https://lightgbm.readthedocs.io/)

**An end-to-end machine learning project: from model training to cloud deployment.**

### 🚀 [**View Live API Documentation**](http://18.223.131.80:8000/docs)

</div>

---

## 📋 Overview

This project delivers a scalable machine learning solution for **Rusty Bargain**, a used car sales service. The primary business objective was to develop an algorithmic tool that allows users to instantly determine the market value of their vehicle.

By analyzing historical data—including technical specifications, trim versions, and pricing—I developed and deployed a model that optimizes for both **prediction accuracy (RMSE)** and **inference speed**, ensuring a seamless user experience in the final application.

---

## 🎯 Objectives

* **Data Engineering:** Perform robust exploratory data analysis (EDA), cleaning, and preprocessing of vehicle specifications.
* **Model Development:** Train and rigorously evaluate multiple regression algorithms (Linear, Tree-based, and Gradient Boosting).
* **Performance Optimization:** Tune hyperparameters to minimize Root Mean Squared Error (RMSE) while monitoring training and prediction latency.
* **Production Deployment:** Containerize the best-performing model (LightGBM) using Docker and deploy it as a REST API on AWS EC2.

---

## 💾 Data Description

The dataset (`car_data.csv`) comprises historical inventory data with the following key features:

| Feature Category | Features |
| :--- | :--- |
| **Vehicle Specs** | `VehicleType`, `Gearbox`, `Power` (hp), `Model`, `FuelType`, `Brand`, `Mileage` |
| **History & Condition** | `RegistrationYear`, `RegistrationMonth`, `NotRepaired`, `DateCrawled`, `LastSeen` |
| **Meta Data** | `DateCreated`, `NumberOfPictures`, `PostalCode` |
| **Target Variable** | **`Price`** (Value in Euros) |

---

## ⚙️ Modeling Approach

To ensure the most robust solution, I implemented a comparative analysis of five distinct algorithms:

1.  **Linear Regression:** Established a baseline for performance (Sanity Check).
2.  **Random Forest:** Utilized for its robustness; tuned `n_estimators` and `max_depth`.
3.  **LightGBM:** Chosen for efficiency; tuned `learning_rate` and `n_estimators`.
4.  **CatBoost:** Implemented for handling categorical features; tuned `depth` and `iterations`.
5.  **XGBoost:** Tested as a competitive gradient boosting alternative.

**Evaluation Metrics:**
* 📉 **RMSE (Euros):** Accuracy of price prediction.
* ⏱️ **Training Time:** Computational cost to train.
* ⚡ **Prediction Time:** Latency for the end-user (critical for app integration).

---

## 📊 Model Performance Summary

After rigorous testing, the models performed as follows:

| Model | RMSE (€) | Training Time (s) | Prediction Time (s) | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **LightGBM** | **1675** | **0.65** | **0.16** | **🏆 Champion** |
| **XGBoost** | 1727 | 2.55 | 0.17 | Runner Up |
| **CatBoost** | 1781 | 7.86 | **0.03** | Fastest Inference |
| **Random Forest**| 1959 | 188.32 | 0.64 | Resource Heavy |
| **Linear Reg.** | 2657 | 4.58 | 0.20 | Baseline |

### 💡 Key Insights
* **LightGBM** was selected as the production model. It achieved the **lowest RMSE (1675)** and the **fastest training time (0.65s)**, offering the perfect balance for an iterative development cycle.
* **CatBoost** offered the fastest inference speed (0.03s), making it a viable backup if real-time latency becomes the sole priority.
* **Linear Regression** confirmed the non-linearity of the data (RMSE 2657), validating the need for complex tree-based ensembles.

---

## ☁️ Deployment Architecture

The champion model (LightGBM) is wrapped in a **FastAPI** application, containerized with **Docker**, and hosted on an **AWS EC2** instance.

* **Live URL:** [http://18.223.131.80:8000/docs](http://18.223.131.80:8000/docs)

### API Usage Example

**Endpoint:** `POST /predict`

```bash
curl -X POST "[http://18.223.131.80:8000/predict?VehicleType=sedan&Gearbox=manual&Power=150&Model=golf&Mileage=100000&FuelType=petrol&Brand=volkswagen&NotRepaired=no&Age=5](http://18.223.131.80:8000/predict?VehicleType=sedan&Gearbox=manual&Power=150&Model=golf&Mileage=100000&FuelType=petrol&Brand=volkswagen&NotRepaired=no&Age=5)"
```

**JSON Response:**
```json
{
  "predicted_price_euros": 12410.39
}
```

---

## 🛠️ How to Run Locally

If you wish to run the API on your local machine:

```bash
# 1. Navigate to the API directory
cd api

# 2. Build the Docker image
docker build -t car-price-api .

# 3. Run the container
docker run -p 8000:8000 car-price-api

# 4. Access the Swagger UI
# Open http://localhost:8000/docs in your browser
```

---

## 📂 Project Structure

```text
├── car.ipynb                      # Jupyter Notebook for EDA, Training & Evaluation
├── car_data.csv                   # Historical Dataset
├── README.md                      # Project Documentation
├── api/
│   ├── main.py                    # FastAPI application entry point
│   ├── Dockerfile                 # Docker container configuration
│   ├── requirements.txt           # Python dependencies
│   └── lightgbm_car_price.joblib  # Serialized Champion Model
```

---

