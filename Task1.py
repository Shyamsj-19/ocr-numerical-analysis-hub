from flask import Flask, request, render_template, jsonify
from PIL import Image
import io
import numpy as np
import pytesseract

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/endpoint-1', methods=['GET', 'POST'])
def extract_text():
    if request.method == 'GET':
        return render_template('endpoint-1.html')
    
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    image = Image.open(io.BytesIO(image_file.read()))
    extracted_text = pytesseract.image_to_string(image)
    return jsonify({'text': extracted_text}), 200

@app.route('/endpoint-2', methods=['GET', 'POST'])
def compute_measures():
    if request.method == 'POST':
        try:
            numbers = [float(num) for num in request.form.get('numbers').split(',')]
            measures = {
                'mean': np.mean(numbers),
                'median': np.median(numbers),
                'std': np.std(numbers),
                'percent_25': np.percentile(numbers, 25),
                'percent_75': np.percentile(numbers, 75),
                'min': np.min(numbers),
                'max': np.max(numbers)
            }
            return jsonify(measures)
        except Exception as e:
            return jsonify({"error": str(e)})
    return render_template('endpoint-2.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=9090)
