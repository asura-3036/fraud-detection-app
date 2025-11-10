Fraud Detection System

Overview

This project implements a machine learning-based fraud detection system designed to identify suspicious financial transactions. Utilizing Python and libraries such as pandas, scikit-learn, Matplotlib, and Streamlit, the system processes transaction data, extracts critical features, trains a classification model, and provides an interactive prediction interface.

Dataset Description

The dataset comprises transaction records with features like transaction type, transaction amount, balances before and after transactions, and a label indicating whether the transaction is fraudulent or legitimate. It contains highly imbalanced data, with very few fraud cases compared to genuine transactions, reflecting real-world scenarios.​

Methodology

Data Loading & Exploration: Initial data analysis including summary statistics, null-value checks, and visualizations of feature distributions such as transaction amounts and times.

Feature Engineering: Derivation of new features like balances differences to improve model accuracy.

Preprocessing: Scaling numerical variables and encoding categorical features for effective modeling.

Model Training: Utilization of Logistic Regression with class weights to mitigate imbalance, followed by model training on the processed dataset.

Evaluation: Performance metrics including classification reports and confusion matrices assess model reliability, emphasizing precision and recall for fraud detection.

Deployment & Application

The project features a web app built with Streamlit, enabling users to input transaction data interactively and receive real-time fraud predictions. This demonstrates practical deployment of machine learning models for fraud monitoring in financial systems.​​

Benefits

Facilitates early fraud detection, reducing financial risks.

Demonstrates an end-to-end machine learning pipeline, from data handling to deployment.

Offers visualization tools for insightful analysis of transaction patterns and fraud prevalence.

Applicable in banking, insurance, and other sectors dealing with financial transactions.

Usage

Users can clone the repository, set up the environment, and run the Streamlit app to perform live fraud detection predictions on custom input data.

