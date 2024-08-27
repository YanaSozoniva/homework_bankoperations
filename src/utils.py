import json
from os.path import exists
from typing import Any


def get_financial_transaction_data(path_file: str) -> Any:
    """Функция возвращает список словарей с данными о финансовых транзакциях."""
    if not exists(path_file):
        return []
    else:
        with open(path_file, encoding="utf-8") as json_file:
            try:
                transactions = json.load(json_file)
            except json.JSONDecodeError:
                return []
            except TypeError:
                return []

    return transactions


# if __name__ == "__main__":
#     print(
#         get_financial_transaction_data(
#             r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\data\operations.json"
#         )
#     )
