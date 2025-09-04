# Titanic Exploratory Data Analysis (EDA)

This project performs **Exploratory Data Analysis** on the Titanic dataset to understand passenger demographics, survival statistics, and relationships between features.

---

## Dataset

- Source: [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)  
- Contains 891 rows and 12 columns:  
  - `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin`, `Embarked`

---

## Features

- **Data Cleaning**  
  - Fill missing `Age` values with median  
  - Fill missing `Embarked` values with mode  
  - Drop `Cabin` column (too many missing values)

- **Summary Statistics**  
  - Count, mean, standard deviation, min, max, and percentiles for numeric columns

- **Visualizations**  
  - Survival count  
  - Survival by passenger class  
  - Age distribution  
  - Survival by gender  

All charts are saved in the `outputs/` folder.

---

## How to Run

1. Clone the repository:  
   ```bash
   git clone https://github.com/Kanan066/SCT_DS_TASK2.git
