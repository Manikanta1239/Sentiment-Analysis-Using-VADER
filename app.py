from flask import Flask, request, render_template
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import re
from string import punctuation

# Download NLTK stopwords
nltk.download('stopwords')

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    # Load stopwords for filtering
    stop_words = set(stopwords.words('english'))

    # Retrieve input text and preprocess it
    text1 = request.form['text1']
    text_lower = text1.lower()
    text_no_digits = re.sub(r'\d+', '', text_lower)  # Remove digits
    text_no_punct = re.sub(r'[^\w\s]', '', text_no_digits)  # Remove punctuation
    text_clean = ' '.join([word for word in text_no_punct.split() if word not in stop_words])  # Remove stopwords

    # Initialize sentiment analysis
    sa = SentimentIntensityAnalyzer()
    sentiment_scores = sa.polarity_scores(text_clean)

    # Determine dominant sentiment
    compound_score = round((1 + sentiment_scores['compound']) / 2, 2)  # Normalize compound score to [0, 1]
    if sentiment_scores['compound'] >= 0.05:
        sentiment = "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Render the template with sentiment analysis results
    return render_template(
        'form.html',
        final=compound_score,
        input_text=text1,  # Original user input
        cleaned_text=text_clean,  # Preprocessed text
        positive_score=sentiment_scores['pos'],
        neutral_score=sentiment_scores['neu'],
        negative_score=sentiment_scores['neg'],
        compound_score=sentiment_scores['compound'],
        sentiment=sentiment
    )

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)
