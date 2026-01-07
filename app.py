import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model/eligibility_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/scheme_encoder.pkl", "rb") as f:
    scheme_encoder = pickle.load(f)


st.set_page_config(page_title="Govt Scheme AI", layout="centered")
st.title("🎯 Government Scheme Eligibility Predictor")
st.write("Enter your details to check eligible government schemes.")

# Input fields
age = st.slider("Age", 18, 60, 25)

education_map = {
    "School": 0,
    "Diploma": 1,
    "Undergraduate": 2,
    "Postgraduate": 3
}
employment_map = {
    "Unemployed": 0,
    "Student": 1,
    "Employed": 2,
    "Self-employed": 3
}
income_map = {
    "Below 1.5L": 0,
    "1.5L-3L": 1,
    "3L-6L": 2,
    "Above 6L": 3
}
category_map = {
    "General": 0,
    "OBC": 1,
    "SC": 2,
    "ST": 3
}

education = st.selectbox("Education Level", list(education_map.keys()))
employment = st.selectbox("Employment Status", list(employment_map.keys()))
income = st.selectbox("Annual Income", list(income_map.keys()))
category = st.selectbox("Category", list(category_map.keys()))

if st.button("Check Eligible Schemes"):
    input_data = np.array([[  
        age,
        education_map[education],
        employment_map[employment],
        income_map[income],
        category_map[category]
    ]])

    predictions = model.predict_proba(input_data)[0]

    # Decode scheme names
    schemes = scheme_encoder.inverse_transform(
        np.arange(len(predictions))
    )

    st.subheader("📌 Eligibility Results")

    for scheme, prob in zip(schemes, predictions):
        st.write(f"**{scheme}** → {round(prob * 100, 2)}% eligible")
