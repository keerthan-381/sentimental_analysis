# Sentiment Analysis App

This repository contains a simple sentiment analysis application built using Streamlit. The app analyzes the emotions present in a text file based on a predefined sentiment word list.

## Features

- Upload a text file (.txt format) for sentiment analysis.
- Clean and tokenize the text data.
- Remove common English stopwords.
- Identify emotions in the text using a predefined sentiment word list (`sentiment.txt`).
- Display the frequency of emotions in the text.
- Visualize the results using a bar chart.

## Files in the Repository

### 1. **`app.sentiment.py`**

The main application file containing the Streamlit app logic. It:

- Processes the uploaded text file.
- Cleans and tokenizes the text.
- Identifies and counts emotions based on the `sentiment.txt` file.
- Visualizes the emotion frequencies.

### 2. **`sentiment.txt`**

A sentiment word list file containing word-emotion mappings in the format:

```
word1:emotion1
word2:emotion2
...
```

This file is used to match words from the uploaded text with corresponding emotions.

### 3. **`hello.txt`**

A sample text file for testing the application. You can upload this file to the app to see how it works.

### 4. **`requirements.txt`**

A file listing the Python dependencies required to run the app. Install these dependencies using:

```bash
pip install -r requirements.txt
```

## Installation and Setup

1. Clone this repository to your local machine:
   ```bash
   git clone git@github.com:keerthan-381/sentimental_analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd sentimental_analysis
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Run the Streamlit app:
   ```bash
   streamlit run app.sentiment.py
   ```
2. Open your web browser and go to the URL displayed in the terminal.
3. Upload a text file to analyze emotions.

## How It Works

1. Upload a `.txt` file via the Streamlit interface.
2. The app reads and preprocesses the text by:
   - Converting it to lowercase.
   - Removing punctuation.
   - Tokenizing the text.
   - Removing common English stopwords.
3. It then matches words in the text against the word-emotion mappings in `sentiment.txt`.
4. Counts and displays the frequency of each emotion.
5. A bar chart is displayed to visualize the emotion distribution.

## Dependencies

- Python 3.7+
- Streamlit
- NLTK
- Matplotlib

You can install all dependencies using the `requirements.txt` file.

## Troubleshooting

- Ensure that `sentiment.txt` is present in the same directory as `app.sentiment.py`.
- If you encounter missing NLTK resources, run the following commands in your Python environment:
  ```python
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  ```
  
## Acknowledgments

- [Streamlit](https://streamlit.io/) for building interactive web apps.
- [NLTK](https://www.nltk.org/) for natural language processing.

The app is accessible online at: [Sentiment Analysis App](https://sentimentalanalysis-1.streamlit.app/).
