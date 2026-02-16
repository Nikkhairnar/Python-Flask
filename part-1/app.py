from flask import Flask  # Import Flask class from the flask package

app = Flask(__name__)  # Create Flask app instance, __name__ tells Flask where to look for templates/static files


@app.route('/')  # Decorator that maps URL '/' (home page) to this function
def home():
    return "Hello Flask! Welcome to my first web server!"  # This text displays in the browser


if __name__ == '__main__':
    app.run(debug=True)  # debug=True enables auto-reload and detailed error messages


