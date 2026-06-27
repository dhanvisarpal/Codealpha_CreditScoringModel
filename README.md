# Credit Scoring Model

## Project Overview

This project predicts whether a customer is likely to default on their next credit card payment using 
machine learning classification algorithms. The application is deployed as an interactive Streamlit dashboard, 
allowing users to enter customer financial information and receive a default risk prediction.

## Features

- Interactive Streamlit Dashboard
- Dataset Overview
- Exploratory Data Analysis (EDA)
- Model Performance Comparison
- Customer Default Prediction
- Probability of Default Estimation

## Machine Learning Models Used

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

## Best Performing Model

**Random Forest**

- Accuracy: **81.43%**
- Precision: **0.64**
- Recall: **0.36**
- F1-Score: **0.46**
- ROC-AUC: **0.7567**

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

## 📂 Project Structure

```text
Credit Card Default Prediction/
│── app.py
│── requirements.txt
│── README.md
│
├── data/
│   └── default of credit card clients.csv
│
├── models/
│   └── random_forest_model.pkl
│
└── pages/
    ├── 1.Dataset Overview.py
    ├── 2.EDA.py
    ├── 3.Model Comparison.py
    └── 4.Predict Customer Default.py
```

##  How to Run

1. Clone this repository.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## 📊 Project Outcome

The Random Forest classifier achieved the best overall performance and was selected as the final model 
for predicting customer default risk. The application provides an intuitive interface for entering customer 
details and estimating the likelihood of default.
