# ==========================================================
# COM763 - Advanced Machine Learning
# Email Spam Detection using Multinomial Naive Bayes
# ==========================================================

import streamlit as st
import joblib
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK resources
import nltk

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load trained model
model = joblib.load("model.pkl")

# Load TF-IDF Vectorizer
vectorizer = joblib.load("vectorizer.pkl")

# Create Porter Stemmer
ps = PorterStemmer()
# ==========================================================
# Text Preprocessing Function
# ==========================================================

def transform_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Tokenize words
    text = nltk.word_tokenize(text)

    y = []

    # Keep only letters and numbers
    for word in text:
        if word.isalnum():
            y.append(word)

    text = y[:]
    y.clear()

    # Remove stopwords and punctuation
    for word in text:
        if word not in stopwords.words('english') and word not in string.punctuation:
            y.append(word)

    text = y[:]
    y.clear()

    # Apply stemming
    for word in text:
        y.append(ps.stem(word))

    return " ".join(y)
# ==========================================================
# Streamlit User Interface
# ==========================================================

st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧"
)

st.title("📧 Email Spam Detection System")

st.write("This application predicts whether an email is Spam or Ham using a Multinomial Naive Bayes model.")

email = st.text_area(
    "Enter your email message below:",
    height=200
)
# ==========================================================
# Prediction
# ==========================================================

if st.button("Predict"):

    if email.strip() == "":
        st.warning("Please enter an email message.")

    else:

        # Clean the text
        transformed_email = transform_text(email)

        # Convert text into TF-IDF features
        vector_input = vectorizer.transform([transformed_email])

        # Predict
        prediction = model.predict(vector_input)[0]

        # Display result
        if prediction == 1:
            st.error("🚨 Spam Email")
        else:
            st.success("✅ Not Spam (Ham Email)")
            
# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("About")

st.sidebar.info("""
**COM763 - Advanced Machine Learning**

**Project:**
Email Spam Detection using Multinomial Naive Bayes

**Student Name:** Kosala Ranathunga
                
**Student ID:** S25021954

This application predicts whether an email is Spam or Ham using Machine Learning.
""")