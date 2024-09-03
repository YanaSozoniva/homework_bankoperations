import csv
from os.path import exists
from typing import Any

import pandas as pd


def export_data_from_csv(file_name: str) -> list[dict]:
    """Функция считывание финансовых операций из CSV-файла"""
    if not exists(file_name):
        print("Файл не найден")
        return []
    with open(file_name, "r", encoding="utf-8") as file_csv:
        reader = csv.DictReader(file_csv, delimiter=";")
        # for item in reader:
        #     yield item
        return list(reader)


def export_data_from_xlsx(file_name: str) -> list:
    """Функция считывание финансовых операций из XLSX-файла"""
    if not exists(file_name):
        print("Файл не найден")
        return []
    reader = pd.read_excel(file_name)
    return list(reader.to_dict(orient="records"))


# if __name__ == '__main__':
#     rd = export_data_from_csv(r'C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\transactions.csv')
#     print(rd)
#     xr = export_data_from_xlsx(r'C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\transactions_excel.xlsx')
#     print(xr)
