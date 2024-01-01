OCR & Numerical Analysis Hub This repository contains a Flask-based web application that provides two main endpoints:

OCR - Extract Text from Image: Allows users to upload an image, and the system extracts text content from the image using Tesseract OCR.

Compute Measures from Numbers: Enables users to input a list of numbers separated by commas, and the application computes various statistical measures such as mean, median, standard deviation, and percentiles.

Prerequisites Ensure you have the following installed on your machine: Docker Git

Steps to Run the Project

- Clone the Repository Clone this repository to your local machine using the following command:
  
**git clone https://github.com/Shyamsj-19/ocr-numerical-analysis-hub.git**

- Navigate to the project directory:
  
**cd ocr-numerical-analysis-hub**

- Build Docker Image Build the Docker image using the provided Dockerfile:
  
**docker build -t ocr-analysis-app .**

- Run Docker Container Run the Docker container based on the built image:
  
**docker run -p 9090:9090 ocr-analysis-app**

- Access the Application Once the Docker container is up and running, open your web browser and navigate to: 
**http://localhost:9090/**

You should see the homepage of the OCR & Numerical Analysis Hub. From here, you can navigate to the endpoints to either upload an image for text extraction or compute measures from a list of numbers.

Additional Notes The application uses Tesseract OCR for text extraction from images. Ensure you have Docker installed to set up the necessary environment with Tesseract and other required libraries. The application is configured to run on port 9090. Ensure this port is available and not being used by another application on your machine. The uploaded images are processed on the server-side using Python and Tesseract. Ensure you have sufficient resources (CPU, memory) available if processing large images or multiple requests simultaneously.

Contributing If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request. Your contributions are highly appreciated! Happy analyzing! 🚀
