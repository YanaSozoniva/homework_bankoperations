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
### Функция filter_by_state

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
 
### Функция sort_by_date

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

## Тестирование
Проект покрыт юнит-тестами. Для тестирования использовался фреймворк pytest. 
Для их запуска выполните команду:
```
pytest
```

### Функция filter_by_currency

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

### Функция transaction_descriptions

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

Вывод функции 
for card_number in card_number_generator(1, 5):
    print(card_number)

--> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005

## Тестирование
Проект покрыт юнит-тестами. Для тестирования использовался фреймворк pytest. 
Для их запуска выполните команду:
```
pytest
```