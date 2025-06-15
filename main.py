from src import utils, external_api

operations = utils.get_operations_from_json("/home/p3n/ПИТОН/SkyPro/data/operations.json")
print(f"Список:\n{operations[1]}")

amount = external_api.check_amount(operations[1])
