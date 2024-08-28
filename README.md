# Client_Bank_Operations

## Описание:

Client_Bank_Operations - это приложение на Python, которое показывает несколько последних успешных банковских операций клиента.

## Установка:

Клонируйте репозиторий:

Для SSH:
```
git clone git@github.com:YanaSozoniva/homework_bankoperations.git
```
Для HTTPS:
```
git clone https://github.com/YanaSozoniva/homework_bankoperations.git
```

## Разработанные функции и примеры работы с ними:
### Модуль Processing
#### Функция filter_by_state
Возвращает новый список словарей, у которых ключ state соответствует указанному значению.

my_list =[
             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
         ]

Вывод функции со статусом по умолчанию 'EXECUTED'
filter_list = filter_by_state(my_list)
--> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Вывод функции, если вторым аргументов передано 'CANCELED'
filter_list = filter_by_state(my_list, "CANCELED")
--> [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
 
#### Функция sort_by_date
Функция возвращает новый список, отсортированный по дате (по умолчанию - сортируется по убыванию).

my_list =[
             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
         ]

Вывод функции (сортировка по убыванию (по умолчанию))
filter_list = sort_by_date(my_list)
--> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Вывод функции (сортировка по возрастанию)
filter_list = sort_by_date(my_list, False)
--> [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

### Модуль mask
#### Функция get_mask_card_number
Функция принимает на вход номер карты и возвращает ее маску.

Вывод функции
get_mask_card_number(7000792289606361)
-->7000 79** **** 6361

#### Функция get_mask_account
Функция принимает на вход номер счета и возвращает его маску.

Вывод функции
get_mask_account(73654108430135874305)
-->**4305

### Модуль wedget
#### Функция mask_account_card
Функция принимает информацию о карте/счете и возвращает их маску.

Вывод функции
mask_account_card("Visa Platinum 7000792289606361")
-->Visa Platinum 7000 79** **** 6361
mask_account_card("Счет 64686473678894779589")
-->Счет **9589

#### Функция get_date
Функция принимает на вход дату в формате "2024-03-11T02:26:18.671407" и возвращает - в формате 'ДД.ММ.ГГГГ'

Вывод функции
get_date("2024-03-11T02:26:18.671407")
-->11.03.2024

### Модуль generators
#### Функция filter_by_currency
Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.

Вывод функции 
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
--> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD" } },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD" } },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       } 

#### Функция transaction_descriptions
Функция возвращает описание каждой операции по очереди.

Вывод функции 
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

--> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации

### Функция card_number_generator
Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.

Вывод функции 
for card_number in card_number_generator(1, 5):
    print(card_number)

--> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005

## Модуль decorators
#### Функция log
Декоратор регистрирует детали выполнения функций: имя функции, передаваемые аргументы, результат выполнения
и информация об ошибках. Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.

Вывод функции
 @log()
    def my_function(x, y):
        return x + y
    my_function(2, 3)
-->Функция my_function выполнилась успешно. Результат ее работы - 5.

 my_function("2", 3)
-->Функция my_function не выполнилась. Тип ошибки can only concatenate str (not "int") to str. 
 Входные данные: args = ('2', 3), kwargs = {}.

## Модуль utils
#### Функция get_financial_transaction_data
Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
Возвращает список словарей с данными о финансовых транзакциях.Если файл пустой, содержит не список или не найден, 
функция возвращает пустой список."""

Вывод функции
get_financial_transaction_data(r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\data\operations.json"
-->[{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': 
{'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации',
'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'EXECUTED', 
'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}, ]

## Модуль external_api
#### Функция convert_to_rubles
Функция обращается к внешнему API для получения текущего курса валют и конвертирует сумму операции в рубли.

Вывод функции
convert_to_rubles("USD", 1)
-->{
  "date": "2024-08-28",
  "historical": "",
  "info": {
    "rate": 148.972231,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 1,
    "from": "USD",
    "to": "RUB"
  },
  "result": 91.599176,
  "success": true
}

#### Функция get_sum_transaction
Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях. Если транзакция была
в другой валюте - суммы операции конвертируется в рубли

Вывод функции
trans = {'id': 441945886, 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': 
{'name': 'руб.', 'code': 'RUB'}}}
get_sum_transaction(trans)
-->31957.58

## Тестирование
Проект покрыт unit-тестами. Для тестирования использовался фреймворк pytest. 
Для их запуска выполните команду:
```
pytest
```