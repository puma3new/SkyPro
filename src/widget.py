from datetime import datetime

from src import masks  # type: ignore


def mask_account_card(card_number: str) -> str:
    """Шифрует данные банковской карты или счёта при помощи masks.py"""
    # Разделяем текстовую часть и цифры
    text = "".join(filter(lambda x: x.isalpha() or x.isspace(), card_number))
    digits = "".join(filter(str.isdigit, card_number))

    # Проверяем наличие слов "Счёт" или "Счет" в текстовой части
    if "Счёт" in text or "Счет" in text:
        return str(masks.get_mask_account(int(digits)))
    else:
        return str(masks.get_mask_card_number(int(digits)))


def get_date(timestamp: str) -> str:
    """Преобразует дату из формата '2024-03-11T02:26:18.671407' в формат 'ДД.ММ.ГГГГ'."""
    date_obj = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
