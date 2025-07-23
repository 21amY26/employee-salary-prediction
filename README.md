# 💼 Employee Salary Prediction using Machine Learning 💵

This project uses machine learning to predict an employee's annual salary based on several features such as age, work experience, education level, job title, industry, working mode, and selected skills.

It features a user-friendly **Streamlit web interface** where users can input their details through dropdowns and get a real-time salary estimate.

---

## 🚀 Features

- Predict salary based on:
  - Age, Experience, Hours worked
  - Education Level (encoded)
  - Job Title (e.g., Software Engineer, Project Manager)
  - Industry (e.g., IT, Finance, Healthcare)
  - Work Mode (Remote, Hybrid, Onsite)
  - Technical/Soft Skills (e.g., Python, Excel, Communication)
- Used Linear Regression, Decision Tree, XGBoost, Random Forest and evaluated on MAE, MSE and R2 metric
- Tuned and trained **XGBoost** model using RandomizedSearchCV for prediction
- Deployed with Streamlit Cloud *(optional)*

---

## 🧠 Model

- Model: `XGBoostRegressor`
- Evaluation Metrics:
  - MAE: 8492.42
  - RMSE: 11761.68
  - R² Score: 0.7760
- Preprocessing:
  - One-hot encoding for categorical data
  - Label encoding for education levels
  - Manual encoding for skills and work mode

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python, XGBoost, Pandas, Scikit-Learn, Google Colab notebooks
- **Model Serialization:** Joblib
- **Deployment:** Streamlit Cloud 

---

## 📁 Repository Structure

```bash
├── st_app.py               # Streamlit app
├── xgboost_salary_model.pkl  # Trained model
├── feature_cols.pkl       # Feature list used during training
├── requirements.txt       # Dependencies
└── README.md              # You're here!
├── 00_empl_sal_create.py       # used pandas to create custom dataset
└── 01_empl_sal_prep.ipynb  # preprocessed dataset in colab nb
└── 02_model_eval_select.ipynb  # split, trained & tested dataset
└── employee_salary_dataset.csv # dataset in csv format
└── prep_emp_sal_data.csv # preprocessed dataset in csv format
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/21amY26/employee-salary-prediction.git
cd employee-salary-prediction
pip install -r requirements.txt
streamlit run st_app.py
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Amisha S.**  
*© 2025 | All rights reserved.*

