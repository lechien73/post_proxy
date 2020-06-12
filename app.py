"""
Simple proxy to redirect after Zapier
"""

from flask import Flask, request, redirect
import os
import requests


app = Flask(__name__)
WEBHOOK = os.environ.get("ZAPIER_WEBHOOK")
SUCCESS_URL = os.environ.get("SUCCESS_URL")
FAILURE_URL = os.environ.get("FAILURE_URL")


@app.route("/", methods=["POST"])
def index():
    response = requests.post(WEBHOOK, data=request.form)

    if response.status_code == 200:
        return redirect(SUCCESS_URL)
    else:
        return redirect(FAILURE_URL)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", 5000)),
            debug=False)
