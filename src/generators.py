from typing import Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    if len(transactions_list) == 0:
        raise RuntimeError("Список пуст")

    if all(tran["operationAmount"]["currency"]["name"] != currency for tran in transactions_list):
        raise NameError("Транзакций с данной валютой не было")

    for tran in transactions_list:
        if tran["operationAmount"]["currency"]["name"] == currency:
            yield tran


def transaction_descriptions(transactions_list: list[dict]) -> Generator:
    """Функция возвращает описание каждой операции по очереди"""

    if len(transactions_list) == 0:
        raise RuntimeError("Список пуст")

    for tran in transactions_list:
        yield tran["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """Генератор может сгенерировать номера карт в заданном диапазоне от
    0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if not 0 < start < stop < 10000000000000000:
        raise RuntimeError("Некорректный ввод данных")

    while start < stop + 1:
        start_str = str(f"{start:016}")
        yield start_str[:4] + " " + start_str[4:8] + " " + start_str[8:12] + " " + start_str[12:]
        start += 1
