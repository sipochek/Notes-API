FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY main.py database.py schemas.py ./

CMD ["python", "-m","uvicorn","main:app","--host","0.0.0.0","--port","8000"]