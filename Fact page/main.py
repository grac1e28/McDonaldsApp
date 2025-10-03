import requests
from flask import Flask

app = Flask("__main__")

def get_random_fact():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url)
    data = response.json()
    return data["text"]




@app.route
def index():
    return


if __name__ == "__main__":
    app.run(debug=True)