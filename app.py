import numpy as np
import pickle
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

MODEL_PATH = 'model.pkl'
model = pickle.load(open(MODEL_PATH, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    result = str(prediction[0])  # Gets the first element as string
    return render_template('index.html', prediction_text='{}'.format(result))

if __name__ == "__main__":
    app.run(debug=True)