# Loan Default Prediction App

## About
This project is an end-to-end machine learning application that predicts the risk of loan default based on customer financial and repayment details. The model is deployed as an interactive web application using Streamlit, allowing users to input loan-related information and instantly receive a default risk score.

## Application Features
- Interactive Streamlit-based user interface  
- Real-time loan default risk prediction  
- Logistic Regression classification model  
- Feature scaling using a trained scaler  
- Probability-based risk scoring with clear Safe/Risky output  

## How It Works
Users provide basic loan and repayment details such as loan amount, age, billing amount, payment delay, and monthly payment. The inputs are transformed using a saved scaler and passed to a trained Logistic Regression model, which outputs the probability of loan default.

## Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Model:** Logistic Regression  
- **Web Framework:** Streamlit  
- **Model Persistence:** Joblib  

loan-default-prediction/
│
├── Loan_default.ipynb     # EDA + Model training (81% accuracy)
├── loan.csv              # Dataset (30K samples)
│
├── loan_predictor.py     # Streamlit app
├── lr_model.pkl          # Trained model
├── scaler.pkl            # Feature scaler
│
├── requirements.txt
└── README.md



## Run Locally
1. Clone the repository  
2. Install dependencies from `requirements.txt`  
3. Run the Streamlit application  

```bash
streamlit run loan_predictor.py
```


Use Case
This project demonstrates the application of machine learning in credit risk analysis and supports data-driven decision-making for loan approval.

## Output
Prediction: 

- Loan default risk percentage  
- Loan status: Safe or Risky based on predicted probability
  
---
<img width="1799" height="738" alt="image" src="https://github.com/user-attachments/assets/0175199d-c0d9-444d-bf16-c1d34adb215b" />

 ---

<img width="1812" height="730" alt="image" src="https://github.com/user-attachments/assets/eb4aa169-a865-4c3b-acc3-8cd68489eeb5" />

---

<img width="1783" height="725" alt="image" src="https://github.com/user-attachments/assets/62838526-9706-4c00-823e-6caebbf570d2" />

 --- 
 
Live Application

🔗 Streamlit App: https://loan-default-prediction-ufrccvvi77pa4cpyqwpc96.streamlit.app/


