from src.filter_transactions import filter_by_operations, get_count_transactions_by_category


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
    tran = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        }
    ]
    result = filter_by_operations(tran, "открытие")
    assert result == []


def test_filter_by_operations_zero_list(transactions):
    """Тестирование, если передан пустой словарь"""
    result = filter_by_operations([], "открытие")
    assert result == []


def test_get_count_transactions_by_category_no_operation(transactions):
    """Тестирование успешного нахождения списка операции и их количества, если список не указан"""
    result = get_count_transactions_by_category(transactions)
    assert result == {"Перевод организации": 2, "Перевод со счета на счет": 2, "Перевод с карты на карту": 1}


def test_get_count_transactions_by_category(transactions):
    """Тестирование успешного нахождения списка операции и их количества по указанному списку"""
    result = get_count_transactions_by_category(transactions, ["Перевод со счета на счет", "Перевод с карты на карту"])
    assert result == {"Перевод со счета на счет": 2, "Перевод с карты на карту": 1}


def test_get_count_transactions_by_category_not_found_operation(transactions):
    """Тестирование, если не найдено не одной категории операций по заданному списку"""
    result = get_count_transactions_by_category(transactions, ["открытие"])
    assert result == {}


def test_get_count_transactions_by_category_not_found_key_description(transactions):
    """Тестирование, если отсутствует ключ description"""
    tran = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        }
    ]
    result = get_count_transactions_by_category(tran, ["Перевод с карты на карту"])
    assert result == {}


def test_get_count_transactions_by_category_zero_list(transactions):
    """Тестирование, если передан пустой словарь"""
    result = get_count_transactions_by_category([], "Перевод с карты на карту")
    assert result == {}
