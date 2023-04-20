

# Пірамідальне сортування
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
import random
import time

#Сортування виборкою
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


#Тепер порівняємо їх ефективність для випадкового масиву з 10 000 цілих чисел:
arr = [random.randint(-10000, 10000) for _ in range(10000)]

start_time = time.time()
heap_sort(arr)
print(f"Heap Sort(Пірамідальне сортування): {time.time() - start_time} seconds")

start_time = time.time()
selection_sort(arr)
print(f"Selection Sort(Сортування виборкою): {time.time() - start_time} seconds")
