# 🧠 ADHD ML Predictor

Ever wondered if machine learning could help understand ADHD patterns? This project is exactly that—a clean, minimal ML app that predicts ADHD likelihood using a neural network trained on synthetic data. Built with care for folks who think differently. Not for medical diagnosis, but for learning and exploration.

## What's This About?

This repo combines three core ideas:
1. **Smart preprocessing** — turning messy behavioral data into something a neural network can actually learn from
2. **Clean code** — no bloat, no unnecessary complexity, just what you need
3. **Accessible UI** — a simple Streamlit app so anyone can run predictions without touching code

Think of it as a playground for understanding how ML models work with ADHD-related data patterns.

---

## 🚀 Quick Start (5 Minutes)

### Windows (PowerShell)

```powershell
# Clone the repo
git clone https://github.com/muhammadmuaazansari2004-svg/adhd-ml-predictor
cd adhd-ml-predictor

# Set up your environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements.txt
```

### Get Model & Preprocessing Files (Important!)

This repo uses **Git LFS** for large binary files. They're *not* in the repo by default—you need to pull them:

```powershell
# Install Git LFS (first time only)
git lfs install

# Pull the model and pickle files
git lfs pull
```

If you don't have Git LFS installed, visit [git-lfs.com](https://git-lfs.com) and grab it.

**What gets downloaded:**
- `model_base.h5` — trained neural network (~5-50MB depending on architecture)
- `pickle/columns.pkl` — feature column names
- `pickle/encoded_columns.pkl` — one-hot encoded columns
- `pickle/scaler.pkl` — data normalization

Once downloaded, run the app:

```powershell
streamlit run app.py
```

Open **http://localhost:8501** → you're predicting. 🎉

---

## 🎯 How It Actually Works

### Step 1: Collect Input
The UI asks for things like:
- Age, gender, education stage
- Symptom scores (inattention, hyperactivity, impulsivity)
- Behavioral flags (daydreaming, RSD, anxiety, depression)
- Medication & support type

### Step 2: Preprocess Like We Trained
Here's the secret sauce—we do *exactly* what we did during training:
1. **One-hot encode** categorical features (Gender, EducationStage, Medication, SchoolSupport) with `drop_first=True`
2. **Reindex** to match the training column order
3. **Scale** with StandardScaler (exact same fit from training)

This means predictions are reliable because the data goes through the same pipeline. No surprises.

### Step 3: Predict
The Keras model runs inference and spits out a probability (0.0 to 1.0).

### Step 4: Show Results
You get:
- **Probability score** — how confident the model is
- **Risk label** — "Likely ADHD" or "Unlikely ADHD" (threshold: 0.5)

---

## 📁 Project Structure

```
adhd-ml-predictor/
├── app.py                 # Streamlit app (the UI you see)
├── requirements.txt       # Python dependencies
├── setup_venv.ps1        # Windows environment setup (one-click)
├── README.md             # This file
├── LICENSE               # Project license
├── .gitignore            # Excludes large files from Git
│
├── pickle/               
│   ├── columns.pkl
│   ├── encoded_columns.pkl
│   └── scaler.pkl
│
└── model_base.h5         

**Why not commit the model & pickles?** They're heavy and binary. Use Git LFS or host them externally (Hugging Face, AWS S3, etc.).

---

## 🔧 Dependencies

All in `requirements.txt`:
- **numpy, pandas** — data handling
- **scikit-learn** — preprocessing (StandardScaler)
- **tensorflow** — Keras model inference
- **streamlit** — web UI
- **jupyter, ipykernel** — for local notebook work

One command installs them all:
```powershell
pip install -r requirements.txt
```

---

## 🌐 Deployment Ideas

### Streamlit Cloud (Easiest)
1. Push your repo to GitHub (no model/pickles)
2. Connect to Streamlit Cloud
3. Add a setup step that downloads the model at startup
4. Deploy one-click ✨

### Docker
Build a container with all dependencies. Mount model/pickles from external storage (S3, etc.).

### Production Server
Use Gunicorn + Streamlit's server mode. Load model from S3 or similar at startup.

### Model Hosting
- **Hugging Face Model Hub** — free, simple
- **AWS S3** — scalable, reliable
- **Google Cloud Storage** — similar to S3
- **GitHub Releases** — quick and dirty for small models

---

## 🧪 What's Inside `app.py`

The code is intentionally minimal:
- **~90 lines of pure logic** — no bloat
- **Fail-fast error handling** — clear messages if artifacts are missing
- **Direct preprocessing** — matches training exactly
- **ADHD-friendly design** — simple UI, no distractions


