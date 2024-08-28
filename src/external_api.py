import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rubles(currency_cod: str, amount: float) -> float:
    """Функция обращается к внешнему API для получения текущего курса валют и
    конвертирует сумму операции в рубли"""
    headers = {"apikey": API_KEY}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_cod}&amount={amount}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Не удалось получить курс валюты")

    total_amount = response.json()["result"]

    if total_amount <= 0:
        raise ValueError(f"Нет информации по валюте {currency_cod}")

    return total_amount


def get_sum_transaction(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    Если транзакция была в другой валюте - суммы операции конвертируется в рубли"""
    if not transaction or not transaction.get("operationAmount"):
        return 0
    cod = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])

    if cod == "RUB":
        return amount
    else:
        amount = convert_to_rubles(cod, amount)

    return amount


# if __name__ == "__main__":
#     trans = {'id': 441945886, 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}}
#     print(get_sum_transaction(trans))
