import csv
from typing import Dict, List

import pandas as pd


def read_csv_transactions(route_to_csv: str) -> List[Dict]:
    """Функция для чтения данных о банковских операциях из CSV"""
    readed_csv_transactions = []
    with open(route_to_csv, newline="", encoding='utf-8') as trans_csv:
        reader = csv.DictReader(
            trans_csv, delimiter=";"
        )  # Сохраняем первую строку с названиями столбцов
        for row in reader:  # Сохраняем построчно содержимое таблицы в список словарей
            readed_csv_transactions.append(row)
    return readed_csv_transactions


def read_excel_transactions(route_to_excel: str) -> List[Dict]:
    """Функция для чтения данных о банковских операциях из Excel"""
    excel_transactions = pd.read_excel(route_to_excel)
    readed_excel_transactions = excel_transactions.to_dict("records")
    return readed_excel_transactions
