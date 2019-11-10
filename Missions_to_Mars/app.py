from flask import Flask, render_template
from flask_pymongo import pymongo
# import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.MarsDB
collection = db.mars

@app.route("/")
def index():
    mars = list(db.collection.find())
    return render_template("index.html", mars=mars)


# @app.route("/scrape")
# def scrape():
#     mars = mongo.db.mars
#     mars_data = scrape_mars.scrape_all()
#     mars.update({}, mars_data, upsert=True)
#     return "Scraping Successful!"


if __name__ == "__main__":
    app.run(debug=True)
