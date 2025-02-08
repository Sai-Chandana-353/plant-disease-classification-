### 🌱 Plant Disease Classification
📌 Overview
This project utilizes Python and Artificial Intelligence (AI) to help identify plant diseases and provide appropriate solutions. It assists farmers and gardeners by simplifying the process of disease detection and offering actionable solutions, including prevention steps and recommended supplements.

### 🚀 Features
✅ Identify plant diseases using AI-powered predictions
✅ Provide disease details and prevention suggestions
✅ User-friendly web interface for easy image uploads
✅ Virtual environment (venv) for dependency management

### 🛠️ Technology Stack
Backend: Python, Flask, TensorFlow/Keras
Frontend: HTML, CSS, Bootstrap, Jinja2
Libraries Used: Pillow (Image Processing), JSON (Class Mapping)
Environment: Virtual Environment (venv) for dependency isolation
### 🏗️ Project Structure
├── venv/                   # Virtual environment  
│   ├── Include/  
│   ├── Lib/  
│   ├── Scripts/  
│   ├── pyvenv.cfg  
├── static/                  # Static files (CSS, JS, Images)  
├── templates/               # HTML Templates  
│   ├── home.html            # Landing page  
│   ├── index.html           # Upload form for image input  
│   ├── result.html          # Displays disease prediction & solutions  
├── model/                   # Trained model (model.h5)  
├── app.py                   # Main application script  
├── requirements.txt         # Dependencies  
├── README.md                # Project documentation  
### 🌟 How It Works
1️⃣ User uploads an image of a plant leaf through the web interface.
2️⃣ AI model processes the image and predicts the disease using TensorFlow/Keras.
3️⃣ The system displays results with disease details and prevention suggestions.
### 🏃‍♂️ Getting Started
1️⃣ Clone the Repository
git clone https://github.com/Sai-Chandana-353/plant-disease-classification.git
cd plant-disease-classification
2️⃣ Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
python app.py
### 📜 License
This project is open-source under the MIT License.



