from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_to_rubles, get_sum_transaction


def test_convert_to_rubles_success():
    """Тестирует успешное получение текущего курса валют"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "query": {"amount": 1, "from": "USD", "to": "RUB"},
        "result": 91.599176,
    }

    with patch("src.external_api.requests.get", return_value=mock_response):
        result = convert_to_rubles("USD", 1)
        assert result == 91.599176


def test_convert_to_rubles_incorrect_parameters():
    """Тестирует запрос, который содержит синтаксическую ошибку или неверные параметры."""
    mock_response = Mock()
    mock_response.status_code = 400

    with patch("src.external_api.requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Не удалось получить курс валюты"):
            convert_to_rubles("руб", 1)


def test_convert_to_rubles_no_currency():
    """Тестирует некорректный результат конвертации валюты"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "query": {"amount": 1, "from": "USD", "to": "RUB"},
        "result": 0,
    }

    with patch("src.external_api.requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Нет информации по валюте USD"):
            convert_to_rubles("USD", 1)

@pytest.mark.parametrize("tran, expected", [
    ({'id': 441945886, 'operationAmount': {'amount': '31957.58', 'currency':
        {'name': 'руб.', 'code': 'RUB'}}}, 31957.58),
    ({'id': 441945886, 'operationAmount': {'amount': '1', 'currency':
        {'name': 'руб.', 'code': 'RUB'}}}, 1),
        ({}, 0),
])
def test_get_sum_transaction_only_rub(tran, expected):
    """Тестирование вывода суммы транзакции в рублях или пустого словаря"""
    assert get_sum_transaction(tran) == expected


@patch('src.external_api.convert_to_rubles')
def test_get_sum_transaction_other_currency(mock_convert):
    """Тестирует успешное получение суммы транзакции, если валюта не рубль"""
    mock_convert.return_value = 1

    trans = {'id': 441945886, 'date': '2019-08-26T10:50:58.294041',
             'operationAmount': {'amount': '2', 'currency': {'name': 'USD', 'code': 'USD'}}}

    result = get_sum_transaction(trans)
    assert result == 1
    mock_convert.assert_called_once()

