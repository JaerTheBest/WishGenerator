# importing modules
import random
import sys

# word database
# Copyright (c) jaer
# 2021.03.18

# Word database
selectword = ["Сбросить лишние килограммы, т.е. похудеть.", "НСправиться с прокрастинацией (бич нашего времени — постоянное откладывание важных дел на потом).", "Написать книгу.", "По-настоящему влюбиться.", "Просто быть счастливым…", "Сделать татуировку.", "Отправиться путешествовать на машине куда глаза глядят, т.е. без определенного пункта назначения.", "Выйти замуж (жениться).", "Путешествовать по миру.", "Пить больше воды.", "Вести личный дневник.", "Увидеть своими глазами северное сияние.", "Выучить испанский язык.", "Создать и вести личный блог.", "Экономить деньги.", "Делать больше фотографий.", "Целоваться под дождем.", "Купить свой дом.", "Завести больше новых друзей.", "Научиться играть на гитаре.", "Пробежать марафон.", "Выучить французский язык.", "Найти работу.", "Рассчитаться с долгами ( кредитами).", "Читать больше книг.", "Быть более уверенным в себе.", "По-настоящему жить, а не существовать.", "Написать рассказ.", "Прыгнуть с парашютом.", "Есть более полезную пищу."]


# making a main logic

print("Добро пожаловать в генератор желаний! Хотите ознакомится с инструкцией? да или нет.")
inputone = input()

# documentation
if inputone == "да":
    print("СГЕНЕРИРОВАТЬ - Генерирует желание.")
    print("ПОВТОРИТЬ - Генерирует другое желание.")
    print("ИСХОДНЫЙ КОД - Ссылка на страницу с исходным кодом.")
    print("ВЫЙТИ - Выход из приложения.")
    print()

# commands
print("Для продолжения введите команду:")
inpt = input()
if inpt == "СГЕНЕРИРОВАТЬ":
  print(random.choice(selectword))
if inpt == "ВЫЙТИ":
	quit()
if inpt == "ПОВТОРИТЬ":
  print(random.choice(selectword))
succes = input()
if succes == "ПОВТОРИТЬ":
  print(random.choice(selectword))

input()
print("я слежу за тобой -_-")

# Codded by www.jaer.cf/users/jaer.html/