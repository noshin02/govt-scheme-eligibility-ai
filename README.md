# 🎯 Government Scheme Eligibility Predictor (AI)

This project is an AI-powered system that predicts the eligibility of users for various Indian government schemes based on their personal and socio-economic details.

The project was developed as part of a **virtual internship** and focuses on building a simple yet meaningful end-to-end machine learning application with a frontend and backend.

---

## 🚀 Features
- Machine Learning–based eligibility prediction
- Uses a trained Random Forest classifier
- Clean and interactive frontend built with Streamlit
- Displays eligibility probability for each scheme
- Simple, student-friendly implementation

---

## 🧠 Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

---

## 📂 Project Structure
govt_scheme_ai/
├── app.py
├── data/
│ └── schemes_dataset.csv
├── model/
│ ├── eligibility_model.pkl
│ └── scheme_encoder.pkl
├── requirements.txt
└── README.md


---

## 📊 Input Parameters
- Age
- Education Level
- Employment Status
- Annual Income
- Category (General / OBC / SC / ST)

---

## 🧪 Output
The system predicts the **probability of eligibility** for each government scheme and displays them in descending order.

---

## 🏁 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
