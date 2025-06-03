# scalping_signals_bot/data/features.py
"""
Обработка свечей в вектор признаков для подачи в модель:
- RSI, ATR, MA5, MA20
- нормализация объёма и цены
- выход — np.array (1, SEQ_LEN, FEATURE_DIM)
"""

import numpy as np
import pandas as pd
from utils.config import SEQ_LEN


def calculate_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period, min_periods=1).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period, min_periods=1).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def calculate_atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = tr.rolling(window=period, min_periods=1).mean()
    return atr


def extract_features(df: pd.DataFrame) -> np.ndarray:
    df = df.copy()

    df["rsi"] = calculate_rsi(df["close"], period=14)
    df["atr"] = calculate_atr(df["high"], df["low"], df["close"], period=14)
    df["ma5"] = df["close"].rolling(window=5).mean()
    df["ma20"] = df["close"].rolling(window=20).mean()
    df["vol"] = df["volume"].astype(float)
    df["return"] = df["close"].pct_change()
    df["vol_norm"] = (df["vol"] - df["vol"].mean()) / (df["vol"].std() + 1e-6)
    df["price_norm"] = (df["close"] - df["close"].mean()) / (df["close"].std() + 1e-6)

    df = df.dropna().tail(SEQ_LEN)

    feature_cols = ["price_norm", "rsi", "atr", "ma5", "ma20", "vol_norm", "return"]
    features = df[feature_cols].fillna(0).to_numpy()

    # Паддинг, если длина < SEQ_LEN
    if features.shape[0] < SEQ_LEN:
        pad = np.zeros((SEQ_LEN - features.shape[0], features.shape[1]))
        features = np.vstack([pad, features])

    return np.expand_dims(features, axis=0)  # (1, SEQ_LEN, FEATURES)
