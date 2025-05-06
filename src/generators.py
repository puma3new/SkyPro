from typing import Dict, Iterator, List

def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор.

    :param transactions: Список словарей с транзакциями
    :param currency: Валюта для фильтрации (например, "USD")
    :return: Итератор, возвращающий транзакции с указанной валютой
    """
    return (transaction for transaction in transactions if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency)

def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, который возвращает описания транзакций по очереди.
    
    :param transactions: Список словарей с транзакциями
    :return: Итератор, возвращающий описания транзакций
    """
    for transaction in transactions:
        yield transaction.get('description', 'Нет описания')

def card_number_generator(start: int = 1, end: int = 9999_9999_9999_9999) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    
    :param start: Начальное значение (1 по умолчанию)
    :param end: Конечное значение (9999999999999999 по умолчанию)
    :yield: Номер карты в формате XXXX XXXX XXXX XXXX
    """
    if start > end:
        raise ValueError("Start cannot be greater than end")
    for number in range(start, end + 1):
        # Форматируем число в 16-значную строку с ведущими нулями
        card_str = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
