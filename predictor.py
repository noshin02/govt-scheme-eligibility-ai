import joblib
import pandas as pd

# Load trained model and encoder
model = joblib.load("model/eligibility_model.pkl")
scheme_encoder = joblib.load("model/scheme_encoder.pkl")

# All schemes (same order as training)
schemes = ["PMKVY", "NSP Scholarship", "PMAY", "Ayushman Bharat", "Mudra Loan"]

def predict_schemes(user_profile):
    """
    user_profile: dict with keys
    age, education, employment, income, category
    """

    results = []

    for scheme in schemes:
        encoded_scheme = scheme_encoder.transform([scheme])[0]

        input_data = pd.DataFrame([{
            "age": user_profile["age"],
            "education": user_profile["education"],
            "employment": user_profile["employment"],
            "income": user_profile["income"],
            "category": user_profile["category"],
            "scheme_name": encoded_scheme
        }])

        probability = model.predict_proba(input_data)[0][1]

        results.append({
            "scheme": scheme,
            "eligibility_probability": round(probability * 100, 2)
        })

    # Sort by highest probability
    results = sorted(
        results,
        key=lambda x: x["eligibility_probability"],
        reverse=True
    )

    return results
