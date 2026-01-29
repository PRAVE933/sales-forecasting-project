# 📊 Sales Forecasting Project

This project predicts future sales using historical sales data with a time-series forecasting approach.


## 🎯 Project Goal
To forecast future sales based on past sales data and visualize the comparison between actual and predicted sales.

## 📁 Dataset
**Store Item Demand Forecasting Dataset**  
Source: Kaggle  
The dataset contains daily sales data for multiple stores and items.

**Columns:**
- `date` – Date of sale  
- `store` – Store ID  
- `item` – Item ID  
- `sales` – Number of items sold  


## 🧠 Model Used
**ARIMA (AutoRegressive Integrated Moving Average)**  
ARIMA is a popular time-series forecasting model that captures trends and patterns from historical data.

---

## 🛠️ Tools & Technologies
- Python 3
- Pandas
- Matplotlib
- Statsmodels
- VS Code

## 📊 Project Workflow
1. Load the dataset
2. Filter data for one store and one item
3. Convert date column to datetime format
4. Visualize historical sales
5. Train ARIMA model
6. Forecast future sales
7. Visualize past vs future sales with color differentiation


## 📈 Output
- Blue line: Historical sales
- Red dashed line: Forecasted future sales


## ▶️ How to Run the Project
1. Clone or download this repository
2. Place `train.csv` in the project folder
3. Run the file:
   ```bash
   python main.py
