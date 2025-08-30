from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Stock Price Prediction API")

FEATURES = ["open", "high", "low", "volume"]

class InputRow(BaseModel):
    open: float
    high: float
    low: float
    volume: float

# Load model (must be in same folder)
try:
    model = joblib.load("best_gb_model.pkl")
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

def _validate_df(df: pd.DataFrame):
    if (df["high"] < df["low"]).any():
        raise HTTPException(status_code=400, detail="'high' cannot be less than 'low'")
    return df

@app.get("/")
def read_root():
    return {"message": "Stock Prediction API is running", "features": FEATURES}

@app.post("/predict")
def predict(item: InputRow):
    df = pd.DataFrame([item.dict()])[FEATURES]
    df = _validate_df(df)
    pred = model.predict(df)[0]
    return {"prediction": float(pred)}

@app.post("/predict_batch")
def predict_batch(rows: list[InputRow]):
    df = pd.DataFrame([r.dict() for r in rows])[FEATURES]
    df = _validate_df(df)
    preds = model.predict(df).tolist()
    return {"predictions": [float(p) for p in preds]}
