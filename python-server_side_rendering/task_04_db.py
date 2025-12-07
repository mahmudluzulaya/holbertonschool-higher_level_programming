#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def read_json():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except Exception as e:
        return {"error": f"JSON Error: {str(e)}"}

def read_csv():
    products = []
    try:
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": row.get("id"),
                    "name": row.get("name"),
                    "category": row.get("category"),
                    "price": row.get("price")
                })
        return products
    except Exception as e:
        return {"error": f"CSV Error: {str(e)}"}

def read_sqlite():
    if not os.path.exists("products.db"):
        return {"error": "Database not found. Please create products.db first."}

    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = []
        for r in rows:
            products.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            })

        return products
    except Exception as e:
        return {"error": f"Database Error: {str(e)}"}

@app.route("/", strict_slashes=False)
def index():
    source = request.args.get("source", "json")

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    elif source == "sql":
        data = read_sqlite()
    else:
        return render_template("product_display.html", error="Wrong source")

    if isinstance(data, dict) and "error" in data:
        return render_template("product_display.html", error=data["error"])

    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(debug=True)
