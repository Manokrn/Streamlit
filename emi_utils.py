import pandas as pd

def calculate_emi(principal, annual_rate, tenure_years):
    monthly_rate = annual_rate / 12 / 100
    months = tenure_years * 12
    if monthly_rate == 0:
        emi = principal / months
    else:
        emi = principal * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
    total_payment = emi * months
    total_interest = total_payment - principal
    return round(emi, 2), round(total_payment, 2), round(total_interest, 2)

def generate_amortization_schedule(principal, annual_rate, tenure_years):
    emi, total_payment, total_interest = calculate_emi(principal, annual_rate, tenure_years)
    monthly_rate = annual_rate / 12 / 100
    months = tenure_years * 12
    balance = principal
    schedule = []

    for month in range(1, months + 1):
        interest = balance * monthly_rate
        principal_paid = emi - interest
        balance -= principal_paid

        if balance < 0:
            principal_paid += balance
            balance = 0

        schedule.append({
            "Month": month,
            "EMI (₹)": round(emi, 2),
            "Principal Paid (₹)": round(principal_paid, 2),
            "Interest Paid (₹)": round(interest, 2),
            "Balance (₹)": round(balance, 2)
        })

    return pd.DataFrame(schedule)
