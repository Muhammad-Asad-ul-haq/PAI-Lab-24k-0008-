import pandas as pd

df = pd.read_excel("employee.xlsx")
df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])
df["Year"] = df["JoiningDate"].dt.year
year = int(input("Enter the year to find employees: "))
employees_in_year = df[df["Year"] == year]
print(f"\nEmployees who joined in {year}:")
print(employees_in_year)
