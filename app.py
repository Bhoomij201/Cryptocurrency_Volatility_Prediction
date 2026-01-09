import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("models/volatility_xgboost_model.pkl")

st.set_page_config(page_title="Crypto Volatility Predictor", layout="centered")

st.title("📈 Cryptocurrency Volatility Predictor")
st.write("Enter the market values below to predict volatility")

st.divider()

# ---- INPUT FIELDS ----
open_price = st.number_input("Open Price", min_value=0.0, value=100.0)
high_price = st.number_input("High Price", min_value=0.0, value=105.0)
low_price = st.number_input("Low Price", min_value=0.0, value=95.0)
close_price = st.number_input("Close Price", min_value=0.0, value=102.0)

volume = st.number_input("Trading Volume", min_value=0.0, value=1_000_000.0)
market_cap = st.number_input("Market Capitalization", min_value=0.0, value=10_000_000_000.0)

close_lag_1 = st.number_input("Close Price (1 Day Ago)", min_value=0.0, value=101.0)
close_lag_7 = st.number_input("Close Price (7 Days Ago)", min_value=0.0, value=98.0)

vol_lag_1 = st.number_input("Volatility (Previous Day)", min_value=0.0, value=0.02)
volatility_14d = st.number_input("14-Day Volatility", min_value=0.0, value=0.03)

ma_7 = st.number_input("7-Day Moving Average", min_value=0.0, value=100.0)

bb_middle = st.number_input("Bollinger Band Middle", min_value=0.0, value=100.0)
bb_upper = st.number_input("Bollinger Band Upper", min_value=0.0, value=110.0)
bb_lower = st.number_input("Bollinger Band Lower", min_value=0.0, value=90.0)

hl_range = st.number_input("High–Low Range Ratio", min_value=0.0, value=0.10)
oc_change = st.number_input("Open–Close Change Ratio", value=0.02)
liquidity_ratio = st.number_input("Liquidity Ratio (Volume / Market Cap)", value=0.0001)

st.divider()

# ---- PREDICTION ----
if st.button("🔮 Predict Volatility"):
    input_data = np.array([[
        open_price, high_price, low_price, close_price,
        volume, market_cap,
        close_lag_1, close_lag_7,
        vol_lag_1, volatility_14d,
        ma_7,
        bb_middle, bb_upper, bb_lower,
        hl_range, oc_change, liquidity_ratio
    ]])

    prediction = model.predict(input_data)[0]

    st.success(f"📊 Predicted Volatility: **{prediction:.4f}**")

    st.divider()

    # ---- EXPLANATION SECTION ----
    st.subheader("📘 What does this volatility value mean?")

    st.write("""
    Volatility represents the **expected percentage fluctuation in price** over a short period of time.
    It is calculated using **log-return based historical price movements**, which is a standard financial approach.
    """)

    st.write(f"""
    - A volatility value of **{prediction:.4f}** means the cryptocurrency price is expected to move
      approximately **±{prediction*100:.2f}%** in the near term.
    - This does **not** indicate price direction (up or down), only the **risk level**.
    """)

    # ---- RISK INTERPRETATION ----
    st.subheader("⚠️ Risk Interpretation")

    if prediction < 0.03:
        st.info("""
        🔵 **Low Volatility (Stable Market)**  
        Price movements are relatively small.  
        Suitable for **long-term investors** and **low-risk strategies**.
        """)
    elif prediction < 0.07:
        st.warning("""
        🟡 **Moderate Volatility (Normal Market Fluctuation)**  
        Prices may change noticeably.  
        Suitable for **swing trading** and **active monitoring**.
        """)
    else:
        st.error("""
        🔴 **High Volatility (Unstable Market)**  
        Large price swings expected.  
        High risk – suitable only for **experienced traders**.
        """)

    st.subheader("📌 Why does the value look small?")
    st.write("""
    Volatility values are expressed as **decimal percentages**, not raw prices.
    For example:
    - `0.02` = 2% price fluctuation  
    - `0.05` = 5% price fluctuation  

    In financial markets, even a **2–3% daily move is considered significant**.
    """)

    st.subheader("🧠 How should traders use this?")
    st.write("""
    - **Low volatility** → safer, stable conditions  
    - **High volatility** → higher risk, potential for rapid gains or losses  
    - Institutions and traders use volatility to manage **risk, position sizing, and hedging**
    """)
