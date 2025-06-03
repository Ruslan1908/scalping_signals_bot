# scalping_signals_bot/api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from data.live_data import get_candles
from data.features import extract_features
from utils.model_loader import load_model, predict
from utils.signal_logger import log_signal, load_history
import torch

app = FastAPI()
model = load_model()

class SignalResponse(BaseModel):
    asset: str
    probability: float
    decision: str

@app.get("/status")
def status():
    return {"status": "online", "model": "AttentionLSTM"}

@app.get("/signal", response_model=SignalResponse)
def signal():
    df = get_candles()
    X = extract_features(df)
    X_tensor = torch.tensor(X, dtype=torch.float32)
    prob = predict(model, X_tensor)
    decision = "BUY ✅" if prob > 0.6 else "SELL ❌" if prob < 0.4 else "WAIT ⏸"
    log_signal("EURUSD", prob, decision)
    return {"asset": "EURUSD", "probability": prob, "decision": decision}

@app.get("/history")
def history():
    return load_history()[-20:]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
