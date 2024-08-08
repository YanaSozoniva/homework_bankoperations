import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [(7000792289606361, "7000 79** **** 6361"),
                                                   ("7000792289606361", "7000 79** **** 6361"),
                                                   ])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number, expected", [(0, '0'),
                                                   ("0", '0'),
                                                   ("", '0')
                                                   ])
def test_get_mask_card_number_zero_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.fixture()
def expected():
    return "Некорректный номер карты"
@pytest.mark.parametrize("card_number", [(70007922896),
                                        ("70007922896063612233"),
                                        ("1544вполло")])
def test_get_mask_card_number_length(card_number, expected):
    assert get_mask_card_number(card_number) == expected
