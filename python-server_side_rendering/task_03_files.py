from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def read_csv(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert id and price to correct types
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id')
    prod_id = int(prod_id) if prod_id and prod_id.isdigit() else None

    if source not in ['json', 'csv']:
        return render_template("product_display.html", error="Wrong source", products=[])

    file_path = f"products.{source}"
    if not os.path.exists(file_path):
        return render_template("product_display.html", error="File not found", products=[])

    data = read_json(file_path) if source == 'json' else read_csv(file_path)

    if prod_id:
        filtered = [p for p in data if p['id'] == prod_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found", products=[])
        data = filtered

    return render_template("product_display.html", products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
