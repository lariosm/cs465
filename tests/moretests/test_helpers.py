from app.helpers import pretty_date
from datetime import datetime, timedelta


def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"

def test_days_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=5))) == "5 days ago"

def test_months_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(weeks=11))) == "2 months ago"

def test_years_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(weeks=120))) == "2 years ago"

def test_weeks_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(weeks=3))) == "3 weeks ago"

def test_minutes_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(minutes=33))) == "33 minutes ago"

def test_hours_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(hours=14))) == "14 hours ago"

def test_hour_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(minutes=70))) == "an hour ago"

def test_minute_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=92))) == "a minute ago"

def test_seconds_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=42))) == "42 seconds ago"