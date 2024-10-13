from flask import Flask, jsonify, request, abort
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the News Aggregator API!"

@app.route('/articles', methods=['GET'])
def get_articles():
    try:
        df = pd.read_csv('news_articles.csv', encoding='ISO-8859-1')  # Ensure the correct encoding
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
        df = pd.read_csv('news_articles.csv', encoding='ISO-8859-1')
        if 'id' in df.columns:
            if id in df['id'].values:
                article = df[df['id'] == id].iloc[0].to_dict()
                return jsonify(article)
            else:
                print("Article not found")
                abort(404, description="Article not found")

        else:
            print("ID column not found in the dataset")
            abort(500, description="ID column not found in the dataset")
        
# Load the articles from the CSV file
df = pd.read_csv('news_articles.csv')

# Ensure the 'summary' column is of type string
df['Summary'] = df['Summary'].astype(str)

@app.route('/search', methods=['GET'])
def search_articles():
    keyword = request.args.get('keyword', '')
    try:
        # Perform the search
        articles = df[df['Summary'].str.contains(keyword, case=False, na=False)]
        return jsonify(articles.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)