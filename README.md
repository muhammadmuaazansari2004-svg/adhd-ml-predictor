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

### Place Your Model & Helpers

You'll need three things (download from your training artifacts):
- `model_base.h5` — the trained neural network (goes in repo root)
- `pickle/columns.pkl` — feature column order
- `pickle/encoded_columns.pkl` — one-hot encoded column names
- `pickle/scaler.pkl` — data normalization (StandardScaler)

Drop these files in their expected spots, then:

```powershell
streamlit run app.py
```

Open **http://localhost:8501** → boom, you're running predictions.

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
├── pickle/               # (Not in Git, download separately)
│   ├── columns.pkl
│   ├── encoded_columns.pkl
│   └── scaler.pkl
│
└── model_base.h5         # (Not in Git, download separately)
```

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

No heavy try/except blocks. If something's wrong, you'll know immediately.

---

## 🎓 What You'll Learn

- How to align preprocessing between training & inference
- Streamlit for building quick ML UIs
- Handling one-hot encoding with `drop_first=True`
- Scaling data consistently (fit on training, transform on inference)
- Git/GitHub workflows for ML projects
- Why model/data artifacts shouldn't live in Git

---

## ⚠️ Important Disclaimer

**This is NOT a medical tool.** This is educational. ADHD diagnosis requires a real clinician, not a spreadsheet + neural network. If you or someone you know suspects ADHD, talk to a professional.

This project uses **synthetic data**, not real patient data. It's for learning how ML works, period.

---

## 🤝 Contributing

Found a bug? Have ideas? Cool—open an issue or submit a PR. Keep it simple, keep it clean.

---

## 📜 License

See `LICENSE` file. (You already set one up locally, so respect that.)

---

## 💡 Random Tips

- **Local testing:** Run `streamlit run app.py` and play with inputs. See if predictions feel reasonable.
- **Debugging:** Check that `columns.pkl` matches your training columns exactly. Off-by-one errors are silent killers.
- **ADHD-friendly coding:** Write code like you're explaining it to someone with brain fog—be explicit, avoid clever tricks.
- **Git workflow:** Always `.gitignore` your model. Always. Your repo will thank you.

---

## 🚀 What's Next?

- Add CI/CD to validate preprocessing on every push
- Host the model on Hugging Face & auto-download at startup
- Build a Flask API wrapper for non-Streamlit deployments
- Add unit tests for preprocessing parity
- Create a mobile app version

You got this. Ship it. 🎉

---

**Made with care for the neurodivergent community. Ship clean code. Keep it simple.** ✨
