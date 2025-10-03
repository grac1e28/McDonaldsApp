import requests
from flask import Flask, render_template




@app.route('/', methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        weather = requests.get(url).json()
    return render_template("index.html", weather=weather)



if __name__ == "__main__":
    app.run(debug=True)