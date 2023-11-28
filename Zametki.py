# Словари - тестирую

dictionary = {
    'car': 'jeep',
    'city': 'Batumi'
}

# print(dictionary)
# print(dictionary['car'])

cars = {'Ford': ['Focus', "Scorpio", 'Mondeo'], 'Lexus': ['GLS', 'S300', 'Turbo'],
        'Porshe': ['911', 'Cayenne', 'Butilka']}

# Добавление ключа и его значений

# Добавление значе®ний в ключ
cars['Ford'].append('Fufel')

print(cars['Ford'])


USER_NAME = 'admin'

print(id(USER_NAME))

songs1 = {
    'Три белых коня',
    'Happy new year',
    'Снежинка'
}
songs2 = {
    'Last christmas',
    'Снежинка',
    'Happy new year'
}
print(songs2.intersection(songs1))

print(help(list))