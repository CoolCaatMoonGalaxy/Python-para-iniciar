"""Las funciones integradas,
o *built-in functions*, son aquellas que vienen predefinidas con la instalación de Python. 
Estas funciones están siempre disponibles para su uso sin necesidad de importar bibliotecas adicionales, 
ya que forman parte del núcleo del lenguaje desde el momento en que se instala Python."""

# Lista de funciones built-in en Python

# 1. abs() - Devuelve el valor absoluto de un número.
print(abs(-7))  # 7

# 2. all() - Devuelve True si todos los elementos de un iterable son verdaderos.
print(all([True, True, False]))  # False

# 3. any() - Devuelve True si al menos un elemento de un iterable es verdadero.
print(any([True, False, False]))  # True

# 4. ascii() - Devuelve una representación en cadena del objeto, escapando caracteres no ASCII.
print(ascii('ñ'))  # "'\\u00f1'"

# 5. bin() - Convierte un número entero en una cadena que representa su valor en binario.
print(bin(10))  # '0b1010'

# 6. bool() - Convierte un valor en un booleano (True o False).
print(bool(1))  # True

# 7. bytearray() - Crea un nuevo objeto de tipo bytearray.
print(bytearray([65, 66, 67]))  # bytearray(b'ABC')

# 8. bytes() - Crea un nuevo objeto de tipo bytes.
print(bytes([65, 66, 67]))  # b'ABC'

# 9. callable() - Verifica si el objeto se puede llamar como una función.
print(callable(len))  # True

# 10. chr() - Devuelve el carácter que corresponde al valor entero dado.
print(chr(65))  # 'A'

# 11. classmethod() - Devuelve una función de clase a partir de un método de clase.
class MyClass:
    @classmethod
    def my_method(cls):
        pass

# 12. compile() - Compila un código fuente en un objeto de código que puede ser ejecutado por exec() o eval().
code = compile('print("Hello World")', '', 'exec')
exec(code)

# 13. complex() - Crea un número complejo.
print(complex(1, 2))  # (1+2j)

# 14. delattr() - Elimina un atributo de un objeto.
class MyClass:
    attr = 5

obj = MyClass()
delattr(obj, 'attr')

# 15. dict() - Crea un nuevo diccionario.
print(dict(a=1, b=2))  # {'a': 1, 'b': 2}

# 16. dir() - Devuelve una lista de atributos y métodos del objeto.
print(dir([]))  # Lista de métodos y atributos de listas

# 17. divmod() - Devuelve una tupla con el cociente y el residuo de una división.
print(divmod(9, 4))  # (2, 1)

# 18. enumerate() - Devuelve un iterador que produce pares de índice y valor a partir de un iterable.
print(list(enumerate(['a', 'b', 'c'])))  # [(0, 'a'), (1, 'b'), (2, 'c')]

# 19. eval() - Evalúa una expresión de Python dentro de una cadena de texto.
print(eval('2 + 3'))  # 5

# 20. exec() - Ejecuta código Python dinámicamente.
exec('x = 5')
print(x)  # 5

# 21. exit() - Termina la ejecución del programa.
# exit()  # Termina el programa

# 22. filter() - Filtra los elementos de un iterable usando una función.
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))  # [2, 4]

# 23. float() - Convierte un número o cadena en un número de punto flotante.
print(float('3.14'))  # 3.14

# 24. format() - Devuelve una cadena de texto formateada.
print(format(1234, ','))  # '1,234'

# 25. frozenset() - Crea un conjunto inmutable.
print(frozenset([1, 2, 3]))  # frozenset({1, 2, 3})

# 26. getattr() - Devuelve el valor del atributo de un objeto.
class MyClass:
    attr = 10

obj = MyClass()
print(getattr(obj, 'attr'))  # 10

# 27. globals() - Devuelve un diccionario que representa el espacio de nombres global.
print(globals())  # {'__name__': '__main__', ...}

# 28. hasattr() - Verifica si un objeto tiene un atributo específico.
print(hasattr(obj, 'attr'))  # True

# 29. hash() - Devuelve el valor hash del objeto.
print(hash('hello'))  # 4301399545066369653 (puede variar)

# 30. help() - Muestra la documentación sobre un objeto.
help(len)  # Muestra información sobre la función len

# 31. hex() - Convierte un número entero en una cadena que representa su valor en hexadecimal.
print(hex(255))  # '0xff'

# 32. id() - Devuelve el identificador único del objeto.
print(id('hello'))  # 140343912084016 (puede variar)

# 33. input() - Lee una línea de entrada del usuario.
# name = input('Enter your name: ')  # 'John'

# 34. int() - Convierte un número o cadena en un número entero.
print(int('10'))  # 10

