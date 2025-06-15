import logging

logger = logging.getLogger("__name__")
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s at %(name)s: %(levelname)s - %(message)s"
)
logger.addHandler(file_handler)
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Определяет маску карты (out) по её номеру (in)"""
    try:
        logger.debug(f"Запущена функция 'get_mask_card_number' со входом {card_number}")
        crypted_card_number = str(card_number)[:6] + "******" + str(card_number)[12:]
        formatted_card_number = " ".join(
            crypted_card_number[i : i + 4]
            for i in range(0, len(crypted_card_number), 4)
        )
        logger.debug(
            f"Функция 'get_mask_card_number'' успешно отработала. Результат: {formatted_card_number}"
        )
        return formatted_card_number
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


def get_mask_account(account_number: int) -> str:
    """Определяет маску счёта (out) по его номеру (in)"""
    try:
        logger.debug(f"Запущена функция 'get_mask_account' со входом: {account_number}")
        crypted_account_number = "**" + str(account_number)[-4:]
        logger.debug(
            f"Функция 'get_mask_account' успешно отработала. Результат: {crypted_account_number}"
        )
        return crypted_account_number
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
