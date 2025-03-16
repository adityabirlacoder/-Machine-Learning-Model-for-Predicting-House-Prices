# -Machine-Learning-Model-API-for-House-Price-Prediction

A Flask-based REST API that predicts house prices using a pre-trained machine learning model built with XGBoost. This project allows users to send property data via a POST request and receive predicted prices in response.

---

## 📦 Features
- Predict house prices using a trained XGBoost model
- API built with Flask for lightweight deployment
- JSON-based input and output
- Easily extendable to other ML models

---

## 🛠️ Technologies Used
- Python 3.x
- Flask
- XGBoost 2.1.4
- scikit-learn 1.3.0
- pandas 2.2.3
- numpy 1.24.4

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/-Machine-Learning-Model-for-Predicting-House-Prices.git
cd -Machine-Learning-Model-for-Predicting-House-Prices
```

### 2. Install Dependencies
Ensure you are in the same directory as `flask_model_api.py`, then run:
```bash
pip install xgboost==2.1.4 scikit-learn==1.3.0 pandas==2.2.3 numpy==1.24.4 flask
```

### 3. Run the API
```bash
python flask_model_api.py
```

Flask will start the server at:
```
http://127.0.0.1:5000/
```

---

## 📡 API Endpoint

### POST `/predict`
Send JSON data to predict house prices.



## 📁 Files
| File                  | Description                                       |
|-----------------------|---------------------------------------------------|
| `flask_model_api.py`  | Flask app serving the trained ML model           |
| `model.pkl`           | Serialized XGBoost model file                     |
| `To_Run_Server.txt`   | All information to establish local server         |
| `Machine Learning Engineer.ipynb`| Data analysis and model training steps    |

---


## 🌐 Live Demo (Optional)
If deployed:
**Hosted API**: [http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict)


---

## 🤝 Contributing
Feel free to open issues or submit pull requests for improvements!

---

## 📧 Contact
Created by [Aditya Birla] — birlaaditya285@gmail.com
