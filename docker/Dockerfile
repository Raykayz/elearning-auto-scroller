FROM selenium/standalone-chrome:latest

USER root

# Installa Python e pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Crea directory di lavoro
WORKDIR /app

# Copia i file necessari
COPY requirements.txt .
COPY src/moodle_auto.py .

# Installa dipendenze Python
RUN pip3 install --no-cache-dir -r requirements.txt --break-system-packages

# Crea utente non-root
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

# Comando di default
CMD ["python3", "moodle_auto.py"]
