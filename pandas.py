import pandas as pd
from functools import reduce

data = {
    "Name": ["Amit", "Riya", "John", "Sneha", "Karan"],
    "Age": [25, 19, 35, 28, 42],
    "Income": [30000, 18000, 50000, 27000, 60000],
    "Credit_Score": [700, 620, 750, 680, 710],
    "Existing_Loan": [5000, 3000, 10000, 8000, 15000]
}

df = pd.DataFrame(data)

df["Credit_Status"] = list(map(lambda x: "Good" if x >= 650 else "Poor", df["Credit_Score"]))

eligible_age = list(filter(lambda x: x >= 21, df["Age"]))

total_loan = reduce(lambda x, y: x + y, df["Existing_Loan"])

def loan_eligibility(row):
    if (
        row["Age"] >= 21 and
        row["Income"] >= 25000 and
        row["Credit_Score"] >= 650 and
        row["Existing_Loan"] <= 0.4 * row["Income"]
    ):
        return "Eligible"
    else:
        return "Not Eligible"

df["Loan_Status"] = df.apply(loan_eligibility, axis=1)

print("\n--- Bank Loan Eligibility Report ---\n")
print(df)

print("\nEligible Ages (filter):", eligible_age)
print("Total Existing Loan (reduce):", total_loan)
