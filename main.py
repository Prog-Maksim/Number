from random import randint  # Библиотека для создания рандомных чисел
from itertools import groupby  # Библиотека для удаления повторяюшихся значений
from collections import Counter  # Библиотека для подсчета количества вхождений в список

random_number = list()  # Список для хранения рандомных чисел
new_random_number = list()  # Список для хранения рандомных чисел без повторов


def random():  # Генерирование случайных значений
    for number in range(1000):  # Делаем итерацию 1000 раз
        random_number.append(randint(-1000, 1000))  # Записываем в список переменную с рандомным числом
    print("Список рандомных чисел", end='\n')
    print(f"список состоит из {len(random_number)} элементов -- {random_number}", end='\n')
    #  Вызываем следуюшую функцию
    sorting()


def replays():  # Удаляем повторяюшиеся значения
    new_random_number.append([el for el, _ in groupby(random_number)])  # создаем список и записываем в него элементы без повторов
    Quantity = len(new_random_number[0])  # подсчитываем количество оставшихся элементов
    # Выводим инфу
    print("Список без повторяюшихся элементов:", end='\n')
    print(f"список состоит из {len(new_random_number[0])} элементов -- {new_random_number[0]}", end='\n')
    # вызываем функцию и передаем ей аргументом - количество элементов в списке
    remainder(Quantity)


def remainder(Quantity: int()):  # Выводим количество удаленных повторяюшихся чисел
    print(f"Программой было отсеянно: {1000 - Quantity} повторяюшихся элементов", end='\n')  # выводим инфу
    quantity()  # Вызываем функцию подсчета повторяющихся чисел


def sorting():  # Сортируем список
    random_number.sort(reverse=True)  # Сортирует список в порябке убывания
    # выводим инфу
    print("Отсортированный список от большего к меньшему:")
    print(random_number, end='\n')
    replays()  # Вызываем функцию удаления повторяющихся чисел


def quantity():  # Подсчитываем количество повторяюшихся элементов
    repeating_numbers = Counter(random_number)  # метод подсчитывает кол-во повторяюшихся элементов
    # выводим инфу
    print("Словарь состояший из чисел и их повторений в основном списке")
    print(repeating_numbers, end='\n')
    # вызываем функцию указывае аргумент - список кол-во вхождений
    file(dict(repeating_numbers))


def file(quantitys: dict()):  # Записываем список чисел в файл
    with open('elements.txt', 'w') as new_file:  # создаем файл с функцией записи данных
        num = 0
        for i in new_random_number[0]:  # цикл для записи элементов из списка в файл
            num += 1  # увеличиваем список на единицу
            new_file.write(f"{i} ")  # записываем число в список
            if num == 100:  # как только в строчке накапливается 100 элементов переносим строку
                new_file.write("\n")
                num = 0  # обнуляем переменную
        new_file.write("\n \n")
        new_file.write(f"{quantitys} ")  # записываем в файл словарь - кол-во вхождений
    printfile()


def printfile():  # Выводим числа из файла
    filen = open('elements.txt', 'r')  # открываем файл с функцией чтения данных
    print("Данные с файла", end='\n')
    print(filen.read())  # выводим все строчки данных с файла
    filen.close()  # закрываем соединение

random()  # вызываем функцию для старта программы