# Part 1: Hello Flask - The Basics

## 🎯 Learning Goals
- Create your first Flask application
- Understand the `@app.route()` decorator
- Run a development server
- See the request-response cycle in action

## 📖 Concepts Covered

### The Flask App Structure
```python
from flask import Flask      # 1. Import
app = Flask(__name__)        # 2. Create app

@app.route('/')              # 3. Define route
def home():                  # 4. Handler function
    return "Hello!"          # 5. Response

app.run(debug=True)          # 6. Start server
```

### What is `@app.route('/')`?
- It's a **decorator** that tells Flask which URL should trigger the function
- `/` means the home page (root URL)
- `/about` would mean `localhost:5000/about`

### What is `debug=True`?
- Auto-reloads server when you save changes
- Shows detailed errors in the browser
- **Never use in production!**

## 🚀 How to Run

```bash
# Make sure you're in the part-1 folder
cd part-1

# Run the app
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debugger is active!
```

Open `http://localhost:5000` in your browser.

-----------------------------------------------------------------------

### Exercises Performed : 

1. Change the return message
```bash
@app.route('/')
def home():
    return "Hello Nikk!"
```
2. Return HTML
```bash
@app.route('/')
def home():
    return "<h1>Hello Flask!</h1><p>This is HTML</p>"
```
3. Add a second route
```bash
@app.route('/about')
def about():
    return "This is the about page"
```
