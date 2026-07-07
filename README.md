# 📧 Email Spam Detection using Multinomial Naive Bayes

## 📖 Project Overview

This project was developed as part of the **COM763 – Advanced Machine Learning** module.

The objective of this project is to develop an intelligent email spam detection system capable of classifying emails as **Spam** or **Ham (Not Spam)** using the **Multinomial Naive Bayes** machine learning algorithm. The system performs text preprocessing, feature extraction using TF-IDF, model training, evaluation, and provides a user-friendly web application developed with Streamlit.

---

## 🎯 Objectives

- Develop an email spam classification model.
- Perform text preprocessing using Natural Language Processing (NLP).
- Convert text into numerical features using TF-IDF.
- Train a Multinomial Naive Bayes classifier.
- Evaluate model performance using standard classification metrics.
- Deploy the trained model as a Streamlit web application.

---

## 📂 Dataset

**Dataset:** Email Spam Dataset

The dataset contains two columns:

| Column | Description |
|---------|-------------|
| Category | Spam or Ham label |
| Message | Email message content |

---

## 🛠 Technologies Used

- Python 3.12
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Matplotlib
- Seaborn
- Joblib

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Text Preprocessing
5. TF-IDF Feature Extraction
6. Model Training (Multinomial Naive Bayes)
7. Model Evaluation
8. Model Deployment using Streamlit

---

## 📊 Model Evaluation

The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

---

## 📁 Project Structure

```
ML-Student-Project/
│
├── app.py
├── Student_Project.ipynb
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## 🚀 Running the Project

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📷 Application Features

- Predict whether an email is Spam or Ham
- Text preprocessing using NLP
- TF-IDF feature extraction
- Machine learning prediction
- Interactive Streamlit web interface

---

## 👨‍🎓 Student Information

**Student Name:** Kosala Ranathunga

**Module:** COM763 – Advanced Machine Learning

**Project:** Email Spam Detection using Multinomial Naive Bayes

---
## Application Interface

![Application](images/home.png)

## 📄 License

This project is developed for academic purposes as part of the MSc coursework submission.