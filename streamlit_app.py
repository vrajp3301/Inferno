import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def calculate_retirement_savings(current_age, retirement_age, current_savings, annual_contribution, annual_return, annual_inflation, adjust_for_inflation, tax_rate):
    years_to_retirement = retirement_age - current_age
    if adjust_for_inflation:
        future_value = current_savings * (1 + (annual_return - annual_inflation)/100)**years_to_retirement
        for _ in range(years_to_retirement):
            future_value += annual_contribution * (1 + (annual_return - annual_inflation)/100)**(years_to_retirement - 1)
            years_to_retirement -= 1
        future_value *= (1 - tax_rate/100)  # Apply tax rate
    else:
        future_value = current_savings * (1 + annual_return/100)**years_to_retirement
        for _ in range(years_to_retirement):
            future_value += annual_contribution * (1 + annual_return/100)**(years_to_retirement - 1)
            years_to_retirement -= 1
        future_value *= (1 - tax_rate/100) 
    return future_value

def main():
    st.set_page_config(page_title="Retirement Savings Calculator", page_icon=":chart_with_upwards_trend:")
    st.title("Retirement Savings Calculator")
    
    with st.expander("Retirement Savings Inputs"):
        current_age = st.number_input("Current Age", min_value=18, max_value=100, value=30, step=1)
        retirement_age = st.number_input("Desired Retirement Age", min_value=50, max_value=100, value=65, step=1)
        current_savings = st.number_input("Current Retirement Savings", min_value=0.0, value=50000.0, step=1000.0)
        annual_contribution = st.number_input("Annual Contribution", min_value=0.0, value=5000.0, step=1000.0)
        annual_return = st.number_input("Expected Annual Rate of Return (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.1)
        annual_inflation = st.number_input("Expected Annual Inflation Rate (%)", min_value=0.0, max_value=10.0, value=2.5, step=0.1)
        adjust_for_inflation = st.checkbox("Adjust for Inflation")
        tax_rate = st.number_input("Tax Rate (%)", min_value=0.0, max_value=50.0, value=15.0, step=0.1)
    
    if st.button("Calculate"):
        estimated_savings = calculate_retirement_savings(current_age, retirement_age, current_savings, annual_contribution, annual_return, annual_inflation, adjust_for_inflation, tax_rate)
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(["Estimated Retirement Savings"], [estimated_savings])
        ax.set_title("Retirement Savings Projection")
        ax.set_xlabel("Metric")
        ax.set_ylabel("Amount (USD)")
        formatter = ticker.FuncFormatter(lambda x, p: "${:,.2f}".format(x))
        ax.yaxis.set_major_formatter(formatter)
        
        st.pyplot(fig)
        st.write(f"Estimated Retirement Savings: **${estimated_savings:.2f}**")

if __name__ == "__main__":
    main()