from flask import Flask, request, jsonify
import csv
import random
import datetime

import os

import config

app = Flask(__name__)

# Define the default response headers
DEFAULT_HEADERS = {
    'Content-Type': 'application/json'
}

# Define the endpoint to read the temp CSV file
@app.route('/read_temprature/<sector>', methods=["GET"])
def read_temprature(sector):
    # Construct the path to the CSV file
    csv_path = '/readings/soil_temprature_readings_sector_'+ sector +'.csv'

    # Read the contents of the CSV file
    rows = []
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)

    # Return the contents of the CSV file as a JSON response
    payload = {
        "message": "Temprature readings",
        "status": "success",
        "sector": sector,
        "contents": rows
    }

    return jsonify(payload), 200, DEFAULT_HEADERS

# Define the endpoint to read the huumidity CSV file
@app.route('/read_humidity/<sector>', methods=["GET"])
def read_humidity(sector):
    # Construct the path to the CSV file
    csv_path = '/readings/soil_humidity_readings_sector_'+ sector +'.csv'

    # Read the contents of the CSV file
    rows = []
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)

    # Return the contents of the CSV file as a JSON response
    payload = {
        "message": "Humidity readings",
        "status": "success",
        "sector": sector,
        "contents": rows
    }

    return jsonify(payload), 200, DEFAULT_HEADERS

if __name__ == "__main__":
    app.run(
        debug=config.DEBUG_MODE, host=config.MS_HOST, port=os.getenv('PORT', config.MS_PORT)
    )
