import pytest

from heysummit import __version__
from heysummit.api import HeySummit, HeySummitException


def test_version():
    assert __version__ == "0.1.0"


def test_token(token):
    test = HeySummit(token=token)

    assert type(test) is HeySummit


def test_no_token():
    with pytest.raises(HeySummitException):
        HeySummit()


def test_get_all_events(hey):

    result = hey.get_events()

    assert len(result) > 0


def test_get_all_talks(hey):

    result = hey.get_talks()

    assert type(result) is list
    assert len(result) > 5


def test_get_all_attendees(hey):

    result = hey.get_attendees()

    assert type(result) is list
    assert len(result) > 5


def test_get_attendee_bad_id(hey):

    result = hey.get_attendee(id=1)

    assert result is None


def test_get_attendee_good_id(hey):

    result = hey.get_attendee(id=1697964)

    assert type(result) is dict
    assert result["event_name"] == "Open Security Summit 2020"


def test_get_all_tickets(hey):

    result = hey.get_tickets()

    assert type(result) is list
    assert len(result) > 5


def test_get_nonexistent_ticket(hey):

    result = hey.get_ticket(id=1)

    assert result is None


def test_get_specific_ticket(hey):

    result = hey.get_ticket(id=8250)
    assert type(result) is dict
    assert result["event_name"] == "Pre Summit Working Sessions"


def test_add_attendee_bad(hey):

    with pytest.raises(HeySummitException):
        hey.add_attendee()


def test_add_attendee_good(hey):

    added = hey.add_attendee(
        event=5573,
        email="felipe.zipitria+test@owasp.org",
        name="Felipe Zipitria API Test",
    )

    assert added is True
