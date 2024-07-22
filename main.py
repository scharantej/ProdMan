
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

product_list = [
    {"name": "Product A", "description": "Description for Product A", "price": 10},
    {"name": "Product B", "description": "Description for Product B", "price": 20},
    {"name": "Product C", "description": "Description for Product C", "price": 30},
]

@app.route('/products')
def products():
    return render_template('products.html', products=product_list)

if __name__ == '__main__':
    app.run(debug=True)
