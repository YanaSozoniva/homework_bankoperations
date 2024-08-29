import logging
from typing import Union

path_dir = r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\logs"
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(path_dir + r"\masks_log.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s  %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    try:
        mask_card_str = str(card_number)
        if mask_card_str == "0" or mask_card_str == "":
            logger.info("Номер карты не был введен или равен нулю")
            return "0"

        if mask_card_str.isalpha() or len(mask_card_str) < 16 or len(mask_card_str) > 16:
            logger.info("Был введен не корректный номер карты (с символами или кол-во цифр больше/меньше 16")
            return "Некорректный номер карты"

        logger.info(f"Накладывается маска на номер карты {card_number}.")

        return mask_card_str[:4] + " " + mask_card_str[4:6] + "** " + "*" * 4 + " " + mask_card_str[12:]

    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    try:
        account_number_str = str(account_number)

        if account_number_str.isalpha() or len(account_number_str) < 20 or len(account_number_str) > 20:
            logger.info("Был введен не корректный номер счета (с символами или кол-во цифр больше/меньше 20")
            return "Некорректный номер счета"

        logger.info(f"Накладывается маска на номер счета {account_number}.")
        account_mask = "**" + account_number_str[-4:]

        return account_mask

    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")


# if __name__ == "__main__":
#     print(get_mask_account(73654108430135874305))
#     print(get_mask_card_number(7000792289606361))
