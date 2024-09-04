import json
import logging
from os.path import exists
from typing import Iterable

path_dir = r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\logs"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(path_dir + r"\utils_log.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s  %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transaction_data(path_file: str) -> Iterable:
    """Функция возвращает список словарей с данными о финансовых транзакциях."""
    transactions = []
    logger.info("Проверяется существует ли указанный путь")
    if not exists(path_file):
        return []
    else:
        with open(path_file, encoding="utf-8") as json_file:
            try:
                logger.info("Считываются данные из файла с данными в json - формате")
                transactions = json.load(json_file)
            except json.JSONDecodeError:
                logger.error("Произошла ошибка: json.JSONDecodeError")
                return transactions
            except TypeError:
                logger.error("Произошла ошибка: TypeError")
                return transactions

    return transactions


# if __name__ == "__main__":
#     print(
#         get_financial_transaction_data(
#             r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\data\operations.json"
#         )
#     )
