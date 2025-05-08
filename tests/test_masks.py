import pytest

from src import masks


@pytest.mark.parametrize(
    "card, expected",
    [("7000792289606361", "7000 79** **** 6361"), ("1234", "1234 **** **")],
)
def test_get_mask_card_number(card, expected):
    assert masks.get_mask_card_number(card) == expected


@pytest.mark.parametrize(
    "account, expected", [("73654108430135874305", "**4305"), ("1234", "**1234")]
)
def test_get_mask_account(account, expected):
    assert masks.get_mask_account(account) == expected
