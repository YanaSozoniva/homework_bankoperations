from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    mask_card_str = str(card_number)

    return mask_card_str[:4] + " " + mask_card_str[4:6] + "** " + "*" * 4 + " " + mask_card_str[12:]


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    account_mask = "**" + str(account_number)[-4:]

    return account_mask


print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))
