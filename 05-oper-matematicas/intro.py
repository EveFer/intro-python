# recurso
# https://github.com/LaunchX-InnovaccionVirtual/CursoIntroPython/blob/main/M%C3%B3dulo%205%20-%20Usar%20operaciones%20matem%C3%A1ticas/M%C3%B3dulo%205%20-%20Operaciones%20matem%C3%A1ticas.md

# adicion
answer = 30 + 12
print(answer)

# sustraccion

difference = 30 - 12
print(difference)

# producto
product = 30 * 12
print(product)

# division
quotient = 30 / 12
print(quotient)

# division de piso -  devulve el valor entero
seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)

# module
seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# Jerarquia
# 1.- Paréntesis
# 2.- Exponentes
# 3.- Multiplicación y división
# 4.- Suma y resta

result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)

# conversion de str a numeros
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# absoluto
print(abs(39 - 16))
print(abs(16 - 39))

# redondeo
# el motodo round redondea
# La función de python incorporada llamada round también es útil. 
# Usada para redondear al entero más cercano si el valor decimal .5 es mayor o mayor, o hacia abajo si es menor que .5.
print(round(14.5))

# Biblioteca Math

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)