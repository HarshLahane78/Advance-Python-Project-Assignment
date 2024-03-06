from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    try:
        req = requests.get('https://cat-fact.herokuapp.com/facts')
        req.raise_for_status()  # Raise an error for 4xx or 5xx status codes
        data = req.json()
        return render_template('index.html', data=data)
    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching cat facts: {e}"
        return render_template('error.html', error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
