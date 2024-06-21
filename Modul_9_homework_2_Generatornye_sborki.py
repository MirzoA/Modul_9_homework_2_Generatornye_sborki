# Фабрика функций для деления и умножения:
def create_operation(operation):
    if operation == "division":
        def division(x, y):
            return x / y
        return division
    elif operation == "multiplication":
        def multiplication(x, y):
            return x * y
        return multiplication
my_func_division = create_operation("division")
my_func_multiplication = create_operation("multiplication")
print(f'Результат деления: {my_func_division(6,2)}')
print(f'Результат умножения: {my_func_multiplication(4,2)}')

# Лямбда функция с аналогом через def
exponential = lambda x, y: x ** y
print(exponential(2, 4)) # Выводит 16

def exponential_def(x, y):
   return x ** y
print(exponential_def(2, 4)) # Выводит 16

# Пример создания вызываемого объекта
class Rect:
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __call__(self):
       rectangle = self.a * self.b
       return rectangle


rectangle_square = Rect(5, 8)
print(f'Стороны прямогульника: {vars(rectangle_square)}')
print(f'Площадь прямогульника равна: {rectangle_square()}')