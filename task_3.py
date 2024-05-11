"""Реалізація алгоритмів, Тестування за допомогою timeit"""
import timeit

# Завантаження тексту
text1 = open('dist/article1.txt', 'r', encoding='cp1251').read()
text2 = open('dist/article2.txt', 'r', encoding='cp1251').read()

# Задаємо підрядки
existing_substring = "дослідження"
fake_substring = "notexist"

# Тестування
def test_algorithm(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=10000)


def boyer_moore_search(text, pattern):
    '''Алгоритм Боєра-Мура'''
    m, n = len(pattern), len(text)
    if m == 0:
        return 0
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1  # текстовий індекс
    k = m - 1  # патерновий індекс
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)  # остання позиція символу в паттерні
            i += m - min(k, j + 1)
            k = m - 1
    return -1

def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    lps = [0] * m
    j = 0  # довжина попереднього найбільшого суфіксу
    compute_lps(pattern, lps)
    i = 0  # індекс для text
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1

def compute_lps(pattern, lps):
    '''Алгоритм Кнута-Морріса-Пратта (KMP)'''
    length = 0
    i = 1
    lps[0] = 0
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

def rabin_karp_search(text, pattern, d=256, q=101):
    '''Алгоритм Рабіна-Карпа'''
    m, n = len(pattern), len(text)
    h = pow(d, m-1) % q
    p, t = 0, 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            t = (t - h * ord(text[i])) % q
            t = (t * d + ord(text[i + m])) % q
            t = (t + q) % q
    return -1


print("Boyer-Moore:", test_algorithm(boyer_moore_search, text1, existing_substring))
print("KMP:", test_algorithm(kmp_search, text1, existing_substring))
print("Rabin-Karp:", test_algorithm(rabin_karp_search, text1, existing_substring))
