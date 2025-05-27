# 🤖 Scalping Signals Bot

Полностью автономный бот для краткосрочной торговли валютными парами:
- 🚀 Нейросеть AttentionLSTM
- 📲 Telegram-интерфейс + MiniApp UI
- 🔁 REST API на FastAPI
- 📈 Дашборд на Streamlit
- 🐳 Docker-ready для деплоя

---

## 📦 Возможности

- Получение сигналов в Telegram (`/signal`)
- Веб-интерфейс с графиком и историей (MiniApp)
- REST API: `/signal`, `/history`, `/status`
- Ежедневное автообучение модели
- Логирование и визуализация сигналов

---

## 🛠️ Стек технологий

- `Python 3.10`
- `PyTorch` + `pandas_ta`
- `FastAPI` / `Streamlit`
- `Docker` / `Makefile`
- `Chart.js` для MiniApp

---

## 🚀 Быстрый старт

```bash
# Склонировать
git clone https://github.com/yourname/scalping-signals-bot.git
cd scalping-signals-bot

# Установить зависимости
pip install -r requirements.txt

# Запустить Telegram-бота
python bot.py

# Или через Docker
make up
```

---

## 🔌 REST API (localhost:8000)

| Метод | Путь         | Описание                 |
|--------|--------------|--------------------------|
| GET    | `/signal`    | Вернуть текущий сигнал   |
| GET    | `/history`   | История последних сигналов |
| GET    | `/status`    | Проверка API             |

---

## 📲 Telegram MiniApp

MiniApp доступен по ссылке:
```
https://<your-username>.github.io/scalping-signals-bot/miniapp.html
```

Подключение:
- Добавить WebApp-кнопку в бота через BotFather
- Или через `types.WebAppInfo(url=...)`

---

## 📊 Streamlit (локально)
```bash
streamlit run signals_dashboard.py
```

---

## 📂 Структура проекта

```
scalping-signals-bot/
├── bot.py                  # Telegram-бот
├── api/                    # FastAPI REST API
├── web/                    # MiniApp UI (gh-pages)
├── models/ core/ data/ ... # Нейросеть и обработка
├── retrain_script.py       # Переобучение
├── docker-compose.yml
├── Makefile / Dockerfile
├── logs/ / model_weights.pt
```

---

## 📄 Лицензия

Проект распространяется под лицензией MIT. См. `LICENSE`.

---

## 💬 Контакты

> [tg:@yourusername](https://t.me/yourusername) — автор
