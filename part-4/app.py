"""
Part 4: Dynamic Routes - URL Parameters
========================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Try different URLs like /user/YourName or /post/123
"""
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user/<username>')  # <username> captures any text from URL, visit: /user/Alice, /user/Bob
def user_profile(username):
    return render_template('user.html', username=username)


@app.route('/post/<int:post_id>')  # <int:post_id> captures only integers, /post/abc returns 404
def show_post(post_id):
    posts = {  # Simulated post data (in real apps, this comes from a database)
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }
    post = posts.get(post_id)  # Get the post or None if not found
    return render_template('post.html', post_id=post_id, post=post)


@app.route('/user/<username>/post/<int:post_id>')  # Multiple dynamic segments, visit: /user/Alice/post/1
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)


@app.route('/about/')  # Trailing slash means both /about and /about/ work
def about():
    return render_template('about.html')


@app.route('/links')  # Demonstrates url_for() - generates URLs dynamically (better than hardcoding!)
def show_links():
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
    }
    return render_template('links.html', links=links)

# Exercise 4.1: Product page route
@app.route('/product/<int:product_id>')
def product(product_id):
    products = {
        1: {'name': 'Laptop', 'price': 60000, 'category': 'electronics'},
        2: {'name': 'Mobile', 'price': 25000, 'category': 'electronics'},
        3: {'name': 'Rice', 'price': 60, 'category': 'groceries'},
        4: {'name': 'Eggs', 'price': 6, 'category': 'groceries'}
    }

    product = products.get(product_id)

    return render_template(
        'product.html',
        product=product,
        product_id=product_id
    )


# Exercise 4.2: Category and product route
@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):
    # Products dictionary with categories
    all_products = {
        1: {'name': 'Laptop', 'price': 60000, 'category': 'electronics'},
        2: {'name': 'Mobile', 'price': 25000, 'category': 'electronics'},
        3: {'name': 'Rice', 'price': 60, 'category': 'groceries'},
        4: {'name': 'Eggs', 'price': 6, 'category': 'groceries'}
    }

    # Get all products in this category
    category_products = {pid: prod for pid, prod in all_products.items() 
                        if prod['category'] == category_name}
    
    # Get the selected product (if provided)
    selected_product = all_products.get(product_id)
    
    # Check if selected product belongs to this category
    is_valid_product = selected_product and selected_product['category'] == category_name
    
    return render_template(
        'category_product.html',
        category_name=category_name,
        category_products=category_products,
        selected_product=selected_product if is_valid_product else None,
        product_id=product_id,
        is_valid_product=is_valid_product
    )


# Exercise 4.3: Search route
@app.route('/search/<query>')
def search(query):
    return render_template('search.html', query=query)


# Exercise 4.3 Bonus: Search form handler
@app.route('/search/', methods=['GET'])
def search_form():
    query = request.args.get('q', '')
    if query:
        return redirect(url_for('search', query=query))
    return render_template('search.html', query='')



if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# URL PARAMETER TYPES:
# =============================================================================
#
# <variable>         - String (default), accepts any text without slashes
# <int:variable>     - Integer, accepts only positive integers
# <float:variable>   - Float, accepts floating point numbers
# <path:variable>    - String, but also accepts slashes
# <uuid:variable>    - UUID strings
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 4.1: Create a product page
#   - Add route /product/<int:product_id>
#   - Create a products dictionary with id, name, price
#   - Display product details or "Not Found" message
#
# Exercise 4.2: Category and product route
#   - Add route /category/<category_name>/product/<int:product_id>
#   - Display both the category and product information
#
# Exercise 4.3: Search route
#   - Add route /search/<query>
#   - Display "Search results for: [query]"
#   - Bonus: Add a simple search form that redirects to this route
#
# =============================================================================
