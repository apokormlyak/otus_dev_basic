"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers: list[int]):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda x: x*x, numbers))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num: int):
    if num in [0, 1]:
        return False
    for i in range(2, (num//2+1)):
        if num % i == 0:
            return False
    return True


def is_odd(num: int):
    if num % 2 == 1:
        return True
    else:
        return False


def is_even(num: int):
    if num % 2 == 0:
        return True
    else:
        return False


def filter_numbers(numbers: list[int], filter_type: str):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(is_odd, numbers))
    elif filter_type == EVEN:
        return list(filter(is_even, numbers))
    elif filter_type == PRIME:
        return [num for num in numbers if is_prime(num)]


if __name__ == '__main__':
    m = filter_numbers([0,1,2,3,4,5,6,7,8,9,10,11], 'prime')
    print(m)
