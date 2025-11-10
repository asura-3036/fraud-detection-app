#Fraud Detection Project
Overview
This project implements a machine learning-based fraud detection system to identify fraudulent financial transactions. The system is built using Python with key libraries like pandas, scikit-learn, and Streamlit. It processes a real-world transaction dataset, extracts relevant features, and trains a logistic regression model to classify transactions as legitimate or fraudulent.

Dataset
The dataset used consists of transaction records with multiple features including transaction type, amounts, and balances before and after transactions. The data is preprocessed to handle missing values and engineered features that improve model performance.

Methodology
Data Loading and Exploration: Initial understanding of the dataset through summary statistics and visualization.

Feature Engineering: Creation of new features such as balance differences to enhance predictive power.

Data Preprocessing: Scaling numerical data and encoding categorical variables.

Model Training: A logistic regression classifier is trained with balanced class weights to address class imbalance.

Model Evaluation: Performance is assessed using classification reports and confusion matrices to measure precision, recall, and accuracy.

Application
The project includes a Streamlit web app that allows users to input transaction details interactively and receive immediate fraud predictions based on the trained model. This demonstrates practical model deployment and real-time prediction capabilities.

Benefits
Enables early detection of fraudulent activities in transaction datasets.

Illustrates end-to-end machine learning workflow from data processing to deployment.

Provides visualization insights into transaction types and fraud rates.

This repository is ideal for those interested in financial fraud detection, applied machine learning workflows, and interactive model deployment.
