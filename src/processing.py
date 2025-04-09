from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)."""
    return sorted(data, key=lambda x: x.get("date", ""), reverse=descending)
