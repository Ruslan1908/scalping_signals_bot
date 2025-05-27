# scalping_signals_bot/utils/model_loader.py
"""
Загружает модель (AttentionLSTM), перемещает на устройство
и предоставляет функцию predict для получения вероятности.
"""

import torch
from models.attention_model import AttentionLSTMModel
from utils.config import MODEL_PATH, DEVICE, FEATURE_DIM, SEQ_LEN

def load_model():
    """Загрузка модели и весов."""
    model = AttentionLSTMModel(feature_dim=FEATURE_DIM, seq_len=SEQ_LEN)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model.to(DEVICE)
    model.eval()
    return model

def predict(model, input_tensor):
    """Инференс модели. input_tensor shape: (1, SEQ_LEN, FEATURE_DIM)"""
    with torch.no_grad():
        output = model(input_tensor.to(DEVICE))  # логит
        prob = torch.sigmoid(output).item()      # [0, 1]
    return prob
