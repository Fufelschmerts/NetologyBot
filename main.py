import random
import telebot

# Телеграм бот на Питоне по бесплатному курсу от Нетологии

token = 'token telegram bot'

bot = telebot.TeleBot(token)

HELP = '''
/help - показать инфу о Боте
/add [дата] [задача] - добавить задачу в список на определенную дату
/show [дата] - показать добавленные задачи на определенный день
/exit - остановить Бота
/print - показать все задачи
/random - добавить случайную задачу на сегодня
'''

TODAY_TASKS = list()
TOMORROW_TASKS = list()
OTHER_TASKS = dict()

RANDOM_TASKS = ['Позвонить в сервис', 'Купить хлеб', 'Захватить мир', 'Посмотреть сериал', 'Поиграть в игру']


# @bot.message_handler(commands=['show'])
# def command_show(message):
#     bot.send_message(message.chat.id, 'Введите дату')


@bot.message_handler(commands=['show'])
def command_show(message):
    bot.send_message(message.chat.id, 'Введите дату')


# @bot.message_handler(func=lambda message: True)
# def show_tasks(message):
#     message_array = message.text.lower().split()
#     print(message_array)
#     if 'сегодня' in message_array or 'today' in message_array:
#         if not TODAY_TASKS:
#             bot.send_message(message.chat.id, "Задач на сегодня нет")
#         else:
#             bot.send_message(message.chat.id, f"Задачи на сегодня:\n{'\n'.join(TODAY_TASKS)}")
#     elif 'завтра' in message_array or 'tomorrow' in message_array:
#         if not TOMORROW_TASKS:
#             bot.send_message(message.chat.id, "Задач на завтра нет")
#         else:
#             bot.send_message(message.chat.id, f"Задачи на завтра:\n{'\n'.join(TOMORROW_TASKS)}")
#     else:
#         for date in OTHER_TASKS:
#             if date in message_array:
#                 bot.send_message(message.chat.id, f"Задачи на {date}:\n📌{OTHER_TASKS[date]}")
#                 break
#         else:
#             bot.send_message(message.chat.id, f"Задач на {message.text} нет")
#     return

@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['exit'])
def command_exit(message):
    bot.send_message(message.chat.id, 'Спасибо за использование, очишение и выход')
    return bot.stop_polling()


def add_other_todo(date, task):
    if date in OTHER_TASKS:
        OTHER_TASKS[date] += f', {task}'
    else:
        OTHER_TASKS[date] = task


@bot.message_handler(commands=['add', 'random'])
def handle_add_random(message):
    command = message.text.split(maxsplit=2)
    if message.text.startswith('/add'):
        date = command[1].lower()
        task = command[2]
        print(command)
        if date == 'сегодня' or date == 'today':
            TODAY_TASKS.append(f'📌{task}')
        elif date == 'завтра' or date == 'tomorrow':
            TOMORROW_TASKS.append(f'📌{task}')
        else:
            add_other_todo(date, task)
        bot.send_message(message.chat.id, f'Задача "{task}" на {date} добавлена')
    if message.text == '/random':
        task = random.choice(RANDOM_TASKS)
        TODAY_TASKS.append(f'📌{task}')
        bot.send_message(message.chat.id, f'Задача "{task}" на сегодня добавлена')
    return


@bot.message_handler(commands=['print'])
def command_show_all(message):
    if not TODAY_TASKS and not TOMORROW_TASKS and OTHER_TASKS == {}:
        bot.send_message(message.chat.id, "Задач нет")
    if TODAY_TASKS:
        bot.send_message(message.chat.id, f"Задачи на сегодня:\n{'\n'.join(TODAY_TASKS)}")
    if TOMORROW_TASKS:
        bot.send_message(message.chat.id, f"Задачи на завтра:\n{'\n'.join(TOMORROW_TASKS)}")
    if OTHER_TASKS:
        bot.send_message(message.chat.id, f"Другие даты:\n📌{'\n📌'.join([f'{key}: {value}' for key, value in OTHER_TASKS.items()])}")
    return


