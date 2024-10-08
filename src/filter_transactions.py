import logging
import re
from collections import Counter

logging.basicConfig(
    encoding="utf-8",
    filename=r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\logs\filter_transactions.log",
    format="%(asctime)s  %(filename)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
)

logger = logging.getLogger("filter_transactions")


def filter_by_operations(transactions: list[dict], request: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка"""
    filter_tran = []
    logger.info('Перебор словарей, проверка наличия ключа "description" и ест ли в нем искомая строка описания')
    for tran in transactions:
        if not tran.get("description"):
            continue
        else:
            if re.match(request.lower(), tran["description"].lower()):
                filter_tran.append(tran)
    return filter_tran


def get_count_transactions_by_category(transactions: list[dict], operations: list = None) -> dict:
    """Функция принимает список с данными о банковских операциях и список категорий операций,
    а возвращает словарь с названиями категории и количество операций в каждой категории
    (по умолчанию - выводит список всех найденных категорий и их количество)"""
    logger.info("Формирование словаря с категориями")
    categories = [tran.get("description") for tran in transactions]
    logger.info("Подсчет операций по категориям")
    count_transaction = dict(Counter(categories))
    if operations:
        result_transaction = {key: val for key, val in count_transaction.items() if key in operations}
        return result_transaction
    return count_transaction


# if __name__ == "__main__":
#     transact = [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160"
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {
#                 "amount": "56883.54",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229"
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {
#                 "amount": "67314.70",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657"
#         }
#     ]
#     print(filter_by_operations(transact))
#     print(get_count_transactions_by_category(transact))
