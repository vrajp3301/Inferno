import streamlit as st

def calculate_retirement_savings(current_age, retirement_age, current_savings, annual_contribution, annual_return):
    years_to_retirement = retirement_age - current_age
    future_value = current_savings * (1 + annual_return/100)**years_to_retirement
    for _ in range(years_to_retirement):
        future_value += annual_contribution * (1 + annual_return/100)**(years_to_retirement - 1)
        years_to_retirement -= 1
    return future_value

def main():
    st.title("Retirement Savings Calculator")
    st.set_page_config(page_title="Inferno - Retirement Savings Calculator", page_icon=":mortar_board:")
    current_age = st.number_input("Current Age", min_value=18, max_value=100, value=30, step=1)
    retirement_age = st.number_input("Desired Retirement Age", min_value=50, max_value=100, value=65, step=1)
    current_savings = st.number_input("Current Retirement Savings", min_value=0.0, value=50000.0, step=1000.0)
    annual_contribution = st.number_input("Annual Contribution", min_value=0.0, value=5000.0, step=1000.0)
    annual_return = st.number_input("Expected Annual Rate of Return (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.1)
    
    if st.button("Calculate"):
        estimated_savings = calculate_retirement_savings(current_age, retirement_age, current_savings, annual_contribution, annual_return)
        st.write(f"Estimated Retirement Savings: ${estimated_savings:.2f}")

if __name__ == "__main__":
    main()