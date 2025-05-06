import pytest
from src import generators


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 3),
    ("RUB", 2),
    ("EUR", 0),
])
def test_filter_by_currency(transactions, currency, expected_count):
    """Тест фильтрации транзакций по валюте"""
    filtered_transactions = list(generators.filter_by_currency(transactions, currency))
    assert len(filtered_transactions) == expected_count
    
def test_transaction_descriptions(transactions):
    """Тест генератора описаний транзакций"""
    result = list(generators.transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    assert result == expected
    
@pytest.mark.parametrize("start, end, expected_count", [
    (1, 5, 5),
    (9999, 10000, 2),
    (100, 103, 4),
])
def test_card_number_generator(start, end, expected_count):
    """Тест генератора номеров банковских карт"""
    result = list(generators.card_number_generator(start, end))
    assert len(result) == expected_count
    assert all(len(card.split()) == 4 for card in result)  # Проверка формата XXXX XXXX XXXX XXXX
    
@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
                {"description": "Перевод организации"},
                {"description": "Перевод организации"},
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
                "Перевод организации"
            ]
        ),
    ]
)
def test_description_extraction(transactions, expected_descriptions):
    """Тест для параметризации и генератора описаний"""
    result = list(generators.transaction_descriptions(transactions))
    assert result == expected_descriptions
