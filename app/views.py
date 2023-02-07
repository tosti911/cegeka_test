from flask import abort, jsonify

from app import app
from app.functions import read_cv_data

cv_data = read_cv_data()


@app.route("/")
def home():
    return "Welcome to the CV data API. Use /personal, /experience, /education, or /skills to access CV data."


@app.route("/personal")
def personal():
    if "personal" not in cv_data:
        abort(404, "personal data not found in cv_data.json")
    return jsonify(cv_data["personal"])


@app.route("/experience")
def experience():
    if "experience" not in cv_data:
        abort(404, "experience data not found in cv_data.json")
    return jsonify(cv_data["experience"])


@app.route("/education")
def education():
    if "education" not in cv_data:
        abort(404, "education data not found in cv_data.json")
    return jsonify(cv_data["education"])


@app.route("/skills")
def skills():
    if "skills" not in cv_data:
        abort(404, "skills data not found in cv_data.json")
    return jsonify(cv_data["skills"])