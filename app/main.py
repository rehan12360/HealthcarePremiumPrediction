import streamlit as st
from prediction_helper import predict

# Gradient text style for title + input/button styling
st.markdown(
    """
    <style>
    /* Gradient text for title */
    .title-gradient {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #6a11cb, #2575fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Style input boxes */
    div.stNumberInput > label, div.stSelectbox > label {
        font-weight: 600;
        color: #333;
        font-size: 1rem;
    }
    div.stNumberInput > div > input, div.stSelectbox > div > div[role="combobox"] {
        border: 2px solid #6a11cb;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 1rem;
        transition: border-color 0.3s ease;
        color: #111;
    }
    div.stNumberInput > div > input:focus, div.stSelectbox > div > div[role="combobox"]:focus {
        outline: none;
        border-color: #2575fc;
        box-shadow: 0 0 8px rgba(37, 117, 252, 0.5);
    }

    /* Style Predict button */
    div.stButton > button {
        background: linear-gradient(90deg, #6a11cb, #2575fc);
        color: white;
        font-size: 1.2rem;
        font-weight: 700;
        padding: 10px 25px;
        border-radius: 25px;
        border: none;
        transition: background 0.4s ease;
        cursor: pointer;
        margin-top: 20px;
        width: 100%;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #2575fc, #6a11cb);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with gradient text style
st.markdown('<h1 class="title-gradient">Health Insurance Cost Predictor</h1>', unsafe_allow_html=True)

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f'Predicted Amount: {prediction}')
