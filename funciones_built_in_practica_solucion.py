# 1. Valor Absoluto
print("1. Valor Absoluto:")
numbers = [-10, -5, 0, 5, 10]
absolute_values = [abs(num) for num in numbers]
print(absolute_values)  # [10, 5, 0, 5, 10]

# 2. Verificación de Elementos
print("\n2. Verificación de Elementos:")
bool_list = [True, True, False]
print("All:", all(bool_list))  # False
print("Any:", any(bool_list))  # True

# 3. Conversión de Bases
print("\n3. Conversión de Bases:")
num = 255
print("Bin:", bin(num))  # '0b11111111'
print("Oct:", oct(num))  # '0o377'
print("Hex:", hex(num))  # '0xff'

# 4. Comprobación de Atributos
print("\n4. Comprobación de Atributos:")
class MyClass:
    def __init__(self):
        self.attr1 = 10
        self.attr2 = 20

obj = MyClass()
print("Has attr1:", hasattr(obj, 'attr1'))  # True
print("Has attr3:", hasattr(obj, 'attr3'))  # False

# 5. Iteradores y Enumeraciones
print("\n5. Iteradores y Enumeraciones:")
strings = ['a', 'b', 'c']
for index, value in enumerate(strings):
    print(f"Index: {index}, Value: {value}")

# 6. Ordenar y Filtrar
print("\n6. Ordenar y Filtrar:")
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Sorted:", sorted_numbers)  # [1, 2, 5, 5, 6, 9]
print("Even:", even_numbers)  # [2, 6]

# 7. Reversa y Representación
print("\n7. Reversa y Representación:")
reversed_list = list(reversed(numbers))
repr_string = repr('Hello')
print("Reversed:", reversed_list)  # [6, 5, 5, 1, 9, 2]
print("Repr:", repr_string)  # "'Hello'"

# 8. Funciones y Métodos
print("\n8. Funciones y Métodos:")
def my_function():
    return "I am callable"

print("Callable:", callable(my_function))  # True

# 9. Métodos de Cadena
print("\n9. Métodos de Cadena:")
int_to_str = str(123)
str_length = len(int_to_str)
print("String:", int_to_str)  # '123'
print("Length:", str_length)  # 3

# 10. Evaluación y Ejecución de Código
print("\n10. Evaluación y Ejecución de Código:")
expression = '2 + 3'
result = eval(expression)
print("Eval:", result)  # 5

code = """
x = 5
print('Exec:', x)
"""
exec(code)  # 'Exec: 5'

# 11. Propiedades y Métodos Estáticos
print("\n11. Propiedades y Métodos Estáticos:")
class MyClass:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    @staticmethod
    def static_method():
        return "I'm static"

obj = MyClass()
print("Property:", obj.value)  # 0
print("Static Method:", MyClass.static_method())  # "I'm static"

# 12. Uso de Byte y MemoryView
print("\n12. Uso de Byte y MemoryView:")
byte_data = bytes([65, 66, 67])
bytearray_data = bytearray([65, 66, 67])
memory_view = memoryview(byte_data)
print("Bytes:", byte_data)  # b'ABC'
print("Bytearray:", bytearray_data)  # bytearray(b'ABC')
print("Memoryview:", memory_view[0:2].tobytes())  # b'AB'

# 13. Manipulación de Archivos
print("\n13. Manipulación de Archivos:")
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

with open('example.txt', 'r') as file:
    content = file.read()
print("File Content:", content)  # 'Hello, World!'

# 14. Atributos y Espacios de Nombres
print("\n14. Atributos y Espacios de Nombres:")
class MyClass:
    def __init__(self):
        self.attr = 10

obj = MyClass()
print("Getattr attr:", getattr(obj, 'attr'))  # 10
setattr(obj, 'attr', 20)
print("Getattr attr after set:", getattr(obj, 'attr'))  # 20
print("Locals:", locals())  # Muestra variables locales
print("Globals:", globals())  # Muestra variables globales

# 15. Sumas y Potencias
print("\n15. Sumas y Potencias:")
numbers = [1, 2, 3, 4]
power = pow(2, 3)
total_sum = sum(numbers)
print("Pow:", power)  # 8
print("Sum:", total_sum)  # 10
