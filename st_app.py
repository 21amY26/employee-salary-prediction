import streamlit as st
import pandas as pd
import joblib
model = joblib.load('xgboost_salary_model.pkl')
fc=joblib.load('feature_cols.pkl')

st.title("💼Employee Salary Prediction💵")

jobs = [
    'Accountant', 'Business Analyst', 'Cloud Engineer', 'Content Writer', 'Data Scientist',
    'DevOps Engineer', 'Electrician', 'Financial Analyst', 'Graphic Designer', 'HR Manager',
    'Machine Learning Engineer', 'Marketing Manager', 'Product Manager', 'Project Manager',
    'QA Engineer', 'Research Scientist', 'Sales Executive', 'Software Engineer', 'Technician',
    'UI/UX Designer'
]

industries = [
    'Construction', 'Consulting', 'Finance', 'Healthcare', 'IT', 'Insurance',
    'Manufacturing', 'Media', 'Retail', 'Tech', 'Utilities'
]

skills = [
    'AWS', 'Agile', 'Analytics', 'Azure', 'CI/CD', 'CNC', 'CRM', 'Communication', 'Compliance',
    'Data Analysis', 'Deep Learning', 'Docker', 'Excel', 'Figma', 'Git', 'HRM', 'HTML/CSS',
    'Illustrator', 'InDesign', 'JIRA', 'Java', 'ML', 'MS Project', 'Maintenance', 'Networking',
    'PM', 'Payroll', 'Photoshop', 'Python', 'R', 'SEM', 'SEO', 'SQL', 'Safety', 'Selenium',
    'Tableau', 'Tally', 'Testing', 'Troubleshooting', 'Valuation', 'Wiring', 'WordPress', 'Writing', 'XD'
]
with st.form("form"):
    age=st.number_input("Age", min_value=18, max_value=60, value=30)
    exp=st.number_input("Experience (Years)",0,40,5)
    hours=st.number_input("Hours/Week",10,80,40)
    edu=st.selectbox("Education",["High School","Diploma","Bachelor's","Master's","PhD"])
    wmode=st.selectbox("Work Mode",["Remote","Hybrid","Onsite"])
    job=st.selectbox("Job Title",jobs)
    industry=st.selectbox("Industry",industries)
    skills = st.multiselect("Select Skills",skills) 
    submitted = st.form_submit_button("Predict")

#preprocessing input data
if submitted:
    edu_map = {
        "High School": 0,
        "Diploma": 1,
        "Bachelor's": 2,
        "Master's": 3,
        "PhD": 4
    }
    edu_encoded = edu_map[edu]

    # Start with all zeros
    input_dict = {col: 0 for col in fc}

    # Fill actual values
    input_dict['Age'] = age
    input_dict['Experience (Years)'] = exp
    input_dict['Hours/Week'] = hours
    input_dict['Education Level Encoded'] = edu_encoded

    # One-hot categorical
    input_dict[f'Work Mode_{wmode}'] = 1
    input_dict[f'Job Title_{job}'] = 1
    input_dict[f'Industry_{industry}'] = 1

    # One-hot skills
    for skill in skills:
        if skill in input_dict:
            input_dict[skill] = 1

    # Predict
    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Salary: ${prediction:,.2f}")