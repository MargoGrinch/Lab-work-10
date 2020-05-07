# 1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
# натурального числа n.
# Грінченко Маргарита 1 курс група 122Б

from time import time
from memory_profiler import profile
import sys

@profile
def start_factorial_recursion(n):
    return factorial_recursion(n)


def factorial_recursion(n):#функція знаходження факторіалу рекурсією
    if n == 0:
        return 1
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)
    return factorial_recursion(n - 1) * n


@profile
def factorial_cycle(n):#функція знаходження факторіалу циклом
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial


print("функція знаходження факторіалу рекурсією: ")
while True:
    try:
        n = int(input("Ведіть число: "))
        break
    except ValueError:
        print("тільки числа")

tic = time()  # час початку роботи функції
print(start_factorial_recursion(n))
toc = time()  # час зупинки функції
print(f"Час роботи функції: {toc - tic}")  # різниця часу - тобто час роботи ф-ї
print()

print("функція знаходження факторіалу циклом: ")
tic = time()  # час початку роботи функції
print(factorial_cycle(n))
toc = time()  # час зупинки функції
print(f"Час роботи функції: {toc - tic}")  # різниця часу - тобто час роботи ф-ї

# цикл менше пам'яті їсть, але рукурсія працює швидше та реалізація та читабельність там і там проста
