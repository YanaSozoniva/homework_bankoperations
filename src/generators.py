def filter_by_currency(transactions_list: list[dict], currency: str):
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    if len(transactions_list) == 0:
        raise RuntimeError("Список пуст")

    if all(tran["operationAmount"]["currency"]["name"] != currency for tran in transactions_list):
        raise NameError("Транзакций с данной валютой не было")

    for tran in transactions_list:
        if tran["operationAmount"]["currency"]["name"] == currency:
            yield tran


def transaction_descriptions(transactions_list: list[dict]):
    """Функция возвращает описание каждой операции по очереди"""

    if len(transactions_list) == 0:
        raise RuntimeError("Список пуст")

    for tran in transactions_list:
        yield tran["description"]
