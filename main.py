import random

# Телеграм бот на Питоне по бесплатному курсу от Нетологии

# Практика 1. Запрос данных у пользователей.

HELP = '''
help - показать инфу о Боте
add - добавить задачу в список (запросить у пользователя)
show - показать добавленные задачи на определенный день
exit - остановить Бота
show all - показать все задачи
random - добавить случайную задачу на сегодня
'''


#  Задание написать ф-ю для подсчета количества слов с этой буквой

task_array = ['Позвонить в сервис', 'Купить хлеб', 'Захватить мир', 'Посмотреть сериал', 'Поиграть в игру']


def count_letter(words, letter):
    result = 0
    for word in words:
        if letter in word:
            result += 1
    return result


print(count_letter(task_array, 'а'))

# функция для случайной задачи
def random_task():
    tasks = ['Позвонить в сервис', 'Купить хлеб', 'Захватить мир', 'Посмотреть сериал', 'Поиграть в игру']
    return random.choice(tasks)


today_task = list()
tomorrow_task = list()
other_task = dict()

is_running = True


def add_other_todo(date, task):
    if date in other_task:
        other_task[date] += f', {task}'
    else:
        other_task[date] = task


while is_running:
    command = input('Введите команду: ')
    if command.lower() == 'help':
        print(HELP)
        continue
    elif command.lower() == '':
        print('Вы не ввели команду!')
        continue
    elif command.lower() == 'add':
        date = input("Введите дату: ")
        task = input("Введите задачу: ")
        if date == '':
            print('Вы не ввели дату!')
            continue
        elif date.lower() == 'сегодня' or date.lower() == 'today':
            today_task.append(f'📌{task}')
        elif date.lower() == 'завтра' or date.lower() == 'tomorrow':
            tomorrow_task.append(f'📌{task}')
        else:
            add_other_todo(date, task)
        print(f'Задача "{task}" на {date} добавлена')
        continue
    elif command == 'show':
        date = input("Введите дату задач: ")
        if date == '':
            print('Вы не ввели дату!')
            continue
        elif date.lower() == 'сегодня' or date.lower() == 'today':
            if not today_task:
                print("Задач на сегодня нет")
            else:
                print(f"Задачи на сегодня:\n{'\n'.join(today_task)}")
                continue
        elif date.lower() == 'завтра' or date.lower() == 'tomorrow':
            if not tomorrow_task:
                print('Задач на завтра нет')
            else:
                print(f"Задачи на завтра:\n{'\n'.join(tomorrow_task)}")
                continue
        else:
            if date in other_task:
                print(f"Задачи на {date}:\n📌{other_task[date]}")
                continue
            else:
                print(f"Задач на {date} нет")
    elif command == 'show all':
        if not today_task and not tomorrow_task and other_task == {}:  # Проверка на пустые списки
            print("Задач нет")
        if today_task:
            print(f"Задачи на сегодня:\n{'\n'.join(today_task)}")
        if tomorrow_task:
            print(f"Задачи на завтра:\n{'\n'.join(tomorrow_task)}")
        if other_task:
            print(f"Другие даты:\n📌{'\n📌'.join([f'{key}: {value}' for key, value in other_task.items()])}")
    elif command.lower() == 'random':
        print("Случайная задача добавлена!")
        today_task.append(f'📌{random_task()}')
    elif command.lower() == 'exit':
        print('Спасибо за использование! И до свидания!')
        break
    else:
        print("Неизвестная команда! Введите help, чтобы узнать список доступных команд.")
        continue

print('Заходите ещё!')
