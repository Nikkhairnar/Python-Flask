# Part 4: Dynamic Routes - URL Parameters

## 🎯 Learning Goals
- Create dynamic routes with `<variable>` syntax
- Use type converters (`int`, `float`, `path`)
- Capture multiple parameters in one route
- Use `url_for()` to generate URLs dynamically

## 📖 Concepts Covered

### Basic Dynamic Route
```python
@app.route('/user/<username>')
def user_profile(username):
    return f"Hello, {username}!"
```
Visit `/user/Alice` → "Hello, Alice!"

### Type Converters
```python
@app.route('/post/<int:post_id>')    # Only integers
@app.route('/price/<float:amount>')  # Floating point
@app.route('/file/<path:filepath>')  # Includes slashes
```

### Multiple Parameters
```python
@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return f"{username}'s post #{post_id}"
```

### url_for() Function
```python
from flask import url_for

# Generate URLs dynamically
url_for('home')                        # Returns '/'
url_for('user_profile', username='Bob') # Returns '/user/Bob'
```

In templates:
```html
<a href="{{ url_for('user_profile', username='Alice') }}">Alice</a>
```

## 🚀 How to Run

```bash
cd part-4
python app.py
```

Try these URLs:
- `http://localhost:5000/` - Home with demos
- `http://localhost:5000/user/YourName` - Dynamic user page
- `http://localhost:5000/post/1` - Post by ID
- `http://localhost:5000/user/Alice/post/1` - Multiple params
- `http://localhost:5000/links` - url_for() demo

### Exercise 1 : Product Page
Task: Create a route that takes an integer ID and displays product details.
```bash
@app.route('/product/<int:product_id>')
def product(product_id):
    products = { 1: {'name': 'Laptop', ...}, 2: {'name': 'Mobile', ...} }
    product = products.get(product_id) # Finds the product or returns None
    return render_template('product.html', product=product, product_id=product_id)
```
Built a route that shows details for Laptops, Mobiles, and Groceries based on their ID.

### Exercise 2 : Category and Product Route
Task: Capture two different values in one URL.
```bash
@app.route('/category/<category_name>/product/<int:product_id>') # Two variables!
def category_product(category_name, product_id):
    # Logic to filter products by category_name...
    return render_template('category_product.html', ...)
```
Implemented a complex route that handles both Categories and Product IDs simultaneously.

### Exercise 3 : Search Route & Form
Task: Create a search page and a form that redirects to it.
```bash
@app.route('/search/', methods=['GET'])
def search_form():
    query = request.args.get('q', '') # Grabs what you typed in the box
    if query:
        return redirect(url_for('search', query=query)) # Sends you to /search/<query>
```
Created a functional search bar that captures a query and displays it on a new page.
