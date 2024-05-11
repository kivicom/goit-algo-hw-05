# Завдання 1

Додати метод delete для видалення пар ключ-значення таблиці HashTable

# Завдання 2

Реалізувати двійковий пошук для відсортованого масиву з дробовими числами. Написана функція для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.

# Завдання 3

Порівняти ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів (стаття 1, стаття 2). Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). На основі отриманих даних визначити найшвидший алгоритм для кожного тексту окремо та в цілому.

## Аналіз результатів ефективності алгоритмів пошуку підрядка до 3-го завдання
З отриманими результатами ми можемо провести детальний аналіз і визначити, який алгоритм виявився найефективнішим:

### Виміряні часи виконання (number=10000):
* Boyer-Moore: 3.1713 секунд
* KMP (Knuth-Morris-Pratt): 17.9653 секунд
* Rabin-Karp: 28.1488 секунд

## Висновки:

1. Алгоритм Боєра-Мура показав найкращі результати за часом виконання. Цей алгоритм ефективний завдяки своїй здатності "стрибати" через значні частини тексту без повторного перевіряння символів, що робить його особливо швидким для великих текстів і патернів, де співпадіння є рідкісними.

2. Алгоритм Кнута-Морріса-Пратта зайняв друге місце з значно більшим часом. Цей алгоритм пропонує поліпшення порівняно з наївним методом пошуку завдяки використанню префіксної функції, яка дозволяє уникати зайвих перевірок, але все ж залишається менш ефективним у порівнянні з Боєром-Муром.

3. Алгоритм Рабіна-Карпа показав найповільніші результати. Хоча цей алгоритм може бути ефективним при пошуку кількох патернів одночасно завдяки своєму хешуванню, він виявляється менш ефективним для великих текстів у сценаріях, де використовується лише один патерн.

## Рекомендації:

* Для оптимальної продуктивності в більшості реальних сценаріїв слід вибрати алгоритм Боєра-Мура, якщо не потрібна підтримка кількох одночасних патернів.

* Алгоритм Кнута-Морріса-Пратта може бути вибрано для специфічних сценаріїв, де важлива стабільність продуктивності, особливо при частій зміні патернів.

* Рабін-Карп підійде для завдань, де важлива можливість швидкого переключення між різними патернами, особливо в контексті обробки великих обсягів даних з мінімальними змінами патерна.

Цей аналіз підтверджує значення