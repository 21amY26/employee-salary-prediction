import pandas as pd
import random

# Define attributes
education_levels = ['High School', 'Diploma', "Bachelor's", "Master's", 'PhD']
job_titles = [
    'Software Engineer', 'Data Scientist', 'Graphic Designer', 'Project Manager',
    'Research Scientist', 'Marketing Manager', 'Technician', 'Business Analyst',
    'Sales Executive', 'DevOps Engineer', 'Content Writer', 'HR Manager',
    'Accountant', 'Machine Learning Engineer', 'UI/UX Designer', 'Product Manager',
    'QA Engineer', 'Electrician', 'Financial Analyst', 'Cloud Engineer'
]
industries = ['IT', 'Finance', 'Media', 'Construction', 'Healthcare', 'Retail',
              'Manufacturing', 'Consulting', 'Insurance', 'Utilities', 'Tech']
#countries = ['USA', 'UK', 'Canada', 'Australia', 'India', 'Germany', 'Brazil', 'South Africa']
work_modes = ['Remote', 'Onsite', 'Hybrid']
work_mode_weights = [0.3, 0.5, 0.2]  # realistic proportions

skills_dict = {
    'Software Engineer': ['Python', 'Java', 'Git'],
    'Data Scientist': ['Python', 'SQL', 'ML'],
    'Graphic Designer': ['Photoshop', 'Illustrator', 'InDesign'],
    'Project Manager': ['PM', 'MS Project', 'Excel'],
    'Research Scientist': ['R', 'Python', 'Data Analysis'],
    'Marketing Manager': ['SEO', 'SEM', 'Analytics'],
    'Technician': ['CNC', 'Maintenance', 'Safety'],
    'Business Analyst': ['Excel', 'SQL', 'Tableau'],
    'Sales Executive': ['CRM', 'Communication'],
    'DevOps Engineer': ['AWS', 'Docker', 'CI/CD'],
    'Content Writer': ['Writing', 'SEO', 'WordPress'],
    'HR Manager': ['HRM', 'Communication', 'Payroll'],
    'Accountant': ['Tally', 'Excel', 'Compliance'],
    'Machine Learning Engineer': ['ML', 'Deep Learning', 'Python'],
    'UI/UX Designer': ['Figma', 'XD', 'HTML/CSS'],
    'Product Manager': ['PM', 'Agile', 'JIRA'],
    'QA Engineer': ['Selenium', 'Python', 'Testing'],
    'Electrician': ['Wiring', 'Safety', 'Troubleshooting'],
    'Financial Analyst': ['Excel', 'Python', 'Valuation'],
    'Cloud Engineer': ['Azure', 'Python', 'Networking']
}

# Salary generation based on job and experience
def generate_salary(job, exp):
    base = {
        'Software Engineer': 60000,
        'Data Scientist': 70000,
        'Graphic Designer': 50000,
        'Project Manager': 75000,
        'Research Scientist': 85000,
        'Marketing Manager': 65000,
        'Technician': 40000,
        'Business Analyst': 60000,
        'Sales Executive': 50000,
        'DevOps Engineer': 80000,
        'Content Writer': 45000,
        'HR Manager': 65000,
        'Accountant': 55000,
        'Machine Learning Engineer': 90000,
        'UI/UX Designer': 60000,
        'Product Manager': 85000,
        'QA Engineer': 50000,
        'Electrician': 45000,
        'Financial Analyst': 65000,
        'Cloud Engineer': 90000
    }
    return int(base[job] + exp*random.uniform(1000,3000) + random.gauss(0,5000))

# Generate dataset
num_samples = 200
data = []

for _ in range(num_samples):
    age = random.randint(22, 60)
    edu = random.choices(education_levels, weights=[10, 15, 35, 30, 10])[0]
    job = random.choice(job_titles)
    exp = min(random.randint(0, age - 21), 40)
    industry = random.choice(industries)
    hours = random.randint(35, 50)
    #country = random.choice(countries)
    work_mode = random.choices(work_modes, weights=work_mode_weights)[0]
    skills = ", ".join(random.sample(skills_dict[job], k=random.randint(2, len(skills_dict[job]))))
    salary = generate_salary(job, exp)

    data.append([age, edu, job, exp, industry, hours, work_mode, skills, salary])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'Age', 'Education Level', 'Job Title', 'Experience (Years)', 'Industry',
    'Hours/Week', 'Work Mode', 'Skills', 'Salary (USD)'
])

# Save to CSV
df.to_csv('employee_salary_dataset.csv', index=False)
print()
print("Dataset saved as 'empl_dataset.csv'")