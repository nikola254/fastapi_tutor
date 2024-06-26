FROM python:3.10.4-slim

COPY . .

RUN pip install -r requariments.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]