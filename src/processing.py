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
