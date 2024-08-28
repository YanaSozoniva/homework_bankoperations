import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')


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


if __name__ == "__main__":
    print(convert_to_rubles("USD", 1))
