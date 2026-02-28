import pandas as pd
import os

data = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Arjun"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [75000, 60000, 82000, 90000, 65000],
    "JoiningDate": pd.to_datetime([
        "2021-06-15",
        "2020-09-23",
        "2019-01-10",
        "2022-03-01",
        "2021-11-19"
    ]),
    "PerformanceScore": [4.5, 3.8, 4.2, 4.9, 3.5]
}

# Create DataFrame
df = pd.DataFrame(data)

os.makedirs('data', exist_ok=True)
data_dir = os.path.join('data', 'data.csv')
print(df.head())

df.to_csv(data_dir, index=False)    
print(f"Data saved to {data_dir}")

