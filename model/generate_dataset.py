import pandas as pd
import random

# Define mappings
education_levels = {0: "School", 1: "Diploma", 2: "Undergraduate", 3: "Postgraduate"}
employment_status = {0: "Unemployed", 1: "Student", 2: "Employed", 3: "Self-employed"}
income_ranges = {0: "Below 1.5L", 1: "1.5L-3L", 2: "3L-6L", 3: "Above 6L"}
categories = {0: "General", 1: "OBC", 2: "SC", 3: "ST"}
schemes = ["PMKVY", "NSP Scholarship", "PMAY", "Ayushman Bharat", "Mudra Loan"]

# Number of rows to generate
num_rows = 1000

data = []

for _ in range(num_rows):
    age = random.randint(18, 60)
    education = random.randint(0, 3)
    employment = random.randint(0, 3)
    income = random.randint(0, 3)
    category = random.randint(0, 3)
    scheme_name = random.choice(schemes)

    # Simple eligibility logic (to make dataset realistic)
    if scheme_name == "PMKVY":
        eligible = 1 if (employment in [0,1] and 18 <= age <= 35) else 0
    elif scheme_name == "NSP Scholarship":
        eligible = 1 if (education in [1,2,3] and 18 <= age <= 25) else 0
    elif scheme_name == "PMAY":
        eligible = 1 if (income in [0,1] and 25 <= age <= 60) else 0
    elif scheme_name == "Ayushman Bharat":
        eligible = 1 if (income in [0,1] and age >= 18) else 0
    elif scheme_name == "Mudra Loan":
        eligible = 1 if (employment in [2,3] and 21 <= age <= 60) else 0
    else:
        eligible = 0

    data.append([age, education, employment, income, category, scheme_name, eligible])

# Create DataFrame
df = pd.DataFrame(data, columns=["age","education","employment","income","category","scheme_name","eligible"])

# Save CSV
df.to_csv("../data/schemes_dataset.csv", index=False, encoding='utf-8')

print("Dataset generated successfully! Rows:", len(df))
