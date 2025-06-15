import json
from typing import Dict, List


def get_operations_from_json(route_to_JSON: str) -> List[Dict]:
    """Получаем путь до JSON (на входе) и конвертируем JSON в Dict"""
    try:
        with open(route_to_JSON, "r", encoding="utf-8") as f:
            operations_data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {route_to_JSON} не найден")
    except json.JSONDecodeError:
        raise ValueError(f"Файл {route_to_JSON} содержит некорректный JSON")
    return operations_data
