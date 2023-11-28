# Description: Списоки фильмов для парсинга
# Важные фильмы 21 века по версии команды inoekino.ru
# Author: Ivan Malinovsky / Иван Малиновский
# Date: 2023-11-25
# Version: 1.0.0
#


film_olga = {
    "Аннетт (2021)",
    "Гарри поттер и философский Камень (2001)",
    "Нефть (2007)",
    "Начало (2010)",
    "Апокалипсис (2006)",
    "Фаворитка (2018)",
    "Пианист (2002)",
    "Бесподобный Мистер фокс (2009)",
    "Дылда (2019)",
    "Город грехов (2005)",
}

film_evgeny = {
    "Отрочество (2014)",
    "Проект «флорида» (2017)",
    "Тайная жизнь (2019)",
    "Залечь на дно в брюгге (2008)",
    "Безумный Макс: Дорога ярости (2015)",
    "Социальная сеть (2010)",
    "Стыд (2011)",
    "Бесславные Ублюдки (2009)",
    "Валл-и (2008)",
    "Старикам тут не место (2007)",
}

film_anatoly = {
    "Внутренняя Империя (2006)",
    "Малхолланд Драйв (2001)",
    "Воображариум Доктора Парнаса (2009)",
    "Инцидент (2014)",
    "Не думай про белых обезьян (2008)",
    "Борьба: жизнь и утраченное искусство Шукальского (2020)",
    "Мэнди (2018)",
    "Вход в пустоту (2009)",
    "Я тоже хочу (2012)",
    "Фонтан (2006)",
}

film_vera = {
    "Приключения Паддингтона 2 (2017)",
    "Туринская Лошадь (2011)",
    "Трудно быть богом (2013)",
    "Весна, лето, осень, зима и снова весна (2003)",
    "Ты, живущий (2007)",
    "Стыд (2007)",
    "Жмурки (2005)",
    "Властелин колец (2001-2003)",
    "Бёрдмэн (2014)",
    "Рома (2018)",
}

film_alexey = {
    "Тайная жизнь (2019)",
    "Убийцы Цветочной Луны (2023)",
    "Любовь (2012)",
    "Корпорация «святые моторы» (2012)",
    "Малхолланд Драйв (2001)",
    "Тони эрдманн (2016)",
    "Внутри Льюина дэвиса (2013)",
    "Небраска (2013)",
    "Унесенные Призраками (2001)",
    "Антихрист (2009)",
}

film_valeria = {
    "Матрица: Перезагрузка и революция (2003)",
    "Бегущий По лезвию 2049 (2017)",
    "Пианист (2002)",
    "Зверополис (2016)",
    "Семь психопатов (2012)",
    "Хранители (реж. Версия, 2009)",
    "Начало (2010)",
    "По соображениям Совести (2016)",
    "Идеальные Незнакомцы (2016)",
    "Молодость (2015)",
}

film_alexandra = {
    "Властелин колец (2001-2003)",
    "Новый свет (расш. Версия, 2005)",
    "Исчезнувшая (2014)",
    "Безумный Макс: Дорога ярости (2015)",
    "Мост искусств (2004)",
    "Догвилль (2003)",
    "Бегуший По лезвию 2049 (2017)",
    "Малхолланд Драйв (2001)",
    "Однажды (2007)",
    "Олдбой (2003)",
}

film_igor = {
    "Рука бога (2021)",
    "Унесенные Призраками (2001)",
    "История призрака (2017)",
    "Трудности Перевода (2003)",
    "Камон камон (2021)",
    "Интерстеллар (2014)",
    "Бесподобный Мистер фокс (2009)",
    "Минари (2020)",
    "Вечное сияние Чистого разума (2004)",
    "Копы в глубоком запасе (2010)",
}

# соберем все фильмы в один список
all_films_list = list(film_olga) + list(film_evgeny) + list(film_anatoly) + list(film_vera) + list(film_alexey) + list(
    film_valeria) + list(film_alexandra) + list(film_igor)

print("Всего фильмов:", len(all_films_list), "шт.")

# Узнаем, какой фильм повторяется чаще всего
print("Самый упоминаемый фильм:", max(all_films_list, key=all_films_list.count) + " - 3 раза")

