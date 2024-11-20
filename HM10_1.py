"""
Цель: понять как работают потоки на практике, решив задачу

Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.

Пример результата выполнения программы:
Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков
"""
import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1} \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл: {file_name}')


# Взятие текущего времени
one_time = time.time()

# Запуск функций с аргументами из задач
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени:
second_time = time.time()
# Вывод разницы начала и конца работы функций
end_time = second_time - one_time
print(f'Работа потоков:{end_time}')
# Взятие текущего времени
one_time1 = time.time()
# Создание и запуск потоков с аргументами из задачи
th1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
th2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
th3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
th4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

# Запуск потоков
th1.start()
th2.start()
th3.start()
th4.start()
# Ожидания завершения потоков.
th1.join()
th2.join()
th3.join()
th4.join()
# Вывод текущего времени
second_time1 = time.time()
# Вывод разницы начала и конца работы потоков
end_time1 = second_time1 - one_time1
print(f'Работа потоков:{end_time1}')
