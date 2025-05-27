# scalping_signals_bot/data/live_data.py
"""
Генератор свечей для модели.
Пока нет подключения к PocketOption или брокеру, используется mock-режим.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from utils.config import SEQ_LEN, LIVE_MODE

def get_mock_candles():
    """Генерирует фейковые OHLC свечи длиной SEQ_LEN."""
    now = datetime.utcnow()
    data = []
    for i in range(SEQ_LEN):
        open_ = 1.1 + np.random.randn() * 0.001
        close = open_ + np.random.randn() * 0.0005
        high = max(open_, close) + np.random.rand() * 0.0003
        low = min(open_, close) - np.random.rand() * 0.0003
        volume = np.random.randint(800, 1200)
        timestamp = now - timedelta(minutes=SEQ_LEN - i)
        data.append({'timestamp': timestamp, 'open': open_, 'high': high, 'low': low, 'close': close, 'volume': volume})
    return pd.DataFrame(data)

def get_live_candles():
    """Заглушка под подключение к API. Сейчас не реализовано."""
    raise NotImplementedError("LIVE_MODE включен, но источник свечей не реализован.")

def get_candles():
    """Выбор между live и mock режимом."""
    return get_live_candles() if LIVE_MODE else get_mock_candles()
