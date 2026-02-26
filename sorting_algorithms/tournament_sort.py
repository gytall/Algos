"""Реализация алгоритма турнирной сортировки."""
import time

from main import generate_random_matrix


def tournament_sort(matrix):
    """
    Сортирует каждую строку матрицы турнирным методом.
    
    Алгоритм находит минимальный элемент и последовательно
    добавляет его в отсортированный список.
    
    Args:
        matrix: Двумерный список (матрица) для сортировки
               (изменяется на месте)
    
    Time Complexity: O(n²) для каждой строки
    Space Complexity: O(n)
    """
    for i in range(len(matrix)):
        sorted_list = []
        while matrix[i]:
            min_value = min(matrix[i])
            sorted_list.append(min_value)
            matrix[i].remove(min_value)
        matrix[i] = sorted_list

if __name__ == "__main__":
    m = int(input("Введите количество строк (по умолчанию 50):") or 50)
    n = int(input("Введите количество столбцов (по умолчанию 50):") or 50)
    min_limit = int(input("Введите минимальное значение (по умолчанию -250):") or -250)
    max_limit = int(input("Введите максимальное значение (по умолчанию 1005):") or 1005)

    matrix = generate_random_matrix(m, n, min_limit, max_limit)
    print("Исходная матрица:")
    for row in matrix:
        print(row)

    start_time = time.perf_counter()
    tournament_sort(matrix)
    end_time = time.perf_counter()

    print("Отсортированная матрица:")
    for row in matrix:
        print(row)

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
