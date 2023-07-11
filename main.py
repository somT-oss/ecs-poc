from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route and its corresponding view function
@app.route('/')
def hello():
    return "Hello, World!"

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)