import os

from src.export_data_from_file import export_data_from_csv, export_data_from_xlsx
from src.filter_transactions import filter_by_operations
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_financial_transaction_data
from src.wedget import get_date, mask_account_card


def main():
    """Главная функция приложения"""

    answer_user = int(
        input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n"""
        )
    )
    path_file = os.getcwd()
    if answer_user == 1:
        print("Для обработки выбран JSON-файл")
        file_name = rf"{path_file}\data\operations.json"
        transactions = get_financial_transaction_data(file_name)
    elif answer_user == 2:
        print("Для обработки выбран CSV-файл")
        file_name = rf"{path_file}\data\transactions.csv"
        transactions = export_data_from_csv(file_name)
    else:
        print("Для обработки выбран XLSX-файл")
        file_name = rf"{path_file}\data\transactions_excel.xlsx"
        transactions = export_data_from_xlsx(file_name)

    flag_state = True
    while flag_state:
        state = input(
            """"Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        ).upper()
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            flag_state = False
            transactions = filter_by_state(transactions)
        else:
            print(f"Статус операции {state} недоступен")

    sort_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if sort_date == "да":
        reverse = input("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию \n").lower()
        is_revers = True if reverse == "по убыванию" else False
        transactions = sort_by_date(transactions, is_revers)

    rub_tran = input("Выводить только рублевые транзакции? Да/Нет \n").lower()
    if rub_tran == "да":
        transactions = list(filter_by_currency(transactions, "RUB"))

    is_filter_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n")
    if is_filter_word.lower() == "да":
        word = input("Введите слово, по которому нужно отфильтровать транзакции\n")
        transactions = filter_by_operations(transactions, word)

    print("Распечатываю итоговый список транзакций...\n")
    print(list(transactions))

    if len(list(transactions)) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(list(transactions))}\n")
        for tran in transactions:
            date = get_date(tran.get("date", "Дата не известна"))
            print(f"{date} {tran['description']}")

            to_disc = mask_account_card(tran["to"])
            if tran["description"] != "Открытие вклада":
                from_disc = mask_account_card(tran.get("from"))
                print(f"{from_disc} -> {to_disc}")
            else:
                print(f"{to_disc}")

            if answer_user == 1:
                print(
                    f"Сумма: {tran.get('operationAmount', {}).get('amount', '0')} "
                    f"{tran.get('operationAmount', {}).get('currency', {}).get('name', '')}\n"
                )
            else:
                print(f"Сумма: {tran.get('amount', '0')} {tran.get('currency_name', '')}\n")


if __name__ == "__main__":
    main()
