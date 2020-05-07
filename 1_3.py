# 3. Сформувати функцію для обчислення індексу максимального елемента масиву
# n*n, де 1<=n<=5.
# Грінченко Маргарита 1 курс група 122Б


from random import randint
from time import time
from memory_profiler import profile
import sys


@profile
def start(l):
    return max_idx_rec(l)


def max_idx_rec(l, r=0, t=0, position_1=0,
                position_2=0):  # функція для обчислення індексу максимального елемента масиву n*n рекурсивно
    if t == len(l[r]):
        r += 1  # рядок
        t = 0  # стовпець
    if r == len(l):
        return position_1, position_2
    if l[r][t] > l[position_1][position_2]:  # перевірка
        position_1 = r  # рядок максимального елемента
        position_2 = t  # стовпець максимального елемента
    t += 1
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)  # зміна межі рекурсії
    return max_idx_rec(l, r, t, position_1, position_2)


@profile
def max_idx_cyc(l):  # функція для обчислення індексу максимального елемента масиву n*n циклом
    position_1 = 0  # рядок максимального елемента
    position_2 = 0  # стовпець максимального елемента
    r = 0
    while r != len(l):
        t = 0
        while t != len(l[r]):  # прості ітерації н на н
            if l[r][t] > l[position_1][position_2]:  # перевірка
                position_1, position_2 = r, t
            t += 1
        r += 1
    return position_1, position_2


# ll = [[1, 5, 3, 4], [1, 2, 5, 4], [1, 7, 5, 300], [1, 9, 3, 40]]
ll = []  # генерація рандомного списку n на n елементів 1<=n<=5
n = randint(10, 50)
for i in range(n):
    g = []
    for j in range(n):
        g.append(randint(1, 11))
    ll.append(g)
print("Рандомний масив n*n", ll)
print()
print("функція для обчислення індексу максимального елемента масиву n*n, де 1<=n<=5 рекурсією: ")
tic = time()  # час початку роботи функції
print(start(ll))
toc = time()  # час зупинки функції
print(f"Час роботи функції: {toc - tic}")  # різниця часу - тобто час роботи ф-ї

print()
print("функція для обчислення індексу максимального елемента масиву n*n, де 1<=n<=5 циклом: ")
tic = time()  # час початку роботи функції
print(max_idx_cyc(ll))
toc = time()  # час зупинки функції
print(f"Час роботи функції: {toc - tic}")  # різниця часу - тобто час роботи ф-ї
# рекурсія працює швидше але цикл потребує менше пам'яті. Читабельність циклу більша. Реалізація циклу простіше.
