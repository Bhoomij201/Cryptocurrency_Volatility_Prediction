# Cryptocurrency Volatility Prediction 📈

## 📌 Project Overview
Cryptocurrency markets are highly volatile, making risk assessment and decision-making challenging for traders and investors.  
This project focuses on **predicting cryptocurrency market volatility** using historical price data, liquidity indicators, and machine learning models.

The objective is to **anticipate periods of high or low volatility** so that stakeholders can manage risk, optimize portfolio allocation, and design better trading strategies.

---

## 🎯 Objectives
- Analyze historical cryptocurrency market data
- Engineer meaningful time-series and volatility-based features
- Train machine learning models to predict future volatility
- Compare multiple models and select the best-performing one
- Deploy the trained model using a simple web interface

---

## 📊 Dataset Description
- **Type:** Historical daily cryptocurrency data  
- **Coverage:** 50+ cryptocurrencies  
- **Features include:**
  - Open price
  - High price
  - Low price
  - Close price
  - Trading volume
  - Market capitalization
  - Timestamp and date

---

## 🧹 Data Preprocessing
The following preprocessing steps were applied:

- Handling missing values and inconsistent records
- Removing infinite values caused by liquidity calculations
- Time-based sorting to preserve temporal order
- Train–test split based on time (not random split)
- Feature scaling and numerical stability checks

---

## 🛠️ Feature Engineering
To improve model performance, several advanced features were engineered:

- **Lag Features**
  - Close price (1-day lag, 7-day lag)
  - Volatility lag

- **Rolling Statistics**
  - 7-day moving average
  - 7-day and 14-day rolling volatility

- **Technical Indicators**
  - Bollinger Bands (Upper, Middle, Lower)
  - High–Low range ratio
  - Open–Close change ratio

- **Liquidity Indicator**
  - Liquidity ratio (Volume / Market Capitalization)

🎯 **Target Variable:**  
- `volatility_7d` (7-day rolling volatility)

---

## 📈 Exploratory Data Analysis (EDA)
EDA was performed to understand:
- Price trends across cryptocurrencies
- Correlation between OHLC prices
- Distribution of volatility values
- Relationship between liquidity and volatility

**Key Observations:**
- Strong correlation among Open, High, Low, and Close prices
- Large-cap cryptocurrencies show relatively lower volatility
- High volatility periods are less frequent but impactful

---

## 🤖 Model Selection & Training
The following models were trained and evaluated:

1. **Baseline Model**
   - Mean volatility prediction

2. **Random Forest Regressor**
   - Captures non-linear feature interactions

3. **XGBoost Regressor (Final Model)**
   - Handles complex patterns efficiently
   - Robust to feature interactions and non-linearity

---

## 📊 Model Evaluation
Models were evaluated using standard regression metrics:

- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

**Result:**  
✅ **XGBoost achieved the best overall performance** and was selected as the final model.

---

## 🖥️ Deployment
The trained model was deployed locally using **Streamlit**, allowing users to:

- Enter market parameters individually
- Predict future volatility
- Understand volatility levels through clear explanations and risk categories

### ▶️ Run the App Locally
```bash
streamlit run app.py
