from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests

load_dotenv()

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = []
    
    if request.method == 'POST':
        try:
            url = request.form['url']
            r = requests.get(url)
            print(r.text)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid try again."
            )
    return render_template('index.html', errors=errors, results=results)

if __name__ == '__main__':
    app.run()