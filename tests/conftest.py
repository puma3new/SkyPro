from typing import Dict, List

import pytest


# widget.py
# masks.py
# ========
@pytest.fixture
def card():
    return "1111222233334444"


@pytest.fixture
def account():
    return "73654108430135874305"


# processing.py
# ========


@pytest.fixture
def date():
    return "2024-01-01T00:00:00.671407"


@pytest.fixture
def test_state():
    state = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return state


# generators.py
@pytest.fixture
def transactions():
    """Фикстура из задания"""
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    return transactions


# sheets_reader.py
@pytest.fixture
def csv_transaction_data() -> str:
    """Фикстура: тестовые данные CSV в виде строки с разделителем ';'

    Returns:
        str: CSV-данные с двумя транзакциями (PENDING и EXECUTED)
    """
    return """id;state;date;amount;currency_name;currency_code;from;to;description
2130098;PENDING;2020-06-07T11:11:36Z;30731;Euro;EUR;Visa 5749750597771353;American Express 9106381490184499;Перевод с карты на карту
41428829;EXECUTED;2019-07-03T18:35:29.512364;8221.37;US Dollar;USD;MasterCard 7158300734726758;Счет 35383033474447895560;Перевод организации
"""


@pytest.fixture
def expected_transactions() -> List[Dict[str, str]]:
    """Фикстура: ожидаемый результат парсинга CSV

    Returns:
        List[Dict[str, str]]: Список словарей с транзакциями в том же порядке, что и в CSV
    """
    return [
        {
            "id": "2130098",
            "state": "PENDING",
            "date": "2020-06-07T11:11:36Z",
            "amount": "30731",
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "Visa 5749750597771353",
            "to": "American Express 9106381490184499",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "41428829",
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "amount": "8221.37",
            "currency_name": "US Dollar",
            "currency_code": "USD",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
            "description": "Перевод организации",
        },
    ]


@pytest.fixture
def excel_transaction_data() -> List[Dict[str, object]]:
    """Фикстура: тестовые данные для Excel (типы значений соответствуют pandas-парсингу)

    Returns:
        List[Dict[str, object]]: Список словарей с транзакциями (числа как float/int)
    """
    return [
        {
            "id": 2130098,  # pandas читает как int
            "state": "PENDING",
            "date": "2020-06-07T11:11:36Z",
            "amount": 30731.0,  # pandas читает как float
            "currency_name": "Euro",
            "currency_code": "EUR",
            "from": "Visa 5749750597771353",
            "to": "American Express 9106381490184499",
            "description": "Перевод с карты на карту",
        }
    ]
