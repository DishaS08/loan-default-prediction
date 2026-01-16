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

## Project Structure
loan-default-prediction/
│── Loan_default.ipynb # Data analysis & model training
│── loan.csv # Dataset
│── loan_predictor.py # Streamlit app
│── lr_model.pkl # Trained model
│── scaler.pkl # Feature scaler
│── requirements.txt # Dependencies
│── README.md


## Run Locally
1. Clone the repository  
2. Install dependencies from `requirements.txt`  
3. Run the Streamlit application  

```bash
streamlit run loan_predictor.py
Output
The application displays:

Loan default risk percentage

Loan status as Safe or Risky based on predicted probability

Use Case
This project demonstrates the application of machine learning in credit risk analysis and supports data-driven decision-making for loan approval.

markdown
Copy code

✅ This will render **perfectly on GitHub**  
✅ Clean, professional, resume-ready  

If you want, next I can give:
- **GitHub “About” section (2 lines)**
- **One-line resume project point**
- **Streamlit Cloud description**
