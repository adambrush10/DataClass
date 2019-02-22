from flask import Flask, render_template, redirect
import datetime
import mission_to_mars
from flask_pymongo import PyMongo
import pandas as pd

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:5000/mission_to_mars'
mongo = PyMongo(app)
last_update = ''

@app.route('/')
def main():
    #last_update = datetime.datetime.now().strftime("%b %d, %Y at %H:%M")
    #headline = mongo.db.variables.find({'type':'headlines'})[0]

    return render_template('index.html',
        mars = mission_to_mars.mars_dict)

@app.route("/scrape")
def scrape():
    from mission_to_mars import news
    last_update = datetime.datetime.now().strftime("%b %d, %Y at %H:%M")

    return redirect('/')






if __name__ == "__main__":
    app.run(debug=True)
