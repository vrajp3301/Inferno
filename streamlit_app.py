import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Inferno")

st.title("Inferno")

st.write("A retirement savings calculator web app to help users plan their financial future.")

initial_investment = st.number_input("Initial Investment", min_value=0.0, step=1000.0)
annual_return = st.number_input("Annual Return (%)", min_value=0.0, max_value=100.0, step=0.1)
withdrawal_rate = st.number_input("Withdrawal Rate (%)", min_value=0.0, max_value=100.0, step=0.1)
retirement_years = st.number_input("Retirement Years", min_value=1, step=1)

results = pd.DataFrame({
    "Initial Investment": [initial_investment],
    "Annual Return (%)": [annual_return],
    "Withdrawal Rate (%)": [withdrawal_rate],
    "Retirement Years": [retirement_years],
    "Success Rate (%)": [np.random.randint(50, 100)]
})

st.write(results)