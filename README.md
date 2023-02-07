## Description
This is a coding test example for a simple Flask app that presents your CV data

## Installation
First we need to clone the repository using: `git clone https://github.com/tosti911/cegeka_test.git`

After that we need to create a Virtual Environment using: `python -m venv venv`

Activate the venv using: `source venv/bin/activate`, followed by installing the requirements for this project: `pip install -r requirements.txt`

## Usage
The application can be run either by calling `python flask-run.py`, or by using the terminal with `flask run`

In order to see all the available routes, we have the following options:
- We can navigate to `http://localhost:5000/`
- We can run `flask routes` in the terminal and see a list of routes

For the CLI commands, run `flask` inside the terminal to see a list of all the cli commands.

The following endpoints are available:
- `/personal` which returns the personal data from the CV
- `/experience` which returns the experience data from the CV
- `/education` which returns the education data from the CV
- `/skills` which returns the skills data from the CV

The following CLI commands are available:
- `flask personal-data` which returns the personal data from the CV
- `flask experience-data` which returns the experience data from the CV
- `flask education-data` which returns the education data from the CV
- `flask skills-data` which returns the skills data from the CV