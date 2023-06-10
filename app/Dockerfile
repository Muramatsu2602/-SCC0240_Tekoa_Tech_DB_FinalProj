FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY verify_table.py ./

CMD ["python", "main.py","&&","python", "verify_table.py"]
