FROM python:3.12-slim

WORKDIR /app

COPY calculadora.py .

USER nobody

CMD ["python", "calculadora.py"]
