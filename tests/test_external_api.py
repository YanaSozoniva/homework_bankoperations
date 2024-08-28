from src.external_api import convert_to_rubles
from unittest.mock import patch, Mock
import pytest


def test_convert_to_rubles_success():
    """Тестирует успешное получение текущего курса валют"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
    "query": {
        "amount": 1,
        "from": "USD",
        "to": "RUB"  },
    "result": 91.599176,}

    with patch('src.external_api.requests.get', return_value=mock_response):
        result = convert_to_rubles("USD", 1)
        assert result == 91.599176


def test_convert_to_rubles_incorrect_parameters():
    """Тестирует запрос, который содержит синтаксическую ошибку или неверные параметры."""
    mock_response = Mock()
    mock_response.status_code = 400

    with patch('src.external_api.requests.get', return_value=mock_response):
        with pytest.raises(ValueError, match="Не удалось получить курс валюты"):
            convert_to_rubles("руб", 1)



def test_convert_to_rubles_no_currency():
    """Тестирует некорректный результат конвертации валюты"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
    "query": {
        "amount": 1,
        "from": "USD",
        "to": "RUB" },
    "result": 0,}

    with patch('src.external_api.requests.get', return_value=mock_response):
        with pytest.raises(ValueError, match="Нет информации по валюте USD"):
            convert_to_rubles("USD", 1)
