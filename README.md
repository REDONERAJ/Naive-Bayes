# Car Evaluation Prediction (Naive Bayes + Flask)

This project is a **web-based machine learning application** that predicts the **acceptability of a car** based on six categorical features such as buying price, maintenance cost, number of doors, passenger capacity, luggage boot size, and safety. It uses a **Categorical Naive Bayes** model trained on the **Car Evaluation dataset** from the UCI Machine Learning Repository.

The model classifies cars into one of four categories:  
- **unacc** → Unacceptable  
- **acc** → Acceptable  
- **good** → Good  
- **vgood** → Very Good  

---

##  Features
- Categorical Naive Bayes classifier
- Simple web interface with dropdown menus for all features
- Instant prediction of car acceptability
- Data-driven model trained on UCI Car Evaluation dataset

---

## Project Structure
```car-evaluation-naive-bayes/
│
├── app.py # Flask application
├── model.py # Model training script
├── car_evaluation_naive_bayes_model.pkl # Trained Naive Bayes model
├── templates/
│ └── index.html # HTML form with dropdown inputs
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```

---

## Dataset
- **Source:** [UCI Machine Learning Repository – Car Evaluation Dataset](https://archive.ics.uci.edu/ml/datasets/car+evaluation)
- **Instances:** 1,728
- **Features:**  
  1. Buying Price (`vhigh`, `high`, `med`, `low`)  
  2. Maintenance Cost (`vhigh`, `high`, `med`, `low`)  
  3. Number of Doors (`2`, `3`, `4`, `5more`)  
  4. Persons Capacity (`2`, `4`, `more`)  
  5. Luggage Boot Size (`small`, `med`, `big`)  
  6. Safety Level (`low`, `med`, `high`)  
- **Target Classes:** `unacc`, `acc`, `good`, `vgood`

---

## Prediction Output
The app predicts one of:
- **unacc** – Unacceptable  
- **acc** – Acceptable  
- **good** – Good  
- **vgood** – Very Good  

---

## Requirements

Flask
scikit-learn
pandas
joblib

---

## Screenshot
<img width="1366" height="647" alt="Screenshot 2025-08-11 210634" src="https://github.com/user-attachments/assets/468889ec-8fa7-4885-bf40-af43047c3d51" />
<img width="1366" height="647" alt="Screenshot 2025-08-11 210703" src="https://github.com/user-attachments/assets/04e51f9d-d08e-4851-97bd-a34ce34f6346" />
<img width="1366" height="654" alt="Screenshot 2025-08-11 210713" src="https://github.com/user-attachments/assets/8347b894-ca93-4b9b-91d8-49060dcd6fe8" />


---
