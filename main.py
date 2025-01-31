from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)

# Directory where uploaded files will be temporarily stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded images from the form
    image1 = request.files.get('image1')
    image2 = request.files.get('image2')

    if not image1 or not image2:
        return render_template('index.html', predict_text="Please upload both images!")

    # Save the first image temporarily
    image1_path = os.path.join(app.config['UPLOAD_FOLDER'], image1.filename)
    image1.save(image1_path)

    # Pass the filename to the template
    return render_template('index.html', image1=image1.filename, predict_text="Change Detection Completed!")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Serve the image from the 'uploads' directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
