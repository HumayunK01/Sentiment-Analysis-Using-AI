from flask import Flask, render_template, request
from sentiment_analysis import analyze_sentiment  # Assuming sentiment analysis function is implemented in sentiment_analysis.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_sentiment(text)
        return render_template('result.html', text=text, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
