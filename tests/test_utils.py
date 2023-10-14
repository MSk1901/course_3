from src.utils import *
import pytest


@pytest.fixture
def list_with_dicts():
    return [{}, {"id": 1, "state": "EXECUTED"}, {"id": 1, "state": "CANCELED"}]


@pytest.fixture
def list_with_dates():
    return [{"id": 1, "date": "2018-03-23"}, {"id": 2, "date": "2019-08-26"}]


@pytest.fixture
def list_5():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_prepare_data(list_with_dicts):
    assert prepare_data(list_with_dicts) == [{"id": 1, "state": "EXECUTED"}]


def test_sort_by_date(list_with_dates):
    assert sort_by_date(list_with_dates) == [{"id": 2, "date": "2019-08-26"}, {"id": 1, "date": "2018-03-23"}]


def test_get_five(list_5):
    assert get_first_five(list_5) == [1, 2, 3, 4, 5]


def test_fix_date():
    assert fix_date("2019-08-26T10:50:58.294041") == "26.8.2019"


def test_check_from():
    assert check_from({"from": "card"}) == "card"
    assert check_from({"to": "card"}) is None


def test_make_numbers():
    assert make_numbers("Счет 64686473678894779589") == "Счет **9589"
    assert make_numbers("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"
