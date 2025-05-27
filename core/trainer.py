# scalping_signals_bot/core/trainer.py
"""
Модуль для обучения модели AttentionLSTM на новых данных:
- обучает на одном батче
- сохраняет веса модели в файл
"""

import torch
import torch.nn as nn
import torch.optim as optim
from models.attention_model import AttentionLSTMModel
from utils.config import DEVICE, MODEL_PATH, FEATURE_DIM, SEQ_LEN

def train_once(train_data, labels, epochs=5, lr=0.001):
    model = AttentionLSTMModel(feature_dim=FEATURE_DIM, seq_len=SEQ_LEN).to(DEVICE)
    model.train()

    optimizer = optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.BCEWithLogitsLoss()

    X_tensor = torch.tensor(train_data, dtype=torch.float32).to(DEVICE)
    y_tensor = torch.tensor(labels, dtype=torch.float32).unsqueeze(1).to(DEVICE)

    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X_tensor)
        loss = loss_fn(outputs, y_tensor)
        loss.backward()
        optimizer.step()
        print(f"🧠 Эпоха {epoch+1}/{epochs} — Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), MODEL_PATH)
    print(f"✅ Вес модели сохранён в {MODEL_PATH}")

def schedule_daily_training(data_loader_func):
    X, y = data_loader_func()
    train_once(X, y)
