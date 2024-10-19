import pickle as pk
import numpy as np

# Function to load pickle files safely
def load_pickle(file_path):
    with open(file_path, 'rb') as f:
        return pk.load(f)

# Load the scaler
scaler_path = 'scaler.pkl'
scaler = load_pickle(scaler_path)

# Load the model
model_path = 'model.pkl'
model = load_pickle(model_path)

# Load the label encoder
label_encoder_path = 'label_encoder.pkl'
label_encoder = load_pickle(label_encoder_path)

# Function to predict using the loaded model and scale
def predict_and_decode(input_number):
    input_data = np.array([input_number]).reshape(-1, 1)
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)
    predicted_label = label_encoder.inverse_transform(prediction)
    return predicted_label

# Predict for numbers from 0 to 99
for number in range(100):
    try:
        result = predict_and_decode(number)
        print(f"Input Number: {number}, Predicted Output: {result}")
    except Exception as e:
        print(f"Error processing number {number}: {e}")