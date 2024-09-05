from src.filter_transactions import filter_by_operations
from tests.conftest import transactions


def test_filter_by_operations(transactions):
    """Тестирование успешного нахождения списка операции по заданному описанию"""
    result = filter_by_operations(transactions, "ПЕРЕвод")
    assert result == transactions


def test_filter_by_operations_not_found_operation(transactions):
    """Тестирование, если не найдено не одной операции по заданному описанию"""
    result = filter_by_operations(transactions, "открытие")
    assert result == []


def test_filter_by_operations_not_found_key_description(transactions):
    """Тестирование, если отсутствует ключ description"""
    result = filter_by_operations(transactions, "открытие")
    assert result == []
