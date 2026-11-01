# Digital Marketing Campaign Conversion Prediction

## Project Overview

This project focuses on predicting whether a customer is likely to convert after being exposed to a digital marketing campaign.

The project combines customer demographics, campaign information, advertising spend, website engagement, email engagement, previous purchases, and loyalty information to build a machine learning model for conversion prediction.

The main objective is to help marketing teams improve customer targeting, identify potentially valuable customers, and make better use of marketing resources.

---

## Business Problem

Digital marketing campaigns generate large amounts of customer and engagement data. However, not every customer exposed to a campaign will convert.

A marketing team can benefit from identifying customers who have a higher likelihood of conversion so that campaigns and follow-up activities can be targeted more effectively.

This project addresses the following business question:

> **Can customer demographic, campaign, engagement, and spending information be used to predict customer conversion?**

---

## Project Objectives

The major objectives of this project are:

- Analyze customer and campaign characteristics.
- Understand factors associated with customer conversion.
- Perform data cleaning and exploratory data analysis.
- Analyze the data using SQL.
- Perform statistical significance testing.
- Build and compare multiple machine learning models.
- Tune the best-performing model.
- Compare the final machine learning model with a neural network.
- Develop a Power BI dashboard for business analysis.
- Build a Streamlit application for individual customer conversion prediction.
- Provide business-oriented interpretation of model results.

---

## Dataset

The dataset contains 8,000 customer campaign records.

The major variables include:

- CustomerID
- Age
- Gender
- Income
- CampaignChannel
- CampaignType
- AdSpend
- ClickThroughRate
- ConversionRate
- WebsiteVisits
- PagesPerVisit
- TimeOnSite
- SocialShares
- EmailOpens
- EmailClicks
- PreviousPurchases
- LoyaltyPoints
- Conversion
- AdvertisingPlatform
- AdvertisingTool

The target variable is:

**Conversion**

where:

- `1` = Customer converted
- `0` = Customer did not convert

---

## Project Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
SQL Business Analysis
     ↓
Statistical Testing
     ↓
Machine Learning
     ↓
Model Comparison
     ↓
XGBoost Hyperparameter Tuning
     ↓
Neural Network Comparison
     ↓
Power BI Dashboard
     ↓
Streamlit Prediction Application
```

---

## Data Preparation

The dataset was inspected for:

- Missing values
- Duplicate records
- Data types
- Numerical distributions
- Categorical distributions
- Target class distribution
- Outliers and unusual values

Additional engineered features were created:

### EmailClickRate

```text
EmailClickRate = EmailClicks / (EmailOpens + 1)
```

This represents email click activity relative to email opens.

### SpendPerVisit

```text
SpendPerVisit = AdSpend / (WebsiteVisits + 1)
```

This provides a simple measure of advertising spend relative to website activity.

The `+1` prevents division by zero when a customer has no website visits or email opens.

---

## Exploratory Data Analysis

EDA was performed using Python libraries including:

- Pandas
- NumPy
- Matplotlib
- Seaborn

The analysis examined:

- Conversion distribution
- Numerical feature distributions
- Categorical feature distributions
- Feature relationships with conversion
- Correlation between numerical variables
- Conversion rates across campaign channels
- Conversion rates across campaign types
- Customer demographic patterns

---

## SQL Analysis

MySQL was used to perform business-oriented analysis.

Examples of SQL analysis include:

- Conversion rate by campaign channel
- Conversion rate by campaign type
- Customer distribution by age group
- Advertising spend analysis
- Campaign cost and conversion analysis

The SQL analysis was used to translate the dataset into business-focused insights rather than relying only on machine learning.

---

## Statistical Analysis

Statistical tests were performed to determine whether selected variables showed statistically significant relationships with conversion.

Numerical variables were evaluated using statistical comparison tests, while categorical variables were evaluated using chi-square tests.

The analysis found that several engagement and campaign-related variables showed statistically significant relationships with conversion, while variables such as Gender, Age, Income, and SocialShares were not statistically significant in the tested comparisons.

Statistical significance indicates an observed relationship in the analyzed data; it does not by itself prove that a variable causes conversion.

---

## Machine Learning

Several classification algorithms were evaluated.

The models included:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- K-Nearest Neighbors
- Naive Bayes
- Dummy Classifier

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Because the target variable was imbalanced, F1-related metrics and ROC-AUC were considered in addition to accuracy.

---

## Model Comparison

The initial model comparison produced the following results:

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| XGBoost | 0.9175 | 0.9205 | 0.9914 | 0.9547 | 0.8204 |
| Gradient Boosting | 0.9119 | 0.9140 | 0.9929 | 0.9518 | 0.8144 |
| Random Forest | 0.8906 | 0.8915 | 0.9964 | 0.9411 | 0.8125 |
| Logistic Regression | 0.8900 | 0.8935 | 0.9929 | 0.9405 | 0.7857 |
| Naive Bayes | 0.8894 | 0.8924 | 0.9936 | 0.9403 | 0.7872 |
| KNN | 0.8781 | 0.8837 | 0.9914 | 0.9345 | 0.6514 |
| Dummy Classifier | 0.8762 | 0.8762 | 1.0000 | 0.9340 | 0.5000 |
| Decision Tree | 0.8706 | 0.9051 | 0.9522 | 0.9281 | 0.6828 |

XGBoost produced the strongest overall F1 Score among the evaluated models.

---

## XGBoost Hyperparameter Tuning

The XGBoost model was tuned using cross-validation.

The selected parameters were:

```text
learning_rate = 0.1
max_depth = 3
n_estimators = 200
```

The cross-validation F1 macro score improved from approximately:

```text
0.7503
```

to:

```text
0.7695
```

---

## Final XGBoost Performance

The tuned model achieved the following test-set results:

| Metric | Score |
|---|---:|
| Accuracy | 0.9219 |
| Precision | 0.9237 |
| Recall | 0.9929 |
| F1 Score | 0.9570 |
| F1 Macro | 0.7637 |
| ROC-AUC | 0.8171 |
| Average Precision | 0.9494 |

The model showed very strong performance for identifying converted customers.

However, the minority class was harder to identify. Therefore, accuracy alone should not be used to judge the model.

---

## Neural Network Comparison

A neural network model was also evaluated as an additional comparison.

| Model | F1 Macro | ROC-AUC |
|---|---:|---:|
| XGBoost | 0.7637 | 0.8171 |
| Neural Network | 0.6400 | 0.7710 |

XGBoost performed better on the selected evaluation metrics, so XGBoost was retained as the final model.

---

## Important Features

The model identified several features as important for prediction.

Important variables included:

- PreviousPurchases
- EmailClicks
- CampaignType
- EmailOpens
- TimeOnSite
- PagesPerVisit
- WebsiteVisits
- ConversionRate
- ClickThroughRate
- AdSpend
- LoyaltyPoints
- EmailClickRate

Feature importance indicates which variables contributed to the model's predictions. It should not be interpreted as proof that these variables independently cause customer conversion.

---

## Power BI Dashboard

A three-page Power BI dashboard was developed.

### Page 1 — Executive Overview

The dashboard provides:

- Total Customers
- Total Conversions
- Overall Conversion Rate
- Total Ad Spend
- Conversion rate by campaign channel
- Conversion rate by campaign type
- Conversion rate by age group

### Page 2 — Customer & Campaign Analysis

This page focuses on:

- Customer demographics
- Gender analysis
- Age analysis
- Campaign performance
- Advertising spend
- Email engagement
- Campaign filtering

### Page 3 — Model Performance & Prediction

This page presents:

- Model comparison
- Final XGBoost metrics
- Confusion matrix
- Important prediction features

---

## Streamlit Application

A Streamlit application was developed to allow users to enter an individual customer and campaign profile and receive a conversion prediction.

The application accepts:

- Age
- Gender
- Income
- Campaign Channel
- Campaign Type
- Ad Spend
- Click Through Rate
- Conversion Rate
- Website Visits
- Pages Per Visit
- Time On Site
- Social Shares
- Email Opens
- Email Clicks
- Previous Purchases
- Loyalty Points

The application automatically calculates:

```text
EmailClickRate
SpendPerVisit
```

The saved machine learning pipeline then performs:

```text
StandardScaler
        +
