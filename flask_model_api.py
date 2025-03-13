from flask import Flask, request, jsonify
import pickle
import pandas as pd  # Import pandas
import numpy as np

# Load the trained models
with open("Linear_Regression.pkl", "rb") as file:
    linear_model = pickle.load(file)
with open("Decision_Tree.pkl", "rb") as file:
    tree_model = pickle.load(file)
with open("Random_Forest.pkl", "rb") as file:
    rf_model = pickle.load(file)
with open("XGBoost.pkl", "rb") as file:
    xgb_model = pickle.load(file)

# Create a Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Machine Learning Model API! Use the /predict endpoint to get predictions."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON input
        data = request.get_json()
        
        if not data or "features" not in data:
            return jsonify({"error": "Invalid input. Expecting a JSON with a 'features' key."}), 400

        features = data["features"]
        
        # Convert input to DataFrame
        input_data = pd.DataFrame([features])

        # Select model
        model_name = data.get("model", "Linear_Regression")  # Default to Linear Regression if not specified
        models = {
            "Linear_Regression": linear_model,
            "Decision_Tree": tree_model,
            "Random_Forest": rf_model,
            "XGBoost": xgb_model
        }

        if model_name not in models:
            return {"error": f"Model '{model_name}' is not available. Choose from {list(models.keys())}"}, 400

        model = models[model_name]
        
        # Make prediction
        prediction = model.predict(input_data)
        
        return jsonify({"model": model_name, "prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
