import streamlit as st
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
from collections import Counter

# Initialize NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Streamlit app
def main():
    st.title("Sentiment Analysis from Text File")
    
    st.write("Upload a text file to analyze emotions based on a sentiment word list.")
    
    # File upload functionality
    uploaded_file = st.file_uploader("Choose a file", type=["txt"])
    
    if uploaded_file is not None:
        # Read the uploaded text file
        text = uploaded_file.read().decode('utf-8')
        
        # Text processing
        lower_case = text.lower()
        cleaned_text = lower_case.translate(str.maketrans(' ', ' ', string.punctuation))

        # Tokenize the cleaned text
        tokenized_words = word_tokenize(cleaned_text, "english")

        # Remove stopwords
        final_words = [word for word in tokenized_words if word not in stopwords.words('english')]

        # Read sentiment word list
        emotion_list = []
        try:
            with open('sentiment.txt', 'r') as file:
                for line in file:
                    clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                    word, emotion = clear_line.split(':')
                    
                    # If the word is in the cleaned text, append the emotion
                    if word in final_words:
                        emotion_list.append(emotion)
        except FileNotFoundError:
            st.error("The sentiment.txt file was not found.")
            return

        # Count the occurrences of each emotion
        W = Counter(emotion_list)

        # Display the emotion frequencies
        if W:
            st.write("Emotion frequencies found in the text:")
            st.write(W)

            # Plot a bar chart of the emotion frequencies
            fig, ax1 = plt.subplots()
            ax1.bar(W.keys(), W.values())
            plt.xlabel('Emotion')
            plt.ylabel('Frequency')
            plt.title('Emotion Frequency Analysis')
            st.pyplot(fig)
        else:
            st.write("No emotions found in the text.")

# Run the app
if __name__ == '__main__':
    main()
