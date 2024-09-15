"""
Ejemplos de operadores aritméticos, de comparación, y lógicos en Python
Este script está diseñado para mostrar cómo funcionan los distintos operadores en Python.
"""

# Operadores aritméticos
a = 10
b = 5

# Suma
suma = a + b  # 10 + 5 = 15
print("Suma:", suma)

# Resta
resta = a - b  # 10 - 5 = 5
print("Resta:", resta)

# Multiplicación
multiplicacion = a * b  # 10 * 5 = 50
print("Multiplicación:", multiplicacion)

# División
division = a / b  # 10 / 5 = 2.0
print("División:", division)

# División entera
division_entera = a // b  # 10 // 5 = 2
print("División entera:", division_entera)

# Módulo (resto de la división)
modulo = a % b  # 10 % 5 = 0
print("Módulo:", modulo)

# Potencia
potencia = a ** b  # 10^5 = 100000
print("Potencia:", potencia)


# Operadores de comparación
x = 10
y = 20

# Igualdad
igual = x == y  # False
print("¿x es igual a y?:", igual)

# Diferencia
diferente = x != y  # True
print("¿x es diferente a y?:", diferente)

# Mayor que
mayor_que = x > y  # False
print("¿x es mayor que y?:", mayor_que)

# Menor que
menor_que = x < y  # True
print("¿x es menor que y?:", menor_que)

# Mayor o igual que
mayor_igual = x >= y  # False
print("¿x es mayor o igual que y?:", mayor_igual)

# Menor o igual que
menor_igual = x <= y  # True
print("¿x es menor o igual que y?:", menor_igual)


# Operadores lógicos
verdadero = True
falso = False

# Operador AND (y)
and_resultado = verdadero and falso  # False
print("True AND False:", and_resultado)

# Operador OR (o)
or_resultado = verdadero or falso  # True
print("True OR False:", or_resultado)

# Operador NOT (no)
not_resultado = not verdadero  # False
print("NOT True:", not_resultado)

# Operador XOR (exclusivo o) utilizando comparación lógica
xor_resultado = verdadero != falso  # True
print("True XOR False:", xor_resultado)
