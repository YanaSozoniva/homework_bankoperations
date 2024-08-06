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

Выdод функции (сортировка по убыванию (по умолчанию))
filter_list = sort_by_date(my_list)
--> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Вывод функции (сортировка по возрастанию)
filter_list = sort_by_date(my_list, False)
--> [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]