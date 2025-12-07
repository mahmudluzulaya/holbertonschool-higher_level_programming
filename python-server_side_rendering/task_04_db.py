#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# -------- JSON --------
def read_json(product_id=None):
    try:
        with open("products.json", "r") as f:
            data = json.load(f)
    except Exception as e:
        return {"error": f"JSON Error: {str(e)}"}

    if product_id is None:
        return data

    # Filter by ID
    for p in data:
        if str(p.get("id")) == str(product_id):
            return [p]

    return []  # no product found


# -------- CSV --------
def read_csv(product_id=None):
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
    except Exception as e:
        return {"error": f"CSV Error: {str(e)}"}

    if product_id is None:
        return products

    for p in products:
        if str(p["id"]) == str(product_id):
            return [p]

    return []


# -------- SQL --------
def read_sqlite(product_id=None):
    if not os.path.exists("products.db"):
        return {"error": "Database not found. Please create products.db first."}

    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        if product_id:
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id = ?",
                (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()
        conn.close()

        products = [{
            "id": r[0],
            "name": r[1],
            "category": r[2],
            "price": r[3]
        } for r in rows]

        return products
    except Exception as e:
        return {"error": f"Database Error: {str(e)}"}


# -------- MAIN ROUTE --------
@app.route("/products", strict_slashes=False)
def products():
    source = request.args.get("source", "json")
    product_id = request.args.get("id", None)

    if source == "json":
        data = read_json(product_id)
    elif source == "csv":
        data = read_csv(product_id)
    elif source == "sql":
        data = read_sqlite(product_id)
    else:
        return render_template("product_display.html", error="Wrong source"), 200

    # Check for errors
    if isinstance(data, dict) and "error" in data:
        return render_template("product_display.html", error=data["error"]), 200

    # No product found
    if product_id and len(data) == 0:
        return render_template(
            "product_display.html",
            error="Product not found"
        ), 200

    return render_template("product_display.html", products=data), 200


if __name__ == "__main__":
    app.run(debug=True)
