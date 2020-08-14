"""
Задание 2.
Предложить варианты оптимизации и доказать (наглядно, кодом) их эффективность
"""
"""Для оптимизации кода, с целью его ускорения мы используем встроенные функции, словари,
    Но словари в свою очередь требуют больше памяти, поэтому первое что приходит на ум в плане оптимизации памяти и времени
    использовать множества(хеш-таблица), так как множества хранят незименяемые объекты, доступ и добавление в множество 
    имеет сложность О(1), скорость будет постоянной. 
"""

from memory_profiler import profile, memory_usage
import time


def time_decorator(function_to_decorate):
    def wrapper_my_func():
        print(f'Создание: {"*" * 20}')
        ts1 = time.process_time()
        ms1 = memory_usage()
        function_to_decorate()
        tf1 = time.process_time()
        mf1 = memory_usage()
        tdiff1 = tf1 - ts1
        mdiff1 = mf1[0] - ms1[0]
        print(f'Время выполнения Алгоритма: {tdiff1} Миллисекунд\nКоличество выделенной памяти: {mdiff1} Mib')

    return wrapper_my_func


@profile
@time_decorator
def create_lst():
    return list(range(0, 100))


@profile
@time_decorator
def create_dct():
    return {i + 1: i for i in range(0, 100)}


@profile
@time_decorator
def create_set():
    return set(range(0, 100))


if __name__ == "__main__":
    create_lst()
    create_dct()
    create_set()
