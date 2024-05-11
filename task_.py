def binary_search_with_upper_bound(arr, target):
    low, high = 0, len(arr) - 1  # Ініціалізація початкових значень
    iterations = 0  # Лічильник кількості ітерацій
    closest_greater = None  # Зберігає найближчий більший елемент

    while low <= high:
        iterations += 1  # Збільшуємо лічильник ітерацій
        mid = (low + high) // 2  # Знаходження середини
        if arr[mid] < target:
            low = mid + 1  # Звужуємо пошук до правої частини
        elif arr[mid] > target:
            closest_greater = arr[mid]  # Оновлюємо найближчий більший елемент
            high = mid - 1  # Звужуємо пошук до лівої частини
        else:
            # Якщо знайдено точне співпадіння
            return (iterations, arr[mid])
    
    # Якщо цикл завершено без знаходження точного значення
    if closest_greater is not None:
        return (iterations, closest_greater)
    # Перевірка на наявність елемента, що є верхньою межею
    if low < len(arr) and arr[low] >= target:
        return (iterations, arr[low])
    return (iterations, None)  # Якщо немає більших елементів

# Приклад використання:
arr = [1.1, 2.5, 3.7, 4.6, 5.8, 6.9]
target = 4.0
result = binary_search_with_upper_bound(arr, target)
print("Кількість ітерацій та верхня межа:", result)
