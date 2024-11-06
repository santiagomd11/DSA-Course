# O(1) example

def get_element(array, index):
    return array[index]

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Element at index 8: {get_element(array, 8)}')

# O(n) example

def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 8
print(f'Element {element} found at index: {linear_search(array, element)}')

# O(n**2) example

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
array = [64, 34, 25, 12, 22, 11, 90]
print(f'Sorted array: {bubble_sort(array)}')


# O(log n) - Complejidad Logarítmica - Binary Search

def binary_search(array, element):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 8
print(f'Element {element} found at index: {binary_search(array, element)}')