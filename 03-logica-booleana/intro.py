# Recurso
# https://github.com/LaunchX-InnovaccionVirtual/CursoIntroPython/blob/main/M%C3%B3dulo%203%20-%20Usar%20l%C3%B3gica%20booleana/M%C3%B3dulo%203%20-%20Usar%20l%C3%B3gica%20booleana.md

# operadores de comparación
# igual a: a == b
# diferente de: a != b
# menos que: a < b
# menor o igual que: a <= b
# mayor que: a > b
# maoyr o igual que: a >= b

# práctica 1
a = 97
b = 55

if a < b:
    print(b)

# práctica 2

c = 93
d = 27
if c >= b:
    print('C es mayor de d: ', c)

# Tips de práctica 1 y 2

e = 24
f = 44

if e <= 0:
    print('e es menor: ', e)
print('se imprime f (cumpla o no cumpla la condicion )', f)

# else

g = 93
h = 27

if g >= h:
    print('g es mayor o igual que h')
else:
    print('h es mayor que g')

# elif

i = 93
j = 27

if i >= b:
    print('i es maoyr o igual que j')
elif i == j:
    print('i es igual que j')
else:
    print('j es mayor que i')

# if , elif, y else

k = 93
l = 27

if k > l:
    print('k es mayor que l')
elif k < l:
    print('k es menor que l')
else:
    print('k es igual que l')

# lógica condicional anidada

m = 16
n = 25
o = 27

if m > n:
    if n > o:
        print('m es mayor que n y n es mayor que o')
    else: 
        print('m es mayor que n y menor que o')
elif m == n:
    print('m es igual que n')
else: 
    print('m es menor que n')

# output: 'm es menor que n'


# Operadores and y or

p = 23
q = 34

# por lo menos una de las expresiones de debe complir para que la prueba se evalue en True
if p == 34 or q == 34:
    print('p + q = ', p + q)

# ambas condiciones deben cumplir para que la prueba se evealue en True
if p == 34 and q == 34:
    print('p + q = ', p + q)

