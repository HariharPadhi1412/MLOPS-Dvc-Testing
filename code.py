import pandas as pd
import os

data = {
    "EmployeeID": [101, 102, 103, 104, 105,106, 107, 108, 109, 110],
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Arjun", "Priya", "Vikram", "Anjali", "Raj", "Sunita"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing", "Finance", "HR", "IT", "Marketing", "Finance"],
    "Salary": [75000, 60000, 82000, 90000, 65000, 78000, 62000, 85000, 72000, 79500],
    "JoiningDate": pd.to_datetime([
        "2021-06-15",
        "2020-09-23",
        "2019-01-10",
        "2022-03-01",
        "2021-11-19",
        "2020-05-30",
        "2018-07-12",
        "2021-02-20",
        "2019-10-05",
        "2020-12-01"
    ]),
    "PerformanceScore": [4.5, 3.8, 4.2, 4.9, 3.5, 4.0, 3.7, 4.6, 3.9, 4.1]
}

# Create DataFrame
df = pd.DataFrame(data)

os.makedirs('data', exist_ok=True)
data_dir = os.path.join('data', 'data.csv')
print(df.head())

df.to_csv(data_dir, index=False)    
print(f"Data saved to {data_dir}")