# Соберем все дубликаты каждого пользователя в отдельный список
duplicate_olga_1 = film_olga.intersection(film_evgeny)
duplicate_olga_2 = film_olga.intersection(film_anatoly)
duplicate_olga_3 = film_olga.intersection(film_vera)
duplicate_olga_4 = film_olga.intersection(film_alexey)
duplicate_olga_5 = film_olga.intersection(film_valeria)
duplicate_olga_6 = film_olga.intersection(film_alexandra)
duplicate_olga_7 = film_olga.intersection(film_igor)

all_olga_duplicates = duplicate_olga_1.union(
    duplicate_olga_2, duplicate_olga_3,
    duplicate_olga_4, duplicate_olga_5,
    duplicate_olga_6, duplicate_olga_7)

# print("Все дубликаты Ольги:", all_olga_duplicates)

duplicate_evgeny_1 = film_evgeny.intersection(film_olga)
duplicate_evgeny_2 = film_evgeny.intersection(film_anatoly)
duplicate_evgeny_3 = film_evgeny.intersection(film_vera)
duplicate_evgeny_4 = film_evgeny.intersection(film_alexey)
duplicate_evgeny_5 = film_evgeny.intersection(film_valeria)
duplicate_evgeny_6 = film_evgeny.intersection(film_alexandra)
duplicate_evgeny_7 = film_evgeny.intersection(film_igor)

all_evgeny_duplicates = duplicate_evgeny_1.union(
    duplicate_evgeny_2, duplicate_evgeny_3,
    duplicate_evgeny_4, duplicate_evgeny_5,
    duplicate_evgeny_6, duplicate_evgeny_7)

# print("Все дубликаты Евгения:", all_evgeny_duplicates)

duplicate_anatoly_1 = film_anatoly.intersection(film_olga)
duplicate_anatoly_2 = film_anatoly.intersection(film_evgeny)
duplicate_anatoly_3 = film_anatoly.intersection(film_vera)
duplicate_anatoly_4 = film_anatoly.intersection(film_alexey)
duplicate_anatoly_5 = film_anatoly.intersection(film_valeria)
duplicate_anatoly_6 = film_anatoly.intersection(film_alexandra)
duplicate_anatoly_7 = film_anatoly.intersection(film_igor)

all_anatoly_duplicates = duplicate_anatoly_1.union(
    duplicate_anatoly_2, duplicate_anatoly_3,
    duplicate_anatoly_4, duplicate_anatoly_5,
    duplicate_anatoly_6, duplicate_anatoly_7)

# print("Все дубликаты Анатолия:", all_anatoly_duplicates)

duplicate_vera_1 = film_vera.intersection(film_olga)
duplicate_vera_2 = film_vera.intersection(film_evgeny)
duplicate_vera_3 = film_vera.intersection(film_anatoly)
duplicate_vera_4 = film_vera.intersection(film_alexey)
duplicate_vera_5 = film_vera.intersection(film_valeria)
duplicate_vera_6 = film_vera.intersection(film_alexandra)
duplicate_vera_7 = film_vera.intersection(film_igor)

all_vera_duplicates = duplicate_vera_1.union(
    duplicate_vera_2, duplicate_vera_3,
    duplicate_vera_4, duplicate_vera_5,
    duplicate_vera_6, duplicate_vera_7)

# print("Все дубликаты Веры:", all_vera_duplicates)

duplicate_alexey_1 = film_alexey.intersection(film_olga)
duplicate_alexey_2 = film_alexey.intersection(film_evgeny)
duplicate_alexey_3 = film_alexey.intersection(film_anatoly)
duplicate_alexey_4 = film_alexey.intersection(film_vera)
duplicate_alexey_5 = film_alexey.intersection(film_valeria)
duplicate_alexey_6 = film_alexey.intersection(film_alexandra)
duplicate_alexey_7 = film_alexey.intersection(film_igor)

all_alexey_duplicates = duplicate_alexey_1.union(
    duplicate_alexey_2, duplicate_alexey_3,
    duplicate_alexey_4, duplicate_alexey_5,
    duplicate_alexey_6, duplicate_alexey_7)

# print("Все дубликаты Алексея:", all_alexey_duplicates)

