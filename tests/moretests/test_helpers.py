from app.helpers import pretty_date
from datetime import datetime, timedelta


def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"