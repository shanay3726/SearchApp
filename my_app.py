from flask import Flask, render_template, abort
 
app = Flask(__name__)
 
RESTAURANTS = {
    '1': {
        'name': 'Blaize',
        'category': 'Italian',
        'price': 12,
    },
    '2': {
        'name': 'Pasta Roma',
        'category': 'Italian',
        'price': 15,
    },
    '3': {
        'name': 'Taco Bell',
        'category': 'Mexican',
        'price': 7,
    },
    '4': {
        'name': 'Subway',
        'category': 'American',
        'price': 12
    }
}
 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', products=RESTAURANTS)
 
@app.route('/product/<key>')
def product(key):
    product = RESTAURANTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run()