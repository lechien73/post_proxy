"""
Simple proxy to redirect after Zapier
"""

from flask import Flask, request, redirect
import os
import requests


app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    """
    Main controller, checks for x_webhook, x_success and x_failure
    form fields. Uses environment variables if they're not available.
    """

    WEBHOOK = request.form["x_webhook"] if request.form["x_webhook"] else os.environ.get(
        "ZAPIER_WEBHOOK", "")
    SUCCESS_URL = request.form["x_success"] if request.form["x_success"] else os.environ.get(
        "SUCCESS_URL", "")
    FAILURE_URL = request.form["x_failure"] if request.form["x_failure"] else os.environ.get(
        "FAILURE_URL", "")

    response = requests.post(WEBHOOK, data=request.form)

    if response.status_code == 200:
        data = []
        if request.form["x_data"]:
            x_data = request.form["x_data"].split(",")
            data = [item + "=" + request.form[item] for item in x_data]

        return redirect(f"{SUCCESS_URL}?{'&'.join(data) if data else ''}")
    else:
        return redirect(f"{FAILURE_URL}?code={response.status_code}")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", 5000)),
            debug=False)
