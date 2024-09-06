import pytest

from src.wedget import get_date, mask_account_card


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Visa Classic 70007922еннр", "Некорректный номер карты"),
        ("Мир 700079225748675423412", "Некорректный номер карты"),
        ("счет 64686473678896564231214559", "Некорректный номер счета"),
        ("Счет 0", "Некорректный номер счета"),
        ("", "0"),
    ],
)
def test_mask_account_card_invalid_input(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Мир 7000792289606361", "Мир 7000 79** **** 6361"),
        ("корреспондентский счет 73654108430135874305", "корреспондентский счет **4305"),
        ("Расчетный счет 73654108430135874305", "Расчетный счет **4305"),
    ],
)
def test_mask_account_card_types_of_account(account_card, expected):
    assert mask_account_card(account_card) == expected


def test_mask_account_card_number_input():
    with pytest.raises(AttributeError):
        mask_account_card(464589456456)


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "date, expected",
    [
        ("", ""),
        ("0", "0"),
        (" ", " "),
    ],
)
def test_get_date_not_date(date, expected):
    assert get_date(date) == expected


@pytest.fixture()
def expected_data():
    return "11.03.2024"


@pytest.mark.parametrize(
    "date",
    [
        ("2024-03-11T02:26:18.671407"),
        ("2024-03-11"),
        ("2024-03-11T02:26:18"),
        ("2024-03-11 02:26:18.671407"),
    ],
)
def test_get_date_success(date, expected_data):
    assert get_date(date) == expected_data
