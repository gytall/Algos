"""Реализация алгоритма быстрой сортировки."""
import time

from main import generate_random_matrix


def quick_sort(matrix):
    """
    Сортирует каждую строку матрицы методом быстрой сортировки.
    
    Алгоритм использует стратегию "разделяй и властвуй":
    выбирает опорный элемент и разделяет массив на части.
    
    Args:
        matrix: Двумерный список (матрица) для сортировки
               (изменяется на месте)
    
    Time Complexity: O(n log n) в среднем, O(n²) в худшем случае
    Space Complexity: O(log n) из-за рекурсии
    """
    def quicksort(arr):
        """Вспомогательная функция для рекурсивной сортировки."""
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
    for i in range(len(matrix)):
        matrix[i] = quicksort(matrix[i])

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
    quick_sort(matrix)
    end_time = time.perf_counter()

    print("Отсортированная матрица:")
    for row in matrix:
        print(row)

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