@bot.message_handler(content_types=['text'])
def dialog(message):
    message_array = message.text.lower().split()  # разделяем сообщение на слова
    if 'иван' in message_array:
        bot.send_message(message.chat.id, 'Ба! Знакомые все лица!')
    if 'сегодня' in message_array or 'today' in message_array:
        if not TODAY_TASKS:
            bot.send_message(message.chat.id, "Задач на сегодня нет")
        else:
            bot.send_message(message.chat.id, f"Задачи на сегодня:\n{'\n'.join(TODAY_TASKS)}")
    elif 'завтра' in message_array or 'tomorrow' in message_array:
        if not TOMORROW_TASKS:
            bot.send_message(message.chat.id, "Задач на завтра нет")
        else:
            bot.send_message(message.chat.id, f"Задачи на завтра:\n{'\n'.join(TOMORROW_TASKS)}")
    else:
        for date in OTHER_TASKS:
            if date in message_array:
                bot.send_message(message.chat.id, f"Задачи на {date}:\n📌{OTHER_TASKS[date]}")
                break
        else:
            bot.send_message(message.chat.id, f"Задач на {message.text} нет")
    return


# #  Задание написать ф-ю для подсчета количества слов с этой буквой
#
# task_array = ['Позвонить в сервис', 'Купить хлеб', 'Захватить мир', 'Посмотреть сериал', 'Поиграть в игру']
#
#
# def count_letter(words_list, letter):
#     result = 0
#     for word in words_list:
#         if letter in word:
#             result += 1
#     return result
#
#
# print(count_letter(task_array, 'а'))


# функция для случайной задачи


#
# while is_running:
#     command = input('Введите команду: ')
#     if command.lower() == 'help':
#         print(HELP)
#         continue
#     elif command.lower() == '':
#         print('Вы не ввели команду!')
#         continue
#     elif command.lower() == 'add':
#         date = input("Введите дату: ")
#         task = input("Введите задачу: ")
#         if date == '':
#             print('Вы не ввели дату!')
#             continue
#         elif date.lower() == 'сегодня' or date.lower() == 'today':
#             today_task.append(f'📌{task}')
#         elif date.lower() == 'завтра' or date.lower() == 'tomorrow':
#             tomorrow_task.append(f'📌{task}')
#         else:
#             add_other_todo(date, task)
#         print(f'Задача "{task}" на {date} добавлена')
#         continue
#     elif command == 'show':
#         date = input("Введите дату задач: ")
#         if date == '':
#             print('Вы не ввели дату!')
#             continue
#         elif date.lower() == 'сегодня' or date.lower() == 'today':
#             if not today_task:
#                 print("Задач на сегодня нет")
#             else:
#                 print(f"Задачи на сегодня:\n{'\n'.join(today_task)}")
#                 continue
#         elif date.lower() == 'завтра' or date.lower() == 'tomorrow':
#             if not tomorrow_task:
#                 print('Задач на завтра нет')
#             else:
#                 print(f"Задачи на завтра:\n{'\n'.join(tomorrow_task)}")
#                 continue
#         else:
#             if date in other_task:
#                 print(f"Задачи на {date}:\n📌{other_task[date]}")
#                 continue
#             else:
#                 print(f"Задач на {date} нет")
#     elif command == 'show all':
#         if not today_task and not tomorrow_task and other_task == {}:  # Проверка на пустые списки
#             print("Задач нет")
#         if today_task:
#             print(f"Задачи на сегодня:\n{'\n'.join(today_task)}")
#         if tomorrow_task:
#             print(f"Задачи на завтра:\n{'\n'.join(tomorrow_task)}")
#         if other_task:
#             print(f"Другие даты:\n📌{'\n📌'.join([f'{key}: {value}' for key, value in other_task.items()])}")
#     elif command.lower() == 'random':
#         print("Случайная задача добавлена!")
#         today_task.append(f'📌{random_task()}')
#     elif command.lower() == 'exit':
#         print('Спасибо за использование! И до свидания!')
#         break
#     else:
#         print("Неизвестная команда! Введите help, чтобы узнать список доступных команд.")
#         continue
#
# print('Заходите ещё!')


# Постоянно обращаемся к серверам телеграм
bot.polling(none_stop=True)
