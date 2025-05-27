# scalping_signals_bot/utils/signal_logger.py
"""
Сохраняет каждый сигнал модели в CSV-файл.
Используется ботом и дэшбордом.
"""

import csv
import os
from datetime import datetime

LOG_FILE = "logs/signals.csv"
os.makedirs("logs", exist_ok=True)

HEADER = ["timestamp", "asset", "probability", "decision"]

def log_signal(asset: str, prob: float, decision: str):
    """Добавляет строку в CSV с сигналом."""
    row = [datetime.now().isoformat(), asset, f"{prob:.4f}", decision]
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(HEADER)
        writer.writerow(row)

def load_history():
    """Возвращает всю историю сигналов в виде списка словарей."""
    if not os.path.isfile(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)
