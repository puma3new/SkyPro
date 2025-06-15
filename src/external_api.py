import os
from pathlib import Path
from typing import Dict, List

import requests
from dotenv import load_dotenv


def check_amount(transaction: List[Dict]) -> float:
    """Возвращает валюту операции из переданного словаря. Если валюта не в рублях - конвертируем через внешний модуль в RUB."""
    currency_code = transaction["operationAmount"]["currency"]["code"]
    transaction_amount = float(transaction["operationAmount"]["amount"])

    if currency_code == "RUB":
        return transaction_amount  # если операция в рублях — возвращаем сразу

    if currency_code == "USD" or currency_code == "EUR":
        # если наша валюта - конвертируем
        # Загружаем переменные из .env в корне проекта
        env_path = (
            Path(__file__).parent.parent / "api_cred.env"
        )  # Поднимаемся на уровень выше к корню
        load_dotenv(env_path)

        # Получаем API-ключ
        API_KEY = os.getenv("EXCHANGE_API_KEY")
        if not API_KEY:
            raise ValueError("API ключ не найден в .env файле")

        # Формируем запрос
        url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
        headers = {"apikey": API_KEY}  # Используем ключ из переменной окружения

        # Пример использования
        params = {"to": "RUB", "from": currency_code, "amount": transaction_amount}

        try:
            response = requests.get(url.format(**params), headers=headers)
            response.raise_for_status()  # Проверка на ошибки HTTP

            result = response.json()
            converted_transaction_amount = result["result"]
            print(
                f"\nРезультат конвертации: {result}\n\nСумма: {converted_transaction_amount}"
            )
            return converted_transaction_amount  # возвращаем сумму операции (!) в RUB

        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return None  # возвращаем None в случае ошибки
    else:
        # если неизвестная валюта (не работаем с которой)
        print(f"В транзакции используется неизвестная валюта - {currency_code}")
        return None  # возвращаем None, чтобы избежать ошибки
