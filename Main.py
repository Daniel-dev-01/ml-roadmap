import  pandas as pd
import matplotlib.pyplot as plt

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

#1. Churn Distribution

df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of customers")
plt.show()

#2. Tenure Distribution
df["tenure"].plot(kind="hist",bins=20)
plt.title("Customer tenure Distribution")
plt.xlabel("Tenure(months)")
plt.ylabel("Number of customers")
plt.show()

# 3. Monthly Charges by Churn
df.boxplot(column='MonthlyCharges', by='Churn')
plt.title('Monthly Charges by Churn')
plt.suptitle('')
plt.xlabel('Churn')
plt.ylabel('Monthly Charges')
plt.show()

# 4. Churn by Contract Type
pd.crosstab(df['Contract'], df['Churn']).plot(kind='bar')
plt.title('Churn by Contract Type')
plt.xlabel('Contract Type')
plt.xticks(rotation=0)
plt.ylabel('Number of Customers')
plt.show()

