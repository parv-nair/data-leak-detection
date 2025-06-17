from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
HIBP_API_KEY = os.getenv("HIBP_API_KEY")
HIBP_API_URL = "https://haveibeenpwned.com/api/v3/breachedaccount/"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_email():
    email = request.form.get("email")
    headers = {"hibp-api-key": HIBP_API_KEY, "User-Agent": "data-leak-checker"}

    try:
        # Query the API
        response = requests.get(f"{HIBP_API_URL}{email}", headers=headers)

        # Debugging: Print response details
        print(f"Status Code: {response.status_code}, Response: {response.text}")

        if response.status_code == 404:  # No breaches found
            return jsonify({"result": "Good news — no pwnage found!"})
        elif response.status_code == 200:  # Breach found
            breaches = response.json()
            breach_count = len(breaches)
            return jsonify({"result": f"Oh no — pwned! Found in {breach_count} data breaches."})
        else:  # Unexpected error
            return jsonify({"result": f"Unexpected error: {response.text}"})
    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging: Print the exception
        return jsonify({"result": f"An error occurred: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
