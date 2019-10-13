from app.helpers import pretty_date
from datetime import datetime, timedelta


def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"

def test_days_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=5))) == "5 days ago"

def test_months_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(weeks=11))) == "2 months ago"