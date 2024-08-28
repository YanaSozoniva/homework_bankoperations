import json
from os.path import exists
from typing import Iterable


def get_financial_transaction_data(path_file: str) -> Iterable:
    """Функция возвращает список словарей с данными о финансовых транзакциях."""
    transactions = []
    if not exists(path_file):
        return []
    else:
        with open(path_file, encoding="utf-8") as json_file:
            try:
                transactions = json.load(json_file)
            except json.JSONDecodeError:
                return transactions
            except TypeError:
                return transactions

    return transactions


# if __name__ == "__main__":
#     print(
#         get_financial_transaction_data(
#             r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\data\operations.json"
#         )
#     )
