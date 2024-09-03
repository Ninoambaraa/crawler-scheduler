# Gunakan image Python sebagai base image
FROM python:3.9-slim

# Set environment variable untuk memastikan bahwa print statements segera muncul di log
ENV PYTHONUNBUFFERED=1

# Buat direktori kerja di dalam container
WORKDIR /app

# Buat virtual environment di dalam container
RUN python -m venv /opt/venv

# Aktifkan virtual environment dan install dependencies
RUN /opt/venv/bin/pip install --upgrade pip
COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Salin semua file dari direktori lokal ke dalam direktori kerja di dalam container
COPY . .

# Set PATH environment variable untuk menggunakan venv secara default
ENV PATH="/opt/venv/bin:$PATH"

# Tentukan perintah untuk menjalankan aplikasi
ENTRYPOINT ["python", "scheduler.py"]
