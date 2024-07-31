from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция принимает информацию о карте/счете и возвращает их маску"""

    list_card_info = card_info.split(" ")
    if list_card_info[0].lower() == "счет":
        list_card_info[-1] = get_mask_account(list_card_info[-1])
    else:
        list_card_info[-1] = get_mask_card_number(list_card_info[-1])

    return " ".join(list_card_info)


def get_date(date: str) -> str:
    """Функция принимает на вход дату в формате "2024-03-11T02:26:18.671407" и возвращает - в формате 'ДД.ММ.ГГГГ'"""
    list_date = date.split("-", 4)
    list_date[-1] = list_date[-1][:2]

    return ".".join(list_date[::-1])


print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
