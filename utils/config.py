# scalping_signals_bot/utils/config.py
"""
Глобальные параметры проекта:
- режимы работы (LIVE, DEBUG)
- путь к модели и данные
- Telegram токен
"""

import os

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_TOKEN", "8116686804:AAEQomMeFifefu66gUz1PRQl3tc2krRp8c4")
AUTHORIZED_USERS = [824311523]  # список разрешённых Telegram ID

# Модель
MODEL_TYPE = "attention"
MODEL_PATH = "model_weights.pt"
SEQ_LEN = 20
FEATURE_DIM = 7  # зависит от extract_features
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Данные
ASSET = "EURUSD"
LIVE_MODE = False
DEBUG = True
