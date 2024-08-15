import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        ("7000792289606361", "7000 79** **** 6361"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number, expected", [(0, "0"), ("0", "0"), ("", "0")])
def test_get_mask_card_number_zero_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.fixture()
def expected():
    return "Некорректный номер карты"


@pytest.mark.parametrize("card_number", [(70007922898), ("700079228960636122333489789745"), ("1544вполло")])
def test_get_mask_card_number_length(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == "**4305"


@pytest.fixture()
def expected_account():
    return "Некорректный номер счета"


@pytest.mark.parametrize(
    "account",
    [
        (70007922896),
        ("73654108430135874305265454"),
        ("8574874вполло"),
        (0),
        (""),
    ],
)
def test_get_mask_account_length(account, expected_account):
    assert get_mask_account(account) == expected_account
