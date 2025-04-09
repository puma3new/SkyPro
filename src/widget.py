import masks

def mask_account_card(card_number: str) -> str:
    """Шифрует данные банковской карты или счёта при помощи masks.py"""
    # Разделяем текстовую часть и цифры
    text = ''.join(filter(lambda x: x.isalpha() or x.isspace(), card_number))
    digits = ''.join(filter(str.isdigit, card_number))
    digits = int(digits)
    
    # Проверяем наличие слов "Счёт" или "Счет" в текстовой части
    if "Счёт" in text or "Счет" in text:
        return masks.get_mask_account(digits)
    else:
        return masks.get_mask_card_number(digits)