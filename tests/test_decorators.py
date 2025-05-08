import os

import pytest

from src.decorators import log
from src.masks import get_mask_card_number


# Тестовая функция для проверки консольного вывода
@log()
def mask_card_console(card_number: int) -> str:
    return get_mask_card_number(card_number)


# Тестовая функция для проверки записи в файл (успешный случай)
@log("tests/test_success.log")
def mask_card_file_success(card_number: int) -> str:
    return get_mask_card_number(card_number)


# Тестовая функция для проверки записи ошибок
@log("tests/test_error.log")
def mask_card_file_error(card_number: int) -> str:
    if len(str(card_number)) < 8:
        raise ValueError("Номер карты слишком короткий")
    return get_mask_card_number(card_number)


def test_console_logging(capsys, card):
    """Тестируем вывод в консоль"""
    result = mask_card_console(card)

    captured = capsys.readouterr()
    output = captured.out

    assert "mask_card_console начата" in output
    assert "mask_card_console завершена" in output
    assert "1111 22** **** 4444" in output  # Проверяем маскированный номер
    assert result == "1111 22** **** 4444"


def test_file_logging_success(card):
    """Тестируем запись успешного выполнения В файл"""
    # Удаляем старый лог-файл если есть
    if os.path.exists("tests/test_success.log"):
        os.path.exists("tests/test_success.log")

    result = mask_card_file_success(card)

    # Проверяем что файл создан
    assert os.path.exists("tests/test_success.log")

    # Читаем содержимое файла
    with open("tests/test_success.log", "r", encoding="utf-8") as f:
        content = f.read()

    # Проверяем содержимое
    assert "mask_card_file_success начата" in content
    assert "mask_card_file_success завершена" in content
    assert "1111 22** **** 4444" in content
    assert result == "1111 22** **** 4444"


def test_file_logging_error(card):
    """Тестируем запись ошибки в файл"""
    # Удаляем старый лог-файл если есть
    if os.path.exists("tests/test_error.log"):
        os.path.exists("tests/test_error.log")

    with pytest.raises(ValueError):
        mask_card_file_error("123")  # Слишком короткий номер карты

    # Проверяем что файл создан
    assert os.path.exists("tests/test_error.log")

    # Читаем содержимое файла
    with open("tests/test_error.log", "r", encoding="utf-8") as f:
        content = f.read()

    # Проверяем содержимое
    assert "mask_card_file_error начата" in content
    assert "Ошибка в функции mask_card_file_error" in content
    assert "ValueError" in content
    assert "Номер карты слишком короткий" in content
    assert "args: ('123',)" in content
