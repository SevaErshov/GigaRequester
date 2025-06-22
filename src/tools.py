import sqlite3

from typing import Dict, List, Tuple
from langchain.tools import tool


database = {
    "schema": "crm",
    "tables": {
        "customers": {
            "description": "Содержит общую информацию о клиентах.",
            "columns": {
                "customer_id": "Целочисленный идентификатор клиента.",
                "first_name": "Имя клиента (строка).",
                "last_name": "Фамилия клиента (строка).",
                "birth_year": "Год рождения клиента (целое число).",
                "registration_year": "Год регистрации в системе (целое число)."
            }
        },
        "contacts": {
            "description": "Контактная информация клиентов.",
            "columns": {
                "contact_id": "Целочисленный идентификатор записи контакта.",
                "customer_id": "Целочисленный ID клиента, к которому относится контакт.",
                "email": "Электронная почта (строка).",
                "phone": "Номер телефона (строка)."
            }
        },
        "purchases": {
            "description": "Информация о покупках клиентов.",
            "columns": {
                "purchase_id": "Целочисленный идентификатор записи о покупке.",
                "customer_id": "Целочисленный ID клиента, который совершил покупку.",
                "purchase_year": "Год покупки (целое число).",
                "amount_rub": "Сумма покупки в рублях (целое число).",
                "product_type": "Тип продукта (строка)."
            }
        }
    }
}


@tool
def get_all_table_descriptions() -> str:
    """Возвращает названия всех таблиц в базе данных и их описание"""
    print("\033[92m" + "Бот запросил информацию о таблицах" + "\033[0m")
    all_tables = database['tables']
    return " | ".join([f'Таблица: {table_name}, Описание: {table_info["description"]}' for table_name, table_info in all_tables.items()])


@tool
def get_table_info(table_name: str) -> Dict:
    """Возвращает список полей и их описание для указанной таблицы"""
    print("\033[92m" + "Бот запросил информацию о списке полей в таблице" + "\033[0m")
    if table_name not in database['tables']:
        raise ValueError(f"Таблица '{table_name}' не найдена в базе данных.")
    table_info = database['tables'][table_name]
    return table_info


@tool
def request_db(request: str):
    """По SQL-запросу возвращает результат запроса к базе данных в виде списка кортежей или сообщает о пустом результате"""
    print("\033[92m" + "Бот сделал запрос к базе данных" + "\033[0m")
    request = request.split(";")[0] + ";"
    conn = sqlite3.connect("db/crm.db")
    cursor = conn.cursor()

    cursor.execute(request)
    result = cursor.fetchall()
    conn.close()
    if not result:
        return 'Результат запроса пустой. Проверьте правильность запроса.'
    return result


@tool
def check_values(column: str, table: str) -> List[Tuple]:
    """Функция для проверки значений в столбце таблицы. По заданному столбцу возвращает список уникальных значений в этом столбце
        Args: column: Название столбца, table: Название таблицы
        Returns: Список уникальных значений в столбце
    """
    print("\033[92m" + "Бот сделал проверил значения полей" + "\033[0m")
    request = f'select distinct {column} from {table};'
    conn = sqlite3.connect("db/crm.db")
    cursor = conn.cursor()

    cursor.execute(request)
    result = cursor.fetchall()
    conn.close()
    if not result:
        return 'Результат запроса пустой. Проверьте правильность запроса.'
    return result
