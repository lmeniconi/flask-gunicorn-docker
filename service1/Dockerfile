FROM python:3

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:3000", "main:app"]