from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def csv_categories():
    df = pd.read_csv("mcdonalds.csv")
    df = df.fillna("")
    categories = df["Category"].unique()
    return categories

def csv_items(category):
    df = pd.read_csv("mcdonalds.csv")
    df = df.fillna("")
    items = []
    headers = list(df.columns[1:])
    for _, row in df.iterrows():
        if row["Category"] == category:
            items.append(row[1:].tolist())

    return items, headers

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Breakfast')
def breakfast():
    return render_template('Breakfast.html', categories = csv_items("Breakfast"))

@app.route('/Beef-and-pork')
def beef_and_pork():
    return render_template('Beef-and-pork.html', categories = csv_items("Beef & Pork"))

@app.route('/Chicken-and-fish')
def chicken_and_fish():
    return render_template('Chicken-and-fish.html', categories = csv_items("Chicken & Fish"))

@app.route('/Salads')
def salads():
    return render_template('Salads.html', categories = csv_items("Salads"))

@app.route('/Snacks-and-sides')
def snacks_and_sides():
    return render_template('Snacks-and-sides.html', categories = csv_items("Snacks & Sides"))

@app.route('/Desserts')
def desserts():
    return render_template('Desserts.html', categories = csv_items("Desserts"))

@app.route('/Beverages')
def beverages():
    return render_template('Beverages.html', categories = csv_items("Beverages"))

@app.route('/Coffee-and-tea')
def coffee_and_tea():
    return render_template('Coffee-and-tea.html', categories = csv_items("Coffee & Tea"))

@app.route('/Smoothies-and-shakes')
def smoothies_and_shakes():
    return render_template('Smoothies-and-shakes.html', categories = csv_items("Smoothies & Shakes"))

if __name__ == '__main__':
    app.run(debug=True)