duplicate_valeria_1 = film_valeria.intersection(film_olga)
duplicate_valeria_2 = film_valeria.intersection(film_evgeny)
duplicate_valeria_3 = film_valeria.intersection(film_anatoly)
duplicate_valeria_4 = film_valeria.intersection(film_vera)
duplicate_valeria_5 = film_valeria.intersection(film_alexey)
duplicate_valeria_6 = film_valeria.intersection(film_alexandra)
duplicate_valeria_7 = film_valeria.intersection(film_igor)

all_valeria_duplicates = duplicate_valeria_1.union(
    duplicate_valeria_2, duplicate_valeria_3,
    duplicate_valeria_4, duplicate_valeria_5,
    duplicate_valeria_6, duplicate_valeria_7)

# print("Все дубликаты Валерии:", all_valeria_duplicates)

duplicate_alexandra_1 = film_alexandra.intersection(film_olga)
duplicate_alexandra_2 = film_alexandra.intersection(film_evgeny)
duplicate_alexandra_3 = film_alexandra.intersection(film_anatoly)
duplicate_alexandra_4 = film_alexandra.intersection(film_vera)
duplicate_alexandra_5 = film_alexandra.intersection(film_alexey)
duplicate_alexandra_6 = film_alexandra.intersection(film_valeria)
duplicate_alexandra_7 = film_alexandra.intersection(film_igor)

all_alexandra_duplicates = duplicate_alexandra_1.union(
    duplicate_alexandra_2, duplicate_alexandra_3,
    duplicate_alexandra_4, duplicate_alexandra_5,
    duplicate_alexandra_6, duplicate_alexandra_7)

# print("Все дубликаты Александры:", all_alexandra_duplicates)

duplicate_igor_1 = film_igor.intersection(film_olga)
duplicate_igor_2 = film_igor.intersection(film_evgeny)
duplicate_igor_3 = film_igor.intersection(film_anatoly)
duplicate_igor_4 = film_igor.intersection(film_vera)
duplicate_igor_5 = film_igor.intersection(film_alexey)
duplicate_igor_6 = film_igor.intersection(film_valeria)
duplicate_igor_7 = film_igor.intersection(film_alexandra)

all_igor_duplicates = duplicate_igor_1.union(
    duplicate_igor_2, duplicate_igor_3,
    duplicate_igor_4, duplicate_igor_5,
    duplicate_igor_6, duplicate_igor_7)

# print("Все дубликаты Игоря:", all_igor_duplicates)

all_duplicates = all_olga_duplicates.union(
    all_evgeny_duplicates, all_anatoly_duplicates,
    all_vera_duplicates, all_alexey_duplicates,
    all_valeria_duplicates, all_alexandra_duplicates,
    all_igor_duplicates)

all_duplicates = list(all_duplicates)

print(f"Повторяющиеся фильмы ({len(all_duplicates)} шт.): \n🎬 {'\n🎬 '.join(all_duplicates)}")


# Соберем все уникальные фильмы в один список
unique_olga = film_olga.difference(all_duplicates)
unique_evgeny = film_evgeny.difference(all_duplicates)
unique_anatoly = film_anatoly.difference(all_duplicates)
unique_vera = film_vera.difference(all_duplicates)
unique_alexey = film_alexey.difference(all_duplicates)
unique_valeria = film_valeria.difference(all_duplicates)
unique_alexandra = film_alexandra.difference(all_duplicates)
unique_igor = film_igor.difference(all_duplicates)

# print("Уникальные фильмы Ольги:", unique_olga)
# print("Уникальные фильмы Евгения:", unique_evgeny)
# print("Уникальные фильмы Анатолия:", unique_anatoly)
# print("Уникальные фильмы Веры:", unique_vera)
# print("Уникальные фильмы Алексея:", unique_alexey)
# print("Уникальные фильмы Валерии:", unique_valeria)
# print("Уникальные фильмы Александры:", unique_alexandra)
# print("Уникальные фильмы Игоря:", unique_igor)

# Соберем все уникальные фильмы в один список
all_unique = unique_olga.union(
    unique_evgeny, unique_anatoly,
    unique_vera, unique_alexey,
    unique_valeria, unique_alexandra,
    unique_igor)

print("Всего уникальных фильмов:", len(all_unique), "шт.")