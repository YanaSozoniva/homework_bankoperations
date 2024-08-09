def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, у которых ключ
    state соответствует указанному значению"""

    new_list = [item for item in list_dict if item["state"] == state.upper()]

    return new_list


def sort_by_date(list_dict: list, revers: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате
    (по умолчанию - сортируется по убыванию)"""

    sorted_list = sorted(list_dict, key=lambda operation: operation["date"], reverse=revers)

    return sorted_list


# my_list =[
#              {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#              {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#              {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#              {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#          ]
# filter_list = filter_by_state(my_list)
# print (filter_list)
# filter_list = filter_by_state(my_list, "CANCELED")
# print (filter_list)
# filter_list = sort_by_date(my_list)
# print (filter_list)
# filter_list = sort_by_date(my_list, False)
# print (filter_list)
