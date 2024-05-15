FROM python:latest
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir telebot
CMD ["python", "bot.py"]