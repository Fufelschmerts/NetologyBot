# Телеграм бот на Питоне по бесплатному курсу от Нетологии

# Практика 1. Запрос данных у пользователей.

HELP = '''
help - показать инфу о Боте
add - добавить задачу в список (запросить у пользователя)
show - показать добавленные задачи
exit - остановить Бота
'''

today = {}
tomorrow = {}
other = {}

run = True

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'add':
        data = input("Введите дату: ")
        task = input("Введите задачу: ")
        if data == 'Сегодня':
            today[data] = task
        elif data.lower() == 'завтра':
            tomorrow[data] = task
        else:
            other[data] = task
        print(f'Задача "{task}" добавлена')
    elif command == 'show':
        if today == {}:
            print('Задач на сегодня нет')
        else:
            print('Задачи на сегодня: ', today)
        if tomorrow == {}:
            print('Задач на завтра нет')
        else:
            print('Задачи на завтра: ', tomorrow)
        if other == {}:
            print('Задач на другие даты нет')
        else:
            print('Другие даты: ', other)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда')
        break

print('Заходите ещё!')

# todo_dic = {}  # Создаем пустой словарь
#
# for i in range(3):  # Запрашиваем данные у пользователя 3 раза
#     data = input("Введите дату: ")
#     todo = input("Введите задачу: ")
#     todo_dic[data] = todo  # Записываем данные в словарь
#
# print(todo_dic)
