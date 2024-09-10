FROM python:3.11-slim

# Встановлення залежностей
RUN pip install pymongo

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо локальні файли до контейнера
COPY . /app

# Запускаємо main.py
CMD ["python", "main.py"]
