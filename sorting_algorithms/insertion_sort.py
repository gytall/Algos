"""Реализация алгоритма сортировки вставками."""
import time

from main import generate_random_matrix


def insertion_sort(matrix):
    """
    Сортирует каждую строку матрицы методом вставок.
    
    Алгоритм строит отсортированную последовательность по одному элементу,
    вставляя каждый новый элемент в правильную позицию.
    
    Args:
        matrix: Двумерный список (матрица) для сортировки
               (изменяется на месте)
    
    Time Complexity: O(n²) для каждой строки
    Space Complexity: O(1)
    """
    for row in matrix:
        for i in range(1, len(row)):
            key = row[i]
            j = i - 1
            while j >= 0 and key < row[j]:
                row[j + 1] = row[j]
                j -= 1
            row[j + 1] = key

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
    insertion_sort(matrix)
    end_time = time.perf_counter()

    print("Отсортированная матрица:")
    for row in matrix:
        print(row)

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
