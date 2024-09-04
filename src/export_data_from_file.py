import csv
import logging
from os.path import exists

import pandas as pd

logging.basicConfig(
    encoding="utf-8",
    filename=r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\logs\export_data_from_file.log",
    format="%(asctime)s  %(filename)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
)

logger = logging.getLogger("export_data_from_file")


def export_data_from_csv(file_name: str) -> list[dict]:
    """Функция считывание финансовых операций из CSV-файла"""
    logger.info("Проверка существования csv-файла")
    if not exists(file_name):
        logger.info("Файл не найден")
        return []
    logger.info("Считывание информации из csv-файла")
    with open(file_name, "r", encoding="utf-8") as file_csv:
        reader = csv.DictReader(file_csv, delimiter=";")
        # for item in reader:
        #     yield item
        return list(reader)


def export_data_from_xlsx(file_name: str) -> list:
    """Функция считывание финансовых операций из XLSX-файла"""
    logger.info("Проверка существования xlsx-файла")
    if not exists(file_name):
        logger.info("Файл не найден")
        return []
    logger.info("Считывание информации из xlsx-файла")
    reader = pd.read_excel(file_name)
    return list(reader.to_dict(orient="records"))


# if __name__ == '__main__':
#     rd = export_data_from_csv(r'C:\Users\user\Desktop\skyPro\practic\Home_work
#     \ClientBankOperations\transactions.csv')
#     print(rd)
#     xr = export_data_from_xlsx(r'C:\Users\user\Desktop\skyPro\practic\Home_work
#     \ClientBankOperations\transactions_excel.xlsx')
#     print(xr)
