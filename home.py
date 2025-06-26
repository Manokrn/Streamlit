import streamlit as st
import matplotlib.pyplot as plt
from emi_utils import calculate_emi, generate_amortization_schedule  # ✅ Imported here

# Streamlit app setup
st.set_page_config(page_title="Home Loan EMI Calculator", layout="centered")
st.title("🏡 Home Loan EMI Calculator")

st.sidebar.header("Enter Loan Details")

principal = st.sidebar.number_input("Loan Amount (₹)", value=500000, min_value=100000,max_value=10000000)
rate = st.sidebar.slider("Interest Rate (% per annum)", min_value=1.0, max_value=20.0, value=8.5)
tenure = st.sidebar.slider("Loan Tenure (Years)", min_value=1, max_value=30, value=20)

emi, total_payment, total_interest = calculate_emi(principal, rate, tenure)

st.subheader("Loan Summary")
st.markdown(f"**EMI:** ₹{emi:,.2f} per month")
st.markdown(f"**Total Interest:** ₹{total_interest:,.2f}")
st.markdown(f"**Total Payment:** ₹{total_payment:,.2f}")

# Pie chart
labels = ['Principal Amount', 'Total Interest']
values = [principal, total_interest]
colors = ['#6fa8dc', '#f4b183']
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Amortization table
with st.expander("📋 Show Amortization Schedule"):
    schedule_df = generate_amortization_schedule(principal, rate, tenure)
    st.dataframe(schedule_df, use_container_width=True)
