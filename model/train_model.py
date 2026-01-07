import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("../data/schemes_dataset.csv")

# Features and target (MATCHING YOUR CSV)
X = df[["age", "education", "employment", "income", "category"]]
y = df["scheme_name"]

# Encode target labels
scheme_encoder = LabelEncoder()
y_encoded = scheme_encoder.fit_transform(y)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y_encoded)

# Save model
with open("eligibility_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save encoder
with open("scheme_encoder.pkl", "wb") as f:
    pickle.dump(scheme_encoder, f)

print("✅ Model and encoder trained & saved successfully")
