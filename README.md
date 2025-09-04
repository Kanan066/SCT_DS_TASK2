# Titanic Exploratory Data Analysis (EDA) 🚢

A **comprehensive Exploratory Data Analysis (EDA)** on the Titanic dataset, designed to uncover insights about passenger demographics, survival patterns, and relationships between features using Python, Pandas, Seaborn, and Matplotlib.

---

## 📊 Project Overview

This project analyzes the Titanic dataset to answer key questions like:

- How many passengers survived vs. perished?  
- Did passenger class (`Pclass`) affect survival?  
- How does age distribution relate to survival?  
- Are there differences in survival rates between genders?

---

## 🗂 Dataset

- **Source:** [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)  
- **Rows:** 891  
- **Columns:** 12  
  - `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin`, `Embarked`  

> Missing values in `Age` and `Embarked` were handled, and `Cabin` was dropped due to excessive missing data.

---

## 🔧 Key Features & Cleaning Steps

- **Data Cleaning**  
  - Fill missing `Age` values with median  
  - Fill missing `Embarked` values with mode  
  - Drop `Cabin` column  

- **Summary Statistics**  
  - Count, mean, standard deviation, min, max, quartiles for numeric features  

- **Visualizations**  
  - Survival Count  
  - Survival by Passenger Class  
  - Age Distribution  
  - Survival by Gender  

All plots are saved automatically in the `outputs/` folder.

---

## 📂 Folder Structure

m/Kanan066/SCT_DS_TASK2.git

## 🚀 How to Run

1. Clone the repository:


git clone https://github.com/Kanan066/SCT_DS_TASK2.git
cd SCT_DS_TASK2

🖋 Author

Kanan Sadiora
GitHub: https://github.com/Kanan066

LinkedIn: https://www.linkedin.com/in/kanan-sadiora-37a819331/
