import json
from unittest.mock import Mock

import pytest

from src.utils import get_financial_transaction_data


@pytest.fixture()
def path_f():
    return r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\data\operations.json"


def test_get_financial_transaction_data(path_f):
    mock_json_objict = Mock(return_value=[{"id": 441945886, "state": "EXECUTED"}])
    json.load = mock_json_objict
    assert get_financial_transaction_data(path_f) == [{"id": 441945886, "state": "EXECUTED"}]
    mock_json_objict.assert_called()


def test_get_financial_transaction_data_not_found_file():
    path_file = r"C:\Users\user\Desktop\skyPro\ClientBankOperations\data\operations.json"
    assert get_financial_transaction_data(path_file) == []


def test_get_financial_transaction_data_error_json(path_f):
    mock_json_objict = Mock(return_value=[])
    json.load = mock_json_objict
    assert get_financial_transaction_data(path_f) == []
    mock_json_objict.assert_called()
