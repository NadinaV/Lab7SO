FROM python:3.8-slim
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=script.py

# portul 5000 sa fie disponibil in afara containeului
EXPOSE 5000

# comanda pentru pornirea aplicatiei
CMD ["python", "script.py"]
