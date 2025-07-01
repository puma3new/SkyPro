from typing import Dict, List
from unittest.mock import MagicMock, mock_open, patch

import pandas as pd

from src import sheets_reader


def test_read_csv_transactions(
    csv_transaction_data: str, expected_transactions: List[Dict[str, str]]
) -> None:
    """Тест для read_csv_transactions: проверка корректности парсинга CSV

    Args:
        csv_transaction_data: Фикстура с тестовыми CSV-данными
        expected_transactions: Фикстура с ожидаемым результатом

    Тестируем:
    1. Корректное открытие файла с правильными параметрами
    2. Правильное чтение данных с учетом разделителя ;
    3. Полное соответствие выходных данных ожидаемому результату
    """
    # 1. Мокаем open() и DictReader
    with patch(
        "builtins.open", mock_open(read_data=csv_transaction_data)
    ) as mocked_file:
        # 2. Создаем мок для DictReader
        mock_reader = MagicMock()
        mock_reader.return_value = expected_transactions

        with patch("csv.DictReader", mock_reader):
            # 3. Вызов тестируемой функции
            result = sheets_reader.read_csv_transactions("dummy.csv")

            # 4. Проверки
            mocked_file.assert_called_once_with(
                "dummy.csv", newline="", encoding="utf-8"
            )
            mock_reader.assert_called_once_with(mocked_file.return_value, delimiter=";")
            assert result == expected_transactions
            assert len(result) == 2
            assert result[0]["currency_code"] == "EUR"
            assert result[1]["amount"] == "8221.37"


def test_read_excel_transactions(
    excel_transaction_data: List[Dict[str, object]],
) -> None:
    """Тест для read_excel_transactions: проверка чтения Excel

    Args:
        excel_transaction_data: Фикстура с тестовыми данными Excel

    Тестируем:
    1. Корректность вызова pd.read_excel
    2. Конвертацию DataFrame в список словарей
    3. Сохранение типов данных (числа остаются числами)
    """
    # 1. Создаем тестовый DataFrame
    mock_df = pd.DataFrame(excel_transaction_data)

    # 2. Мокаем pandas.read_excel
    with patch("pandas.read_excel", return_value=mock_df) as mocked_excel:
        # 3. Вызов тестируемой функции
        result = sheets_reader.read_excel_transactions("dummy.xlsx")

        # 4. Проверки
        mocked_excel.assert_called_once_with("dummy.xlsx")
        assert len(result) == 1
        assert result[0]["id"] == 2130098
        assert isinstance(result[0]["amount"], float)
        assert result[0]["description"] == "Перевод с карты на карту"


def test_empty_csv_file() -> None:
    """Тест на обработку пустого CSV файла"""
    # 1. Мокаем пустой файл
    with patch("builtins.open", mock_open(read_data="")) as mocked_file:
        # 2. Мокаем DictReader для пустого файла
        with patch("csv.DictReader", return_value=[]):
            # 3. Вызов и проверка
            result = sheets_reader.read_csv_transactions("empty.csv")
            assert result == []
            mocked_file.assert_called_once_with(
                "empty.csv", newline="", encoding="utf-8"
            )


def test_csv_with_wrong_delimiter() -> None:
    """Тест на обработку CSV с неправильным разделителем"""
    # 1. Подготовка данных с запятыми вместо точек с запятой
    bad_data = "id,state,date\n1,PENDING,2020-01-01"

    # 2. Мокаем файл
    with patch("builtins.open", mock_open(read_data=bad_data)):
        # 3. Вызов и проверка
        result = sheets_reader.read_csv_transactions("bad.csv")
        # Ожидаем либо пустой список, либо список с одним элементом (всей строкой)
        assert len(result) <= 1
