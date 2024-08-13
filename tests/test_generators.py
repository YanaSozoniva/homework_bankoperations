import pytest

from src.generators import filter_by_currency


def test_filter_by_currency(transactions):
    assert next(filter_by_currency(transactions, "USD")) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_currency_incorrect_currency(transactions):
    with pytest.raises(NameError):
        next(filter_by_currency(transactions, "UcSD"))


def test_filter_by_currency_zero_list():
    with pytest.raises(RuntimeError):
        next(filter_by_currency([], "USD"))
