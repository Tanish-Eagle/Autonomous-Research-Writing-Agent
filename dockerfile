FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy dependency file first
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (FastAPI default via uvicorn)
EXPOSE 8000

# Run the app
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]