OneHotEncoder
        ↓
XGBoost
        ↓
Conversion Prediction
```

The application displays:

- Predicted conversion status
- Estimated conversion probability
- Business interpretation
- Calculated features
- Customer input

---

## Project Structure

```text
Capstone_Marketing/
│
├── Capstone_Marketing_Conversion.ipynb
│
├── data/
│   └── digital_marketing_campaign_dataset.csv
│
├── outputs/
│   ├── model_comparison.csv
│   ├── final_model_metrics.csv
│   ├── feature_importance.csv
│   ├── statistical_tests.csv
│   └── visualization files
│
├── models/
│   └── conversion_model.pkl
│
├── dashboard/
│   └── Marketing_Conversion_Dashboard.pbix
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── report/
│   └── ai_summary.txt
│
├── .gitignore
└── README.md
```

---

## Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn
- Power BI

### Database

- MySQL

### Machine Learning

- Scikit-learn
- XGBoost

### Application Development

- Streamlit

### Development Environment

- Jupyter Notebook
- Anaconda

### Version Control

- Git
- GitHub

---

## How to Run the Streamlit Application

Create and activate the project environment:

```bash
conda activate marketing_project
```

Navigate to the project directory:

```bash
cd Documents\Capstone_Marketing
```

Install the required packages:

```bash
pip install -r app\requirements.txt
```

Run the application:

```bash
streamlit run app\app.py
```

The application will open in the browser.

---

## Business Value

The project demonstrates how digital marketing data can be used to support:

- Customer targeting
- Campaign analysis
- Conversion prediction
- Marketing resource allocation
- Customer engagement analysis
- Data-driven campaign decisions

The prediction application can serve as a simple decision-support tool for evaluating individual customer profiles.

---

## Limitations

The model is based on historical campaign data and should not be interpreted as proof of causal relationships.

The target variable is imbalanced, which makes minority-class prediction more difficult.

Model probability estimates should also be interpreted carefully and should not automatically be treated as perfectly calibrated real-world probabilities.

Actual campaign performance can be affected by factors that are not represented in the dataset, including future customer behavior, campaign execution, market conditions, and changes in marketing strategy.

---

## Conclusion

This project demonstrates an end-to-end digital marketing analytics and machine learning workflow, starting from raw customer campaign data and progressing through data analysis, SQL, statistical testing, machine learning, model tuning, visualization, and deployment through a Streamlit application.

The final XGBoost model provided the strongest overall performance among the evaluated machine learning approaches and was integrated into a user-facing prediction application.

The project combines technical machine learning work with business-oriented analysis to demonstrate how data can support digital marketing decision-making.