import pytest

from src.wedget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"


@pytest.mark.parametrize("account_card, expected",
                         [("Visa Classic 70007922еннр", "Некорректный номер карты"),
                          ("Мир 700079225748675423412", "Некорректный номер карты"),
                          ("счет 64686473678896564231214559", "Некорректный номер счета"),
                          ("Счет 0", "Некорректный номер счета"),
                          ("", "0"),
                          ])
def test_mask_account_card_invalid_input(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize("account_card, expected",
                         [("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
                          ("Мир 7000792289606361", "Мир 7000 79** **** 6361"),
                          ("корреспондентский счет 73654108430135874305", "корреспондентский счет **4305"),
                          ("Расчетный счет 73654108430135874305", "Расчетный счет **4305"), ])
def test_mask_account_card_types_of_account(account_card, expected):
    assert mask_account_card(account_card) == expected


def test_mask_account_card_number_input():
    with pytest.raises(AttributeError):
        mask_account_card(464589456456)




