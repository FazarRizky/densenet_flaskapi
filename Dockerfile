# Gunakan image Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy file ke container
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 7860

# Jalankan aplikasi Flask
CMD ["python", "app.py"]
