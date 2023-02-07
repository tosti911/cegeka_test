import json

from flask import abort


def read_cv_data():
    try:
        with open("cv_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        abort(404, "cv_data.json not found")
    except json.JSONDecodeError:
        abort(500, "cv_data.json is not a valid JSON file")
    except Exception as ex:
        abort(500, f"An error occured while reading the CV data: {ex}")
