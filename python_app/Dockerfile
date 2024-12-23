# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем системные зависимости для сборки psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем приложение
CMD ["python", "app.py"]

