# 3. Сформувати функцію для переведення натурального числа з десяткової системи
# числення у шістнадцятирічну.
# Грінченко Маргарита 1 курс група 122Б

from random import randint
from time import time
from memory_profiler import profile
import sys

alf = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'

@profile
def start(n):
    str16 = ''
    n, str16 = in_ll(n, str16)

    print(str16[::-1])


def in_ll(n, str16):  # функція для переведення натурального числа з десяткової системи
    # числення у шістнадцятирічну рекурсією
    k = n % 16
    str16 += alf[k]
    n = n // 16
    if n == 0:
        return n, str16
    else:
        sys.setrecursionlimit(sys.getrecursionlimit() + 1)  # зміна межі рекурсії
        return in_ll(n, str16)


@profile
def start_second(n):  # функція для переведення натурального числа з десяткової системи
    # числення у шістнадцятирічну циклом
    str16 = ''
    while True:
        k = n % 16
        str16 += alf[k]
        n = n // 16
        if n == 0:
            break
    print(str16[::-1])

print()
print("функція для переведення натурального числа з десяткової системи числення у шістнадцятирічну рекурсією: ")
while True:
    try:
        n = int(input("Ведіть число: "))
        break
    except ValueError:
        print("тільки числа")

tic = time()  # час початку роботи функції
start(n)
toc = time()  # час зупинки функції
print(f"Час роботи функції: {toc - tic}")  # різниця часу - тобто час роботи ф-ї

print()
print("функція для переведення натурального числа з десяткової системи числення у шістнадцятирічну циклом: ")
while True:
    try:
        n = int(input("Ведіть число: "))
        break
    except ValueError:
        print("тільки числа")
tic = time()  # час початку роботи функції
start_second(n)
toc = time()  # час зупинки функції
print(f"Час роботи функції: {toc - tic}")  # різниця часу - тобто час роботи ф-ї
# цикл потребує менше пам'яті, але рукурсія швидше. Читабельність та Реалізація в обох випадках однакова