# 35. isinstance() - Verifica si un objeto es una instancia de una clase o tupla de clases.
print(isinstance(5, int))  # True

# 36. issubclass() - Verifica si una clase es una subclase de otra.
print(issubclass(bool, int))  # True

# 37. iter() - Devuelve un iterador a partir de un iterable.
it = iter([1, 2, 3])
print(next(it))  # 1

# 38. len() - Devuelve la longitud (número de elementos) de un objeto.
print(len('hello'))  # 5

# 39. list() - Crea una lista a partir de un iterable.
print(list('abc'))  # ['a', 'b', 'c']

# 40. locals() - Devuelve un diccionario que representa el espacio de nombres local.
print(locals())  # {'x': 10, 'y': 20, ...}

# 41. map() - Aplica una función a cada elemento de un iterable.
print(list(map(str, [1, 2, 3])))  # ['1', '2', '3']

# 42. max() - Devuelve el valor máximo en un iterable o entre dos o más argumentos.
print(max([1, 2, 3]))  # 3

# 43. memoryview() - Crea un objeto de vista de memoria a partir de un objeto de datos.
mv = memoryview(b'hello')
print(mv[0:2].tobytes())  # b'he'

# 44. min() - Devuelve el valor mínimo en un iterable o entre dos o más argumentos.
print(min([1, 2, 3]))  # 1

# 45. next() - Devuelve el siguiente elemento de un iterador.
it = iter([1, 2, 3])
print(next(it))  # 1

# 46. object() - Crea un nuevo objeto base.
obj = object()

# 47. oct() - Convierte un número entero en una cadena que representa su valor en octal.
print(oct(8))  # '0o10'

# 48. open() - Abre un archivo y devuelve un objeto de archivo.
with open('example.txt', 'w') as f:
    f.write('Hello, World!')

# 49. ord() - Devuelve el valor Unicode de un carácter.
print(ord('A'))  # 65

# 50. pow() - Devuelve el valor de un número elevado a una potencia.
print(pow(2, 3))  # 8

# 51. print() - Imprime el valor de uno o más objetos en la salida estándar.
print('Hello, World!')

# 52. property() - Devuelve una propiedad de un atributo de un objeto.
class MyClass:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

obj = MyClass()
print(obj.x)  # 0

# 53. quit() - Termina la ejecución del programa.
# quit()  # Termina el programa

# 54. range() - Devuelve un objeto de rango, que es una secuencia de números enteros.
print(list(range(5)))  # [0, 1, 2, 3, 4]

# 55. repr() - Devuelve una representación en cadena de un objeto que puede ser evaluada.
print(repr('Hello'))  # "'Hello'"

# 56. reversed() - Devuelve un iterador que accede a los elementos en orden inverso.
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# 57. round() - Redondea un número al entero más cercano o al número de decimales especificado.
print(round(3.14159, 2))  # 3.14

# 58. set() - Crea un nuevo conjunto.
print(set([1, 2, 3, 2, 1]))  # {1, 2, 3}

# 59. setattr() - Establece el valor de un atributo en un objeto.
class MyClass:
    pass

obj = MyClass()
setattr(obj, 'attr', 10)
print(obj.attr)  # 10

# 60. slice() - Devuelve un objeto de corte (slice) que puede ser usado para cortar secuencias.
print('Hello World'[slice(0, 5)])  # 'Hello'

# 61. sorted() - Devuelve una lista ordenada a partir de un iterable.
print(sorted([3, 1, 2]))  # [1, 2, 3]

# 62. staticmethod() - Devuelve una función estática a partir de un método estático.
class MyClass:
    @staticmethod
    def my_method():
        pass

# 63. str() - Convierte un objeto en una cadena.
print(str(123))  # '123'

# 64. sum() - Devuelve la suma de todos los elementos de un iterable.
print(sum([1, 2, 3]))  # 6

# 65. super() - Devuelve un objeto proxy para acceder a métodos en una clase base desde una clase derivada.
class Parent:
    def __init__(self):
        print('Parent init')

class Child(Parent):
    def __init__(self):
        super().__init__()
        print('Child init')

# 66. tuple() - Crea una nueva tupla.
print(tuple([1, 2, 3]))  # (1, 2, 3)

# 67. type() - Devuelve el tipo de un objeto.
print(type('Hello'))  # <class 'str'>

# 68. vars() - Devuelve el diccionario del espacio de nombres local del objeto.
print(vars())  # {'__name__': '__main__', ...}

# 69. zip() - Devuelve un iterador de tuplas, donde el i-ésimo elemento de cada iterable pasado como argumento es agrupado.
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# 70. __import__() - Importa un módulo. Es utilizado por la instrucción import.
import math
print(math.sqrt(16))  # 4.0
