# 💰 Finance Advisor Project

A compact, end-to-end data science project: I built, evaluated and deployed a machine-learning model that predicts stock closing values from daily OHLCV features.  
This repo demonstrates the full pipeline — data creation, EDA, feature engineering, model training/tuning, and deployment via FastAPI.

---

## What this repo contains
- Jupyter notebooks (step-by-step): EDA → features → baseline models → advanced models → hyperparameter tuning → deployment.
- `app_fastapi.py` — FastAPI app that loads the saved model and serves `/predict` endpoints.
- `best_gb_model.pkl` — final tuned Gradient Boosting model (used for the API).
- `requirements.txt` — Python packages needed to run the project.

---

## Quick start (run locally)

1. Clone:
```bash
git clone https://github.com/shahraju/finance_advisor_project.git
cd finance_advisor_project
```

2. Create & activate a virtual env, then install:
```bash
python -m venv finance_env
finance_env\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Run the API:
```bash
uvicorn app_fastapi:app --reload --port 8000
```

4. Open Swagger UI:  
👉 http://127.0.0.1:8000/docs

---

## Example request (POST `/predict`)
```json
{
  "open": 100.5,
  "high": 105.2,
  "low": 98.7,
  "volume": 50000
}
```

Response:
```json
{ "prediction": 101.23 }
```

---

## Short project notes & highlights
- **Dataset:** synthetic OHLCV stock-like series created for the project (not real market data).  
- **Models tried:** Linear Regression, Decision Tree, Random Forest, Gradient Boosting.  
- **Final pick:** Gradient Boosting (tuned) — best test performance (example: MSE ≈ 0.21, R² ≈ 0.98).  
- **Why this is useful:** shows end-to-end pipeline skills: data work, model selection/tuning, and real deployment.

---

## Next steps (ideas)
- Replace synthetic data with real market data (Kaggle / Alpha Vantage).  
- Add a lightweight frontend (Streamlit) to allow non-technical users to query the model.  
- Deploy the API to Render/Railway with a public URL and add CI to automatically redeploy on changes.

---

## Author
**Raju Shah**  
✉️ shahraju2434@gmail.com  
LinkedIn: [Your LinkedIn URL here]
