# AI ADHD Predictor — GitHub Ready

A minimal Streamlit app for running trained ADHD predictions. Clean code, same preprocessing as the notebook.

## What to Commit
- `app.py` — the Streamlit app (production-ready)
- `requirements.txt` — Python dependencies
- `README.md` — this file
- `setup_venv.ps1` — environment setup helper
- `.gitignore` — excludes venv, model, datasets

## What NOT to Commit
- `model_base.h5` (use Git LFS or host externally)
- `pickle/` (optional; host separately or use Git LFS)
- `dataset/` — local data, not for repo
- `.venv/` or `venv/` — virtual environments

## Quick Start

### 1. Clone & Setup (PowerShell)
```powershell
git clone <your-repo-url>
cd Colab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements.txt
```

### 2. Place Model & Helpers
Download or link your trained artifacts:
- `model_base.h5` → repository root
- `pickle/columns.pkl`, `pickle/encoded_columns.pkl`, `pickle/scaler.pkl` → `pickle/` folder

### 3. Run the App
```powershell
streamlit run app.py
```

Open http://localhost:8501 in your browser.

## How It Works
1. **Inputs:** Collect age, gender, education stage, symptom scores, and comorbidity flags via Streamlit UI.
2. **Preprocessing:** One-hot encode categorical columns, reindex to match training, and scale with `StandardScaler`.
3. **Prediction:** Load the Keras model and run inference.
4. **Output:** Display prediction probability and risk label.

The preprocessing is identical to the training notebook, ensuring parity.

## Deployment Tips
- **Streamlit Cloud:** Upload repo (without model/pickles), add a setup step to download the model at startup.
- **GitHub Actions:** Use CI to validate preprocessing against a test dataset on each push.
- **Model hosting:** Consider Hugging Face Model Hub, AWS S3, or Google Cloud Storage for the `.h5` file.

## Notes
- Clean, minimal code — no heavy try/except blocks.
- Fail-fast on missing artifacts (clear error messages).
- Production-focused repo structure.

---
**Clean, simple, and shipped with good vibes ✨**
