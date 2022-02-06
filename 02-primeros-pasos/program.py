from __future__ import division


sum = 2 + 15
print(sum)

print('Hola desde la consola')

sum = 1 + 2 # 3
product = sum * 2
print(product)

# tipos de datos
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

# con la funcion type sabemos que tipo de dato tiene una variable
type(distancia_a_alfa_centauri)


# Operadores
# Aritmeticos
num1 = 10
num2 = 20

suma = num1 + num2
resta = num1 - num2
prod = num1 * num2
division = num1 / num2


# Operadores de asignación

# =
# +=
# -=
# *=
# /=


# DATES

from datetime import date
print('Today: ', date.today())

print("Today's date is: " + str(date.today()))


# Solicitar datos

# 1
print('Hola!!, bienvenido')
name = input('Ingresa tu nombre: ')
print('Saludos: ', name)

# 2
print('Calculadora')
first_num = input('Ingresa el primer numero: ')
second_num = input('Ingresa el segundo numero: ')
print('El resultado es: ' + str(int(first_num) + int(second_num)))