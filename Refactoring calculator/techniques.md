## 1. Extract Method (Виділення методу)
Застосування: Винесення кожної арифметичної операції в окремі класи (Addition, Subtraction тощо).
Де: Класи в operations.py.

## 2. Replace Conditional with Polymorphism (Заміна умов поліморфізмом)
Застосування: Заміна ланцюга if-elif для вибору операції на динамічний виклик через словник self.operations.
Де: Ініціалізація операцій у Calculator.__init__().

## 3. Introduce Parameter Object (Введення об’єкта-параметра)
Застосування: Винесення конфігурації (налаштувань, текстів підказок) в JSON-файл (config.json).
Де: Клас Calculator, метод _load_config().

## 4. Encapsulate Field (Інкапсуляція поля)
Застосування: Приховування прямої роботи з конфігурацією за допомогою приватного методу _load_config().
Де: Завантаження конфігурації в Calculator.

## 5. Introduce Assertion (Введення перевірок)
Застосування: Додавання явної перевірки на ділення на нуль у класі Division.
Де: Метод Division.execute().

## 6. Consolidate Duplicate Conditional Fragments (Усунення дублювання умов)
Застосування: Уніфікація валідації введених даних у методі _get_valid_input().
Де: Клас Calculator, метод для валідації вводу.

## 7. Substitute Algorithm (Заміна алгоритму)
Застосування: Оптимізація вибору операцій через словник замість послідовних умов.
Де: Ініціалізація self.operations у Calculator.

## 8. Introduce Null Object (Введення null-об’єкта)
Застосування: Використання дефолтної конфігурації, якщо файл config.json не знайдено.
Де: Блок try-except у _load_config().

## 9. Replace Magic Number with Symbolic Constant (Заміна магічних чисел)
Застосування: Заміна числа 1000 на константу MAX_INPUT у конфігурації.
Де: Ключ max_input у config.json.

## 10. Decompose Conditional (Розкладання умов)
Застосування: Розбиття складної умови валідації вводу на окремі перевірки.
Де: Метод _get_valid_input() у Calculator.