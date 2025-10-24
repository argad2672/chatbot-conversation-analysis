import streamlit as st
import joblib
import re, string
from nltk.corpus import stopwords

# --- Load the saved model and vectorizer ---
svc_model = joblib.load("models/intent_recognition_model_svc.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# --- Setup stopwords ---
stop_words = set(stopwords.words('english'))

# --- Cleaning function ---
def clean_text(text):
    text = str(text).lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# --- Mapping clusters to intent names ---
cluster_labels = {
    0: "Multilingual / General Requests",
    1: "Technical or Logical Questions",
    2: "Greetings & General Conversation",
    3: "Personal or Emotional Chat",
    4: "Thanks & Closing Messages"
}

# --- Streamlit App UI ---
st.set_page_config(page_title="Chatbot Intent Classifier", page_icon="🤖", layout="centered")
st.title("🤖 Chatbot Intent Recognition App")
st.write("Type a message below to predict its intent:")

# --- Input ---
user_input = st.text_area("Enter your message:", height=120)

if st.button("Predict Intent"):
    if user_input.strip():
        # Clean and vectorize
        cleaned = clean_text(user_input)
        X_new = vectorizer.transform([cleaned])
        
        # Predict
        cluster = svc_model.predict(X_new)[0]
        intent = cluster_labels.get(cluster, "Unknown")
        
        # Display result
        st.success(f"**Predicted Intent:** {intent}")
        st.info(f"(Cluster {cluster})")
    else:
        st.warning("Please type a message before predicting.")
