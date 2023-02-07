import json

from app import app
from app.views import cv_data


@app.cli.command()
def personal_data():
    """Gets and prints the personal data from the CV data file."""
    print(json.dumps(cv_data.get("personal", "Personal data not found in cv_data.json"), indent=2))


@app.cli.command()
def experience_data():
    """Gets and prints the experience data from the CV data file."""
    print(json.dumps(cv_data.get("experience", "Experience data not found in cv_data.json"), indent=2))


@app.cli.command()
def education_data():
    """Gets and prints the education data from the CV data file."""
    print(json.dumps(cv_data.get("education", "Education data not found in cv_data.json"), indent=2))


@app.cli.command()
def skills_data():
    """Gets and prints the skills data from the CV data file."""
    print(json.dumps(cv_data.get("skills", "Skills data not found in cv_data.json"), indent=2))
