# User Event Alert System

## Overview
This Flask API processes user transactions (deposits/withdrawals) and triggers alerts based on predefined rules, such as large withdrawals or consecutive transactions.

## Features
Accepts user actions via a /event endpoint.
Checks for alerts like withdrawals over 100, consecutive withdrawals, or deposits exceeding thresholds.
Returns alert codes and descriptive messages.

## Setup and Installation
Prerequisites
Python 3.6+
pip

## Steps
Extract ZIP File: Unzip the project:

bash
unzip interview-exercise.zip -d interview-exercise
cd interview-exercise

Install Dependencies: Install Flask and required packages:

bash
python3 -m pip install flask

Run the Server: Start the Flask server:

bash
python3 main.py

The server will run at http://127.0.0.1:5000/.

## API Usage
/event (POST)

Request Format:
json
{
  "type": "deposit",
  "amount": "42.00",
  "user_id": 1,
  "time": 10
}

Example Request:
bash
curl -XPOST http://127.0.0.1:5000/event -H 'Content-Type: application/json' \
-d '{"type": "deposit", "amount": "42.00", "user_id": 1, "time": 0}'

Response Format:
json
{
  "alert": true,
  "alert_codes": [1100],
  "alert_messages": ["Withdrawal amount exceeds 100"],
  "user_id": 1
}

