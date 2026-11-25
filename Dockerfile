FROM python:3.15.0-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN python model/download_models.py

EXPOSE 8000 8501

CMD ["sh", "start.sh"]
