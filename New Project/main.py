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
    items = []
    for cat in csv_categories():
    #through csv categories
        if cat == category:
        #if csv cat == chosen cat
            rows = df.values.tolist()
            for row in rows:
                if row[0] == cat:
                    items.append(row[1])
    print(items)

csv_items(category="Breakfast")