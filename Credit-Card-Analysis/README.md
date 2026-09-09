# 💳 Credit Card Fraud Detection & Transaction Time Analysis

## 📌 Project Overview
This project analyzes **1,000,000 credit card transactions** to identify fraud patterns and understand transaction behavior.

The analysis was performed using Python, Pandas, Matplotlib, Seaborn, and Scikit-learn.

A transaction-time feature was also added to study fraud and transaction activity by hour and time period.

## 🎯 Objectives
- Analyze genuine vs fraudulent transactions
- Calculate total fraud transactions and fraud percentage
- Analyze transaction behavior and purchase-price ratios
- Study transaction activity by hour
- Identify the peak fraud hour and busiest transaction hour
- Check missing values and duplicate records
- Analyze class imbalance
- Explore feature correlations
- Build and compare machine-learning models for fraud detection

## 📊 Dataset
The dataset contains **1,000,000 records**.

### Main Features
- `distance_from_home`
- `distance_from_last_transaction`
- `ratio_to_median_purchase_price`
- `repeat_retailer`
- `used_chip`
- `used_pin_number`
- `online_order`
- `fraud`

Additional time-analysis features:
- `Hour`
- `Transaction_Time`
- `Minute`
- `Second`
- `Time_Period`

## 🔎 Key Findings
- Total transactions: **1,000,000**
- Fraudulent transactions: **87,403**
- Fraud percentage: **8.7403%**
- Genuine transactions: **912,597 (91.2597%)**
- No missing values were found.
- No duplicate rows were found.
- Average transaction ratio: **1.8242**
- Median transaction ratio: **0.9977**
- Peak fraud hour by fraud count: **12:00**
- Busiest transaction hour: **15:00**

## 🤖 Machine Learning
The project explored multiple classification approaches:

| Model | Accuracy |
|---|---:|
| Logistic Regression | 95.94% |
| Decision Tree | 99.9985% |
| Random Forest | 99.9975% |
| KNN | 99.551% |

Class imbalance was also investigated, and oversampling was used during model training.

> Note: Accuracy alone should not be used to judge a fraud-detection model. Precision, recall, F1-score and the confusion matrix are also important, especially for the minority fraud class.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## 📁 Project Files
```text
credit-card-fraud-analysis/
│
├── Credit_card_Analysis.ipynb
├── card_transaction_time_analysis.ipynb
├── README.md
└── .gitignore
```

## 📈 Analysis Covered
1. Data loading and inspection
2. Exploratory Data Analysis (EDA)
3. Data quality checks
4. Fraud analysis
5. Transaction amount/ratio analysis
6. Time-based transaction analysis
7. Outlier analysis
8. Correlation analysis
9. Class imbalance analysis
10. Model training and evaluation
11. Model comparison

## 🚀 How to Run
1. Install Python.
2. Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

3. Open Jupyter Notebook:

```bash
jupyter notebook
```

4. Open either notebook and run the cells in order.

## 👨‍💻 Author
**Abdulsamad Mulla**

Aspiring Data Analyst | Python | SQL | Excel | Power BI

---

⭐ If you find this project useful, feel free to star the repository!
