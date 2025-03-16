from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Replace with your API keys
GOOGLE_MAPS_API_KEY = "AIzaSyCcYKj43SqvLuJ-RutR8aPBcAYtl6gmM38"
PREDICTHQ_API_KEY = "y_P5EjAlaQmrGTgEwsOW-PO3HxTGwjhjFHP-XjmR"

# PredictHQ API endpoint
PREDICTHQ_EVENTS_URL = "https://api.predicthq.com/v1/events/"

# Home route to render the map and button
@app.route("/")
def home():
    return render_template("map.html", google_maps_api_key=GOOGLE_MAPS_API_KEY)

# Route to fetch events and return as JSON
@app.route("/fetch_events")
def fetch_events():
    # Fetch events from PredictHQ API for Bengaluru
    headers = {
        "Authorization": f"Bearer {PREDICTHQ_API_KEY}",
        "Accept": "application/json"
    }
    params = {
        "within": "10km@12.9716,77.5946",  # Events within 10km of Bengaluru
        "active.gte": "2023-10-01",  # Example: Events active after October 1, 2023
        "limit": 20  # Limit to 20 events
    }
    response = requests.get(PREDICTHQ_EVENTS_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        events = response.json().get("results", [])
        return jsonify(events)
    else:
        return jsonify({"error": "Failed to fetch events"}), 500

if __name__ == "__main__":
    app.run(debug=True)