# titanic_eda.py
import os

# Ensure the outputs folder exists
os.makedirs("outputs", exist_ok=True)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("datasets/titanic/train.csv")

# Preview data
print("First 5 rows:")
print(df.head())

print("\nData info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Fill missing values (simple cleaning)
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)  # drop Cabin (too many missing)

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Exploratory plots
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.savefig("outputs/survival_count.png")
plt.clf()

sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.savefig("outputs/survival_by_class.png")
plt.clf()

sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.savefig("outputs/age_distribution.png")
plt.clf()

sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.savefig("outputs/survival_by_gender.png")
plt.clf()

print("\nEDA complete. Charts saved in 'outputs/' folder.")
