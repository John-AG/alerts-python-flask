from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

user_transactions = defaultdict(list)

ALERT_MESSAGES = {
    1100: "Withdrawal amount exceeds 100.",
    30: "Three consecutive withdrawals detected.",
    300: "Three consecutive deposits, each larger than the last.",
    123: "Deposits exceeding 200 in a 30-second window detected."
}

def check_alerts(user_id, transaction_type, amount, timestamp):
    alert_codes = []
    transactions = user_transactions[user_id]

    transactions.append({"type": transaction_type, "amount": float(amount), "time": timestamp})

    if transaction_type == "withdraw" and float(amount) > 100:
        alert_codes.append(1100)

    last_3_transactions = transactions[-3:]
    if len(last_3_transactions) == 3 and all(t["type"] == "withdraw" for t in last_3_transactions):
        alert_codes.append(30)

    deposits = [t for t in transactions if t["type"] == "deposit"]
    if len(deposits) >= 3 and deposits[-3]["amount"] < deposits[-2]["amount"] < deposits[-1]["amount"]:
        alert_codes.append(300)

    total_deposit_in_30s = sum(
        t["amount"] for t in deposits if timestamp - t["time"] <= 30
    )
    if total_deposit_in_30s > 200:
        alert_codes.append(123)

    return alert_codes

@app.route('/event', methods=['POST'])
def event():
    data = request.get_json()
    user_id = data['user_id']
    transaction_type = data['type']
    amount = data['amount']
    timestamp = data['time']

    alert_codes = check_alerts(user_id, transaction_type, amount, timestamp)

    response = {
        "alert": bool(alert_codes),
        "alert_codes": alert_codes,
        "alert_messages": [ALERT_MESSAGES[code] for code in alert_codes],
        "user_id": user_id
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
