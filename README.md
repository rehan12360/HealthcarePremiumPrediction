# HealthCare Premium Prediction
# 🏥 Health Insurance Cost Predictor

This is a **Machine Learning-based Web App** that predicts health insurance costs based on user inputs such as age, BMI, medical history, smoking status, and more. The application features a clean, responsive, and user-friendly interface built using **Streamlit**.

---

## 🚀 Live App

🔗 [Click here to try the app](#)  
*(Replace `#` with your actual Streamlit app URL)*

---

## 📌 About the Project

This project was created as part of my learning journey through the **Codebasics Data Science Bootcamp**, mentored by **Dhaval Patel**.

### 📈 Why Two Models?

During experimentation, it was observed that the prediction error was high (around **85%**) for users aged **25 or below**, whereas the performance was stable for others. To tackle this:

- For users **≤ 25 years old**, we used a **Linear Regression** model with an additional feature: **Genetical Risk**.
- For users **> 25 years old**, we used a powerful **XGBoost Regressor**.
  
This two-split model approach helped us reduce the error significantly to **just 2.1%** in the low-age group.

---

## 🧠 Tech Stack

| Area           | Tools / Libraries Used                            |
|----------------|---------------------------------------------------|
| Frontend UI    | Streamlit, HTML/CSS (custom CSS for styling)      |
| ML Algorithms  | Linear Regression, XGBoost Regressor              |
| Data Handling  | Pandas, NumPy                                     |
| ML Utilities   | Scikit-learn                                       |
| Deployment     | Streamlit Cloud                                   |
| Version Control| Git, GitHub                                       |

---

## 📥 Features

- Predicts accurate insurance costs based on user attributes.
- Handles edge cases for younger demographics using a split-model approach.
- Custom-styled, gradient-enhanced UI for better user experience.
- Easy-to-use form layout using multi-column responsive grid.

---

## 🧪 How It Works

1. User enters their details like Age, BMI Category, Smoking Status, etc.
2. If Age ≤ 25:
   - **Linear Regression** is used with **Genetical Risk** feature.
3. If Age > 25:
   - **XGBoost Regressor** is used.
4. The predicted insurance cost is displayed instantly on the screen.

---

## 📁 Project Structure
📦 health-insurance-predictor
├── prediction_helper.py # Contains logic for model selection and prediction
├── app.py # Streamlit application code (main UI)
├── models/
│ ├── linear_model.pkl
│ └── xgb_model.pkl
├── assets/
│ └── style.css # Custom styles for enhanced UI
├── requirements.txt # Required Python packages
└── README.md # You're here!

## 🧑‍💻 How to Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/health-insurance-predictor.git
   cd health-insurance-predictor
2. Install dependencies:   
  ```bash
   pip install -r requirements.txt



