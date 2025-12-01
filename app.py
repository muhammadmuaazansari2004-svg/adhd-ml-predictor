import os
import pickle
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="AI ADHD Predictor", layout="wide")

st.title("🧠 AI ADHD Predictor — clean & ready for GitHub")
st.write("Minimal code, same preprocessing as the notebook. Keep your model and pickles outside Git or use LFS.")

# --- required artifact paths ---
BASE = ""
P_COLUMNS = os.path.join("pickle", "columns.pkl")
P_ENCODED = os.path.join("pickle", "encoded_columns.pkl")
P_SCALER = os.path.join("pickle", "scaler.pkl")
MODEL_PATH = "model_base.h5"

required = [P_COLUMNS, P_ENCODED, P_SCALER, MODEL_PATH]
missing = [p for p in required if not os.path.exists(os.path.join(BASE, p)) and p != MODEL_PATH and not os.path.exists(os.path.join(BASE, MODEL_PATH))]
if missing:
    st.error("Missing required artifacts for prediction: %s" % ", ".join(missing))
    st.info("Place `columns.pkl`, `encoded_columns.pkl`, `scaler.pkl` in `pickle/` and the Keras model at `%s`." % MODEL_PATH)
    st.stop()

# Load persisted helpers (straightforward, fail fast)
with open(P_COLUMNS, "rb") as f:
    columns = list(pickle.load(f))
with open(P_ENCODED, "rb") as f:
    encoded_columns = list(pickle.load(f))
with open(P_SCALER, "rb") as f:
    scaler = pickle.load(f)

from tensorflow.keras.models import load_model
model = load_model(MODEL_PATH)

# --- UI (concise) ---
st.header("Inputs")
cols = st.columns([2, 1])
with cols[0]:
    age = st.slider("Age", 5, 80, 25)
    gender = st.selectbox("Gender", ["Male", "Female", "Nonbinary"])
    education_stage = st.selectbox("Education Stage", ["Child", "Teen", "Undergrad", "Adult"])
    inattention = st.slider("Inattention (0-10)", 0, 10, 3)
    hyperactivity = st.slider("Hyperactivity (0-10)", 0, 10, 3)
    impulsivity = st.slider("Impulsivity (0-10)", 0, 10, 3)
with cols[1]:
    sleep_hours = st.slider("Sleep hours", 3.0, 12.0, 7.0, 0.5)
    screen_time = st.slider("Screen time (hours/day)", 0.0, 18.0, 4.0, 0.5)
    medication = st.selectbox("Medication", ["No", "Stimulant", "Non-stimulant"]) 
    school_support = st.selectbox("School support", ["None", "IEP", "504", "Accommodations", "Therapy"]) 
    family_history = st.selectbox("Family history of ADHD?", ["No", "Yes"]) 
    daydreaming = st.selectbox("Daydreaming?", ["No", "Yes"]) 
    rsd = st.selectbox("RSD?", ["No", "Yes"]) 
    anxiety = st.selectbox("Comorbid anxiety?", ["No", "Yes"]) 
    depression = st.selectbox("Comorbid depression?", ["No", "Yes"]) 

# Map inputs to the training columns
yesno = lambda v: 1 if v == "Yes" else 0
input_map = {
    "Age": age,
    "Gender": gender,
    "EducationStage": education_stage,
    "InattentionScore": inattention,
    "HyperactivityScore": hyperactivity,
    "ImpulsivityScore": impulsivity,
    "SymptomSum": inattention + hyperactivity + impulsivity,
    "Daydreaming": yesno(daydreaming),
    "RSD": yesno(rsd),
    "SleepHours": sleep_hours,
    "ScreenTimeHours": screen_time,
    "ComorbidAnxiety": yesno(anxiety),
    "ComorbidDepression": yesno(depression),
    "FamilyHistoryADHD": yesno(family_history),
    "Medication": medication,
    "SchoolSupport": school_support,
    "AcademicScore": 75.0,
}

# Build row with the training column order
row = [input_map.get(c, 0) for c in columns]
df = pd.DataFrame([row], columns=columns)

# One-hot encode exactly the categorical columns used in training
categoricals = ["Gender", "EducationStage", "Medication", "SchoolSupport"]
encoded = pd.get_dummies(df, columns=categoricals, drop_first=True)
encoded = encoded.reindex(columns=encoded_columns, fill_value=0).astype(float)

# Scale and predict
X = scaler.transform(encoded)
prob = float(model.predict(X, verbose=0)[0][0])
label = "Likely ADHD" if prob > 0.5 else "Unlikely ADHD"

st.markdown("---")
st.metric(label="Prediction probability", value=f"{prob:.3f}")
st.subheader(label)
