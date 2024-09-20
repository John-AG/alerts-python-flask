import pytest 
from app import check_alerts, user_transactions

def test_withdrawl_above_100():
    user_id = 'user_1'
    user_transactions[user_id] = []

    alert_codes = check_alerts(user_id, "withdraw", 150, 100)

    assert 1100 in alert_codes
    assert len(alert_codes) == 1

def test_3_consecutive_withdrawls():
    user_id = 'user_2'
    user_transactions[user_id] = []

    alert_codes = check_alerts(user_id, "withdraw", 50, 100)
    alert_codes = check_alerts(user_id, "withdraw", 30, 100)
    alert_codes = check_alerts(user_id, "withdraw", 40, 100)

    assert 30 in alert_codes
    assert len(alert_codes) == 1

def test_3_consecutive_deposits():
    user_id = "user_3"
    user_transactions[user_id] = []

    alert_codes = check_alerts(user_id, "deposit", 20, 50)
    alert_codes = check_alerts(user_id, "deposit", 30, 60)
    alert_codes = check_alerts(user_id, "deposit", 40, 60)

    assert 300 in alert_codes
    assert len(alert_codes) == 1

def test_deposits_exceed_200():
    user_id = "user_4"
    user_transactions[user_id] = []

    alert_codes = check_alerts(user_id, "deposit", 50, 10)
    alert_codes = check_alerts(user_id, "deposit", 160, 5)

    assert 123 in alert_codes
    assert len(alert_codes) == 1