import streamlit as st
from textblob import TextBlob

# Page Configuration
st.set_page_config(page_title="Chota AI Tool", page_icon="🤖", layout="centered")

# App Header
st.title("🤖 Quick AI Text Tools")
st.write("Apna bada paragraph niche paste karo, AI usko summarize bhi karega aur mood (Sentiment) bhi batayega!")

# User Input
user_text = st.text_area("Enter Text Here:", height=150)

if st.button("Analyze with AI"):
    if user_text.strip() != "":
        blob = TextBlob(user_text)
        
        # 1. AI Sentiment Analysis
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😡"
        else:
            sentiment = "Neutral 😐"
            
        # 2. Quick AI Summary (Extracting key sentences)
        sentences = blob.sentences
        summary = " ".join([str(s) for s in sentences[:2]])
        
        # Display Results
        st.write("---")
        st.subheader("📊 Results:")
        
        st.metric(label="Text Mood / Sentiment", value=sentiment)
        
        st.subheader("📝 Short Summary:")
        st.info(summary if summary else "Text bahut chota hai summarize karne ke liye.")
        
    else:
        st.error("Please kuch text enter kijiye!")
      
