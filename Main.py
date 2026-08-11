import  pandas as pd

df = pd. read_csv("data.csv")

df['SeniorCitizen'] = df['SeniorCitizen'].astype(bool)

print(df['SeniorCitizen'].head())
print(df['SeniorCitizen'].dtype)

df['Churn'] = df['Churn'].map({'Yes': True, 'No': False})

print(df['Churn'].head())
print(df['Churn'].dtype)

print(df)

print(df.info())
print(df.isnull().sum())

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
print(df['TotalCharges'].isnull().sum())

print(df[df['TotalCharges'].isnull()][['tenure', 'MonthlyCharges', 'TotalCharges']])

df['TotalCharges'] = df['TotalCharges'].fillna(0)

print(df['TotalCharges'].isnull().sum())

print(df.duplicated().sum())
print(df['OnlineSecurity'].value_counts())

cols = ["OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies"]
df[cols] = df[cols].replace({"No internet service": "No"})

print(df["DeviceProtection"].value_counts())
