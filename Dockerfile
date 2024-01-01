# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Tesseract OCR and other necessary libraries
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --upgrade Flask Werkzeug numpy Pillow pytesseract

# Define environment variable for Tesseract
ENV TESSDATA_PREFIX /usr/share/tesseract-ocr/5/tessdata/

# Expose port 9090 for the Flask application
EXPOSE 9090

# Run the Flask application
CMD ["python", "Task1.py"]
