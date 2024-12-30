import os
from flask import Flask, redirect, render_template, request
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd
from werkzeug.utils import secure_filename

# Load disease and supplement info
disease_info = pd.read_csv('C:/Users/saich/Downloads/Plant-Disease-Detection-2/Flask Deployed App/disease_info.csv', encoding='cp1252')
supplement_info = pd.read_csv('C:/Users/saich/Downloads/Plant-Disease-Detection-2/Flask Deployed App/supplement_info.csv', encoding='cp1252')

# Load model
model = CNN.CNN(39)
model.load_state_dict(torch.load("C:/Users/saich/Downloads/Plant-Disease-Detection-2/Flask Deployed App/plant_disease_model_1_latest.pt"))
model.eval()

def prediction(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        image = image.resize((224, 224))
        input_data = TF.to_tensor(image).unsqueeze(0)
        output = model(input_data)
        output = output.detach().numpy()
        index = np.argmax(output)
        return index
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

@app.route('/index')
def ai_engine_page():
    return render_template('index.html')

@app.route('/mobile-device')
def mobile_device_detected_page():
    return render_template('mobile-device.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            upload_folder = 'static/uploads'
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)  # Create the directory if it doesn't exist
            
            filename = secure_filename(image.filename)
            file_path = os.path.join(upload_folder, filename)
            image.save(file_path)

            pred = prediction(file_path)
            if pred is not None:
                title = disease_info['disease_name'][pred]
                description = disease_info['description'][pred]
                prevent = disease_info['Possible Steps'][pred]
                image_url = disease_info['image_url'][pred]
                supplement_name = supplement_info['supplement name'][pred]
                supplement_image_url = supplement_info['supplement image'][pred]
                supplement_buy_link = supplement_info['buy link'][pred]
                return render_template('submit.html', title=title, desc=description, prevent=prevent,
                                       image_url=image_url, pred=pred, sname=supplement_name, 
                                       simage=supplement_image_url, buy_link=supplement_buy_link)
            else:
                return "Prediction error occurred.", 500
        else:
            return "No file uploaded.", 400

@app.route('/market', methods=['GET', 'POST'])
def market():
    return render_template('market.html', 
                           supplement_image=list(supplement_info['supplement image']),
                           supplement_name=list(supplement_info['supplement name']), 
                           disease=list(disease_info['disease_name']), 
                           buy=list(supplement_info['buy link']))

if __name__ == '__main__':
    app.run(debug=True)
