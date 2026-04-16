FROM python:3.11-slim

# Evita archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/config/

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev

# Copiar requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar proyecto
COPY . .
COPY .env .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]