import math
import random
a = [round(random.random(),3) for _ in range(10**1*5)]
def is_sorted(arr:list[float]) -> bool:
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
def gambo_sort(arr: list[float]) -> tuple[list[float], int, int]:
    comparisons = 0
    passes = 0
    n = len(arr)
    while True:
        passes += 1
        for i in range(n):
            for j in range(n - 1):
                comparisons += 1
                p = max(0, math.cos(comparisons / 1000))
                if arr[j] > arr[j+1] or random.random() > p:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        if is_sorted(arr):
            return arr, comparisons, passes
sorted_arr, comparisons, passes = gambo_sort(a)
print(sorted_arr[:20], comparisons, passes)