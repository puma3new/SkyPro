import json
from typing import Dict, List


def get_operations_from_json(route_to_JSON: str) -> List[Dict]:
    """Получает путь до JSON (на входе) и возвращает список операций (Dict).
    В случае ошибки чтения файла или декодирования — возвращает пустой список.
    """
    try:
        with open(route_to_JSON, "r", encoding="utf-8") as f:
            operations_data = json.load(f)
        return operations_data
    except FileNotFoundError:
        print(f"[Предупреждение] Файл не найден: {route_to_JSON}")
        return []
    except json.JSONDecodeError:
        print(f"[Предупреждение] Файл содержит некорректный JSON: {route_to_JSON}")
        return []
