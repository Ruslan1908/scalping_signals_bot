# scalping_signals_bot/models/attention_model.py
"""
Нейросеть AttentionLSTM:
- Conv1D выделяет локальные паттерны
- BiLSTM улавливает временные зависимости
- Attention агрегирует важные шаги
- Linear → бинарный логит (подаётся в sigmoid)
"""

import torch
import torch.nn as nn

class AttentionBlock(nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.attn = nn.Linear(hidden_dim, 1)

    def forward(self, lstm_out):
        weights = self.attn(lstm_out)           # (B, T, 1)
        weights = torch.softmax(weights, dim=1) # нормализованные веса по времени
        context = (lstm_out * weights).sum(dim=1)  # агрегированный выход: (B, H)
        return context

class AttentionLSTMModel(nn.Module):
    def __init__(self, feature_dim, seq_len, lstm_hidden=64, conv_out=32):
        super().__init__()
        self.conv1 = nn.Conv1d(in_channels=feature_dim, out_channels=conv_out, kernel_size=3)
        self.relu = nn.ReLU()
        self.lstm = nn.LSTM(
            input_size=conv_out,
            hidden_size=lstm_hidden,
            batch_first=True,
            bidirectional=True
        )
        self.attn = AttentionBlock(lstm_hidden * 2)
        self.fc = nn.Linear(lstm_hidden * 2, 1)

    def forward(self, x):  # x: (B, T, F)
        x = x.transpose(1, 2)           # (B, F, T)
        x = self.relu(self.conv1(x))    # (B, C, T-2)
        x = x.transpose(1, 2)           # (B, T-2, C)
        lstm_out, _ = self.lstm(x)      # (B, T-2, 2H)
        context = self.attn(lstm_out)   # (B, 2H)
        return self.fc(context)         # (B, 1)
