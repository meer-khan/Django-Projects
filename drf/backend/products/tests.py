
# Create your tests here.
from email import header
import pandas as pd 


file = pd.read_csv(r'C:\Users\Hanzalah\Downloads\jan.csv' , header=None)

# print(file)

user = file.iloc[0]

print(user)