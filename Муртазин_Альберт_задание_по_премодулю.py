# -*- coding: utf-8 -*-
""""Муртазин Альберт, задание по премодулю."

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/113WRhcMKn7aIw0XdD1kPW7hKFURDeLlR

## **Задача 1. Приветствие**

На вход программе подается строка текста – имя человека.

 Напишите программу, которая выводит на экран приветствие в виде слова «Привет, » (без кавычек), после которого должна стоять запятая и пробел, а затем введенное имя.

 Для считывания текста используйте команду input(), для печати текста на экране используйте команду print().

**Пример:**

 ввод данных: Екатерина

 вывод данных: Привет, Екатерина
"""

name = input() 
print('Привет,', name)

"""## **Задача 2. Право доступа**

На вход программе подаётся целое число — возраст пользователя. Программа должна вывести текст:
*   «Доступ разрешен», если возраст не менее 18;
*   «Доступ ограничен», если возраст от 14 до 17 лет (включительно);
*   «Доступ запрещен», если возраст менее 14 лет.

Для считывания возраста используйте команду input(), не забыв преобразовать тип данных в числовой с помощью int(); для печати текста на экране используйте команду print(). Используйте условные операторы if-elif-else.

**Пример:**

 ввод данных: 17

 вывод данных: Доступ ограничен
"""

user_age = int(input()) 
if user_age >= 18:
    print('Доступ разрешен')
elif user_age >= 14:
    print('Доступ ограничен')
else:
  print('Доступ запрещен')

"""## **Задача 3. Повторение**

На вход программе подаётся:
*   на первой строке - текстовое предложение;
*   на второй строке - количество повторений (целое число).

Напишите программу, которая выводит предложение нужное количество раз (каждое предложение должно начинаться с новой строки).

Для считывания текста и числа повторений используйте команду input(), не забыв преобразовать тип данных в числовой с помощью int() для количества повторений; для печати текста на экране используйте команду print(). Используйте цикл for.

**Пример:**

 ввод данных: 
*   Век живи - век учись!
*   3

вывод данных: 
 
Век живи - век учись!

Век живи - век учись!

Век живи - век учись!
"""

text = input('ввод данных:')
amount = int(input())
for _ in range(amount): 
  print(text)

"""## **Задача 4. Повторение 2**

Реализуйте задачу 3 через цикл while.
"""

# text = input('ввод данных:') 
# amount = int(input())
# while True:
#    print(text * amount)
#    break

# Решение с помощью счетчика, уменьшаем значение на каждой итерации 
text = input('ввод данных:') 
amount = int(input())

while amount>0:
    print(text)
    amount -= 1

"""## **Задача 5. ФИО**

Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
*   name – имя человека;
*   surname – фамилия человека;
*   patronymic – отчество человека;

а затем выводит на печать ФИО человека (на одной строке, только первые буквы в порядке surname-name-patronymic).

Добавьте комментарий перед каждым этапом:

*   #объявление функции
> def print_fio(name, surname, patronymic)
*   #ввод данных
> name, surname, patronymic =
*   #вызов функции
> print_fio(name, surname, patronymic)

Для считывания текста используйте команду input(); для печати текста на экране используйте команду print(), добавив параметр sep='' для печати на одной строке. Используйте def для объявления функции.

**Пример:**

 ввод данных: 
*   Иван
*   Сидоров
*   Петрович

вывод данных: СИП
"""

name = input('введите имя:')
surname = input('введите фамилию:')
patronymic = input('введите отчество:')

def print_fio(name, surname, patronymic):
    name = name[0]
    surname = surname[0]
    patronymic = patronymic[0]
    print(name+surname+patronymic)
print_fio(name, surname, patronymic)

name = input('введите имя:')
surname = input('введите фамилию:')
patronymic = input('введите отчество:')
#объявление функции
def print_fio(name, surname, patronymic):
  name = f'{name[0]}'
  surname = f'{surname[0]}'
  patronymic = f'{patronymic[0]}'
  #вызов функции
# print(f'{name[0]}, {surname[0]}, {patronymic[0]}')
  print("".join([name[0],surname[0],patronymic[0]]))
  return print_fio
print_fio

"""## **Задача 6. Первая таблица**

Импортируйте библиотеку pandas с именем pd. Скопируйте словарь, у которого в качестве ключей - столбцы таблицы, а в качестве значений в списках - данные таблицы:
> data = {'col 1': ['Я', 'Python', 'Буду'], 'col 2': ['люблю', 'мой', 'стараться'], 'col 3': ['анализ', 'лучший', 'хорошо'], 'col 4': ['данных', 'друг', 'учиться']}

Создайте таблицу, скопировав следующий код:
> df = pd.DataFrame(data)

где df - имя таблицы, pd.DataFrame() - конструктор таблицы, data - словарь.

Выведите таблицу через print() либо просто ее вызовом без print().
"""

import pandas as pd 

data = {'col 1': ['Я', 'Python', 'Буду'], 'col 2': ['люблю', 'мой', 'стараться'], 'col 3': ['анализ', 'лучший', 'хорошо'], 'col 4': ['данных', 'друг', 'учиться']}

df = pd.DataFrame(data)
print(df)