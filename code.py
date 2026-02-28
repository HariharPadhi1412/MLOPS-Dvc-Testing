import pandas as pd
import os

data = pd.read_csv(os.path.join('data', 'data.csv'))

df = pd.DataFrame(data)

os.makedirs('data', exist_ok=True)
data_dir = os.path.join('data', 'data.csv')
print(df.head())

df.to_csv(data_dir, index=False)    
print(f"Data saved to {data_dir}")

