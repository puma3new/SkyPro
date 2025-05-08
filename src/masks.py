def get_mask_card_number(card_number: int) -> str:
    """Определяет маску карты (out) по её номеру (in)"""
    crypted_card_number = str(card_number)[:6] + "******" + str(card_number)[12:]
    formatted_card_number = " ".join(
        crypted_card_number[i : i + 4] for i in range(0, len(crypted_card_number), 4)
    )
    return formatted_card_number


def get_mask_account(account_number: int) -> str:
    """Определяет маску счёта (out) по его номеру (in)"""
    crypted_account_number = "**" + str(account_number)[-4:]
    return crypted_account_number
