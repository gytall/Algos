"""Реализация алгоритма сортировки выбором."""
import time

from main import generate_random_matrix


def selection_sort(matrix):
    """
    Сортирует каждую строку матрицы методом выбора.
    
    Алгоритм находит минимальный элемент и помещает его
    в начало неотсортированной части массива.
    
    Args:
        matrix: Двумерный список (матрица) для сортировки
               (изменяется на месте)
    
    Time Complexity: O(n²) для каждой строки
    Space Complexity: O(1)
    """
    for row in matrix:
        for i in range(len(row)):
            min_idx = i
            for j in range(i + 1, len(row)):
                if row[j] < row[min_idx]:
                    min_idx = j
            row[i], row[min_idx] = row[min_idx], row[i]

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
    selection_sort(matrix)
    end_time = time.perf_counter()  

    print("Отсортированная матрица:")
    for row in matrix:
        print(row)

    elapsed_time = end_time - start_time  
    print(f"Время выполнения: {elapsed_time:.6f} секунд")

