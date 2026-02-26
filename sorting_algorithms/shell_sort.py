"""Реализация алгоритма сортировки Шелла."""
import time

from main import generate_random_matrix


def shell_sort(matrix):
    """
    Сортирует каждую строку матрицы методом Шелла.
    
    Алгоритм является улучшенной версией сортировки вставками,
    использующей убывающие интервалы для сравнения элементов.
    
    Args:
        matrix: Двумерный список (матрица) для сортировки
               (изменяется на месте)
    
    Time Complexity: O(n^(3/2)) в среднем случае
    Space Complexity: O(1)
    """
    for row in matrix:
        gap = len(row) // 2
        while gap > 0:
            for i in range(gap, len(row)):
                temp = row[i]
                j = i
                while j >= gap and row[j - gap] > temp:
                    row[j] = row[j - gap]
                    j -= gap
                row[j] = temp
            gap //= 2

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
    shell_sort(matrix)
    end_time = time.perf_counter()

    print("Отсортированная матрица:")
    for row in matrix:
        print(row)

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
