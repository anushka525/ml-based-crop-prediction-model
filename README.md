**🌾 Crop Recommendation System ✨ (Machine Learning Project)**
Status: ✅ Completed

Technology Stack: 🐍 Python, 🌐 Flask, 🧠 Scikit-learn

**💡 Project Overview**
This project is a Machine Learning-based Crop Recommendation System deployed as a user-friendly web application. It is designed to assist farmers and agricultural users in determining the optimal crop to cultivate for a specific area by analyzing key environmental and soil parameters.

The core of the system is a trained Random Forest Classifier model (model.pkl), which ensures that recommendations are data-driven, promoting efficient resource use and maximizing potential yield. The entire application is served using a Flask backend (app.py).

**⚙️ Key Features**
The system provides intelligent crop prediction based on seven critical agricultural parameters, collected via a simple, green-themed web interface (index.html, style.css):

Soil Nutrients:

N (Nitrogen content)

P (Phosphorus content)

K (Potassium content)

**Environmental Data:**

🌡️ Temperature (in °C)

💧 Humidity (in %)

🧪 pH (pH value of the soil)

🌧️ Rainfall (in mm)

The application features responsive design and a clean user experience, making agricultural planning accessible to everyone.

**🛠️ Technology Stack**
The application leverages a lightweight and effective combination of Python tools and web technologies, all managed via requirements.txt.

**🧠 Backend & Machine Learning**
**Python:** Primary programming language.

**Flask (v3.1.0):** Lightweight micro-framework for building the web application and handling API endpoints (/predict).

**Scikit-learn (v1.6.1):** Used for loading and utilizing the trained Random Forest Classifier model.

**NumPy:** Essential for efficient processing of numerical input features.

**Pickle:** Used to serialize and deserialize the ML model object (model.pkl).

**🎨 Frontend & Deployment**
**HTML5 (index.html):** Structures the clean input form.

**CSS3 (style.css):** Provides the modern, green-focused styling, including background from farm.avif.

**Gunicorn:** Production-ready WSGI server used for robust deployment.

**Render:** Cloud platform used for hosting the live application.

**🚀 Local Setup and Installation**
Follow these steps to get a copy of the project running on your local machine.

**✅ Prerequisites**
Python (3.x recommended)

pip (Python package installer)

**🧑‍💻 Installation Steps**
**Clone the Repository:**

**Bash**

git clone <your-repo-link>
cd crop-prediction-machine-learning-model
Create a Virtual Environment (Recommended):

**Bash**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

**Bash**

pip install -r requirements.txt
Run the Application:

**Bash**

python app.py
Access the App: Open your web browser and navigate to the local server address.

**📂 Project File Structure**
**app.py:** Core application logic, routing, and model prediction.

**model.pkl:** The compiled Machine Learning model file.

**index.html:** The home page template with the crop feature input form.

**requirements.txt:** Defines all project dependencies and their versions.

**style.css:** Custom styling for the web application.

**🤝 Contributing & 📜 License**
Contributions, bug reports, and feature requests are highly appreciated!

This project is licensed under the [Specify Your License Here, e.g., MIT License].
