import re


def filter_by_operations(transactions: list[dict], request: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
     а возвращать список словарей, у которых в описании есть данная строка"""
    filter_tran = []
    for tran in transactions:
        if not tran.get("description"):
            continue
        else:
            if re.match(request.lower(), tran["description"].lower()):
                filter_tran.append(tran)
    return filter_tran


# if __name__ == "__main__":
#     transact = [
#     { "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {"amount": "31957.58",
#     "currency": {"name": "руб.", "code": "RUB"} },
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"},
#     { "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {"amount": "8221.37",
#     "currency": {"name": "USD", "code": "USD"}},
#
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"},
#         {
#             "id": 587085106,
#             "state": "EXECUTED",
#             "date": "2018-03-23T10:45:06.972075",
#             "operationAmount": {
#                 "amount": "48223.05",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#
#             "to": "Счет 41421565395219882431"
#         },
#     ]
#     print(filter_by_operations(transact, 'открытие'))
