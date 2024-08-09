from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    mask_card_str = str(card_number)

    if mask_card_str == "0" or mask_card_str == "":
        return "0"

    if mask_card_str.isalpha() or len(mask_card_str) < 16 or len(mask_card_str) > 16:
        return "Некорректный номер карты"

    return mask_card_str[:4] + " " + mask_card_str[4:6] + "** " + "*" * 4 + " " + mask_card_str[12:]


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account_number_str = str(account_number)

    if account_number_str.isalpha() or len(account_number_str) < 20 or len(account_number_str) > 20:
        return "Некорректный номер счета"

    account_mask = "**" + account_number_str[-4:]

    return account_mask
