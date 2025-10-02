from flask import Flask, render_template, request, jsonify
from sentiment_model import analyze_sentiment, get_tweet_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        result = analyze_sentiment(text)
        return render_template('results.html', text=text, result=result)

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.json
    if 'text' in data:
        text = data['text']
        result = analyze_sentiment(text)
        return jsonify({'text': text, 'result': result})
    return jsonify({'error': 'No text provided'}), 400

@app.route('/tweets', methods=['GET'])
def fetch_tweets():
    keyword = request.args.get('keyword', 'Python')  # Default to 'Python' if no keyword is provided
    tweet_texts = get_tweet_text(keyword)
    sentiment_results = [analyze_sentiment(text) for text in tweet_texts]
    return render_template('tweets.html', keyword=keyword, tweets=tweet_texts, sentiments=sentiment_results)

if __name__ == '__main__':
    app.run(debug=True)
