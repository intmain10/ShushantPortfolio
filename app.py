from flask import Flask, render_template, jsonify
import json

# Create an instance of the Flask class
app = Flask(__name__)

# Load the click count from a file (for persistence)
def load_click_count():
    try:
        with open('click_count.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return 0

# Save the click count to a file
def save_click_count(count):
    with open('click_count.json', 'w') as f:
        json.dump(count, f)

# Initialize click count
click_count = load_click_count()

# Define a route for the root URL ("/")
@app.route("/")
def home():
    return render_template('index.html')

# API route to update the click count
@app.route('/count_click', methods=['POST'])
def count_click():
    global click_count
    click_count += 1
    save_click_count(click_count)
    return jsonify({"status": "success", "click_count": click_count})

# Optional: Route to get the current click count (for displaying if needed)
@app.route('/get_click_count', methods=['GET'])
def get_click_count():
    return jsonify({"click_count": click_count})

# Run the app

