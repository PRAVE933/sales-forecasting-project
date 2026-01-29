# ======================================
# SALES FORECASTING USING ARIMA
# ======================================

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# --------------------------------------
# STEP 1: Load the dataset
# --------------------------------------
data = pd.read_csv("train.csv")
print(data.head())

# --------------------------------------
# STEP 2: Select one store and one item
# --------------------------------------
toy = data[(data['store'] == 1) & (data['item'] == 1)].copy()
print(toy.head())

# --------------------------------------
# STEP 3: Convert date column to datetime
# --------------------------------------
toy.loc[:, 'date'] = pd.to_datetime(toy['date'])

# --------------------------------------
# STEP 4: Plot historical sales
# --------------------------------------
plt.figure(figsize=(10, 4))
plt.plot(
    toy['date'].values,
    toy['sales'].values,
    color='blue',
    linewidth=1.5
)
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show(block=False)


# --------------------------------------
# STEP 5: Build ARIMA model
# --------------------------------------
sales_data = toy['sales'].values

model = ARIMA(sales_data, order=(5, 1, 0))
model_fit = model.fit()

# Forecast next 10 days
future_sales = model_fit.forecast(steps=10)

print("\nFuture Sales Prediction:")
print(future_sales)

# --------------------------------------
# STEP 6: Create future dates
# --------------------------------------
future_dates = pd.date_range(
    start=toy['date'].iloc[-1],
    periods=len(future_sales) + 1,
    freq='D'
)[1:]

# --------------------------------------
# STEP 7: ZOOMED PLOT with COLOR DIFFERENCE
# --------------------------------------
plt.figure(figsize=(10, 4))

# Past sales (BLUE)
plt.plot(
    toy['date'].values[-100:],
    toy['sales'].values[-100:],
    color='blue',
    linewidth=2,
    label="Past Sales"
)

# Future sales (RED DASHED)
plt.plot(
    future_dates.values,
    future_sales,
    color='red',
    linestyle='--',
    linewidth=2,
    marker='o',
    label="Future Sales"
)

plt.title("Sales Forecasting (Past vs Future)")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()
