from unittest.mock import patch

import pandas as pd
import pytest

from src.export_data_from_file import export_data_from_csv, export_data_from_xlsx


@pytest.fixture
def expected():
    result = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    return result


@pytest.fixture
def path_csv():
    return r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\data\transactions.csv"


@patch("src.export_data_from_file.csv.DictReader")
def test_export_data_from_csv(mock_reader, path_csv, expected):
    """Тестирует успешное открытие файла и преобразование данных в список словарей"""
    mock_reader.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]

    result = export_data_from_csv(path_csv)
    assert result == expected
    mock_reader.assert_called_once()


def test_export_data_from_csv_not_found_file():
    """Тестирует получение пустого списка, если файл не найден"""
    path_file = r"C:\Users\user\Desktop\skyPro\ClientBankOperations\data\operations.json"
    assert export_data_from_csv(path_file) == []


@patch("src.export_data_from_file.csv.DictReader")
def test_export_data_from_csv_zero(mock_reader, path_csv):
    """Тестирует пустой файл"""
    mock_reader.return_value = []
    result = export_data_from_csv(path_csv)
    assert result == []
    mock_reader.assert_called_once()


@pytest.fixture
def path_exl():
    return r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\data\transactions.csv"


@pytest.fixture
def test_df():
    """Фикстура, создающая тестовый DataFrame"""

    test_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"],
    }
    return pd.DataFrame(test_dict)


@patch("src.export_data_from_file.pd.read_excel")
def test_export_data_from_xlsx(mock_reader, path_exl, test_df):
    """Тестирует успешное открытие файла и преобразование данных в список словарей"""
    mock_reader.return_value = test_df
    expected = test_df.to_dict(orient="records")
    result = export_data_from_xlsx(path_exl)
    assert result == expected
    mock_reader.assert_called_once()


@patch("src.export_data_from_file.pd.read_excel")
def test_export_data_from_exl_zero(mock_reader, path_exl):
    """Тестирует пустой файл"""
    mock_reader.return_value = pd.DataFrame()
    result = export_data_from_xlsx(path_exl)
    assert result == pd.DataFrame().to_dict(orient="records")
    mock_reader.assert_called_once()


def test_export_data_from_exl_not_found_file():
    """Тестирует получение пустого списка, если файл не найден"""
    path_file = ""
    assert export_data_from_xlsx(path_file) == []
