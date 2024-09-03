# Menggunakan image Python sebagai base
FROM python:3.9-slim

# Mengatur direktori kerja di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal dependencies yang ada di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file dari direktori lokal ke dalam container
COPY . .

# Menjalankan script Python
CMD ["python", "scheduler.py"]
