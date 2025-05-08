import pytest

from src import widget


@pytest.mark.parametrize(
    "card, expected",
    [
        ("Maestro 1596837868705199", "1596 83** **** 5199"),
        ("Счет 64686473678894779589", "**9589"),
    ],
)
def test_mask_account_card(card, expected):
    assert widget.mask_account_card(card) == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        pytest.param(
            "2024-03-11T02:26:18", None, marks=pytest.mark.xfail(raises=ValueError)
        ),
    ],
)
def test_get_date(date, expected):
    assert widget.get_date(date) == expected
