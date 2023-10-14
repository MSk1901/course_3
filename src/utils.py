import json
from datetime import datetime


def get_transactions():
    """Считывает json файл"""
    with open("operations.json") as file:
        transactions = json.load(file)
        return transactions


def prepare_data(data: list):
    """Удаляет ненужные значение из списка"""
    return [operation for operation in data if operation.get('state') == "EXECUTED"]


def sort_by_date(data: list):
    """Сортирует список по дате операции (в начале более новые)"""
    return sorted(data, key=lambda x: x['date'], reverse=True)


def get_first_five(data: list):
    """Возвращает первые 5 элементов списка"""
    return data[:5]


def fix_date(date: str):
    """Приводит дату в нужный вид"""
    thedate = datetime.fromisoformat(date)
    return f"{thedate.day}.{thedate.month}.{thedate.year}"


def check_from(data: dict):
    """Проверяет наличие поля from"""
    from_data = data.get("from", None)
    if from_data is not None:
        return data["from"]
    return None


def make_numbers(data: str):
    """Приводит номер карты/счета в нужный вид"""
    if "Счет" in data:
        return f"{data[:5]}**{data[-4:]}"
    else:
        return f"{data[:-16]}{data[-16:-12]} {data[-12:-10]}** **** {data[-4:]}"


