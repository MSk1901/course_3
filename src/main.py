# Импортируем функции из utils.py
from utils import get_transactions, prepare_data, sort_by_date, get_first_five, fix_date, check_from, make_numbers

# Получаем список транзакций, фильтруем и сортируем его, получаем первые 5 элементов
if __name__ == "__main__":
    trans_list = get_transactions()
    correct_list = prepare_data(trans_list)
    sorted_list = sort_by_date(correct_list)
    five_transactions = get_first_five(sorted_list)

# Запускаем цикл по списку транзакций для вывода каждой из них
    for trans in five_transactions:
        from_field = check_from(trans)
        if from_field is None:
            masked_from = ""
        else:
            masked_from = make_numbers(from_field)

# Выводим данные о транзакции в необходимом формате
        print(f"""{fix_date(trans["date"])} {trans["description"]}
{masked_from} -> {make_numbers(trans["to"])}
{trans["operationAmount"]["amount"]} {trans["operationAmount"]["currency"]["name"]}\n""")
