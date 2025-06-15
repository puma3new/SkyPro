# tests/test_external_api.py
import pytest
from unittest.mock import patch, mock_open
from src.external_api import check_amount

transaction_rub = {
    'operationAmount': {
        'amount': '1000',
        'currency': {'code': 'RUB'}
    }
}

transaction_usd = {
    'operationAmount': {
        'amount': '100',
        'currency': {'code': 'USD'}
    }
}

transaction_unknown = {
    'operationAmount': {
        'amount': '500',
        'currency': {'code': 'JPY'}
    }
}

@patch("src.external_api.os.getenv", return_value="fake_api_key")
@patch("src.external_api.requests.get")
@patch("src.external_api.load_dotenv")
def test_check_amount_usd(mock_dotenv, mock_get, mock_getenv):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
    'result': 9100.0,
    'query': {'amount': 100, 'from': 'USD', 'to': 'RUB'}
    }
    result = check_amount(transaction_usd)
    assert result == 9100.0

def test_check_amount_rub():
    result = check_amount(transaction_rub)
    assert result == 1000.0

def test_check_amount_unknown(capsys):
    result = check_amount(transaction_unknown)
    captured = capsys.readouterr()
    assert "неизвестная валюта" in captured.out
    assert result is None
