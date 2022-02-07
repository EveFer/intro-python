# recurso
# https://github.com/LaunchX-InnovaccionVirtual/CursoIntroPython/blob/main/M%C3%B3dulo%204%20-%20Cadenas/M%C3%B3dulo%204%20-%20Cadenas.md

# Inmutabilidad de las cadenas
# las cadenas son inmutables

fact = 'The Moon has no atmosphere.'
print(fact) # -> 'The Moon has no atmosphere.'
fact + 'No sound can be heard on the Moon.'
print(fact) # -> 'The Moon has no atmosphere.' O: wowww

# para poder obtener le valor nuevo debo alamcenarlo en otra variable

new_fact = fact + 'No sound can be heard on the Moon.'
print(new_fact) # -> The Moon has no atmosphere.No sound can be heard on the Moon.

# Como resultado, las operaciones en cadenas siempre producen nuevas cadenas.

# Comillas

moon_radius = "The Moon has a radius of 1,080 miles"
string_1 = 'The "near side" is the part of the Moon that faces the Earth'
str_2 = "We only see about 60% of the Moon's surface"
str_3 = """We only see about 60% of the Moon's surface, this is known as the "near side"."""

# Texto multilínea

print('----Multilinea-----')

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline_2 = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline_2)


# Métodos string en Python
print('----Métodos de string-----')

# title
print('--- metodo title() -------')
heading = 'temperatures and facts about the moon'.title()
print(heading)

print('--- metodo split() -------')

temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
split_1 = temperatures.split()
split_2 = temperatures.split('\n')

print(split_1)
print(split_2)

print('-------- Busqueda en una cadena ------')

# puede hacerse desde el operador in
print('-------- con in')

print('Moon' in 'This text will describe facts and challenges with space travel')

print('Moon' in 'This text will describe facts about the Moon')

# para encontrar la position de una palabra en una cadena se usa find

print('---- with find()')

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""

print(temperatures.find('Moon'))
print(temperatures.find('Mars'))

# metodo count() devuelve las veces que se encuentr una palabra en la cadena
print('----- with count()')
print(temperatures.count('Mars'))
print(temperatures.count('Moon'))


print('---- lower()')
print("The Moon And The Earth".lower())
print('---- upper()')
print('The Moon And The Earth'.upper())

# obtener la temperatura

print('split y obtener parte de un array, para obtener la temperatura')
temperatures = 'Mars Average Temperature: -60 C'
parts = temperatures.split(':')
print(parts)

print(parts[-1]) # accede a la ultima posicion de la cadena

# otra forma
mars_temperature = 'The highest temperature on Mars is about 30 C'

for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

print("-70".isnumeric()) # es false por no identifica el guion

print('-60'.startswith('-'))

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

# método replace()
print('---- método replace()')

print('Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'.replace('Celsius', 'C'))

text = 'Temperatures on the Moon can vary wildly.' 

print('temperatures' in text)
print('temperatures' in text.lower())

print('===== método join()')

moon_facts = ['The Moon is drifting away from the Earth.', 'On average, the Moon is moving about 4cm every year']



print('|'.join(moon_facts))

# Formatos de cadenas

print('--- Formato de cadenas')

print(' with %')
mass_percentage = '1/6'
print('On the Moon, you would weigh about %s of your weight on Earth' % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight,
    but only one side is seen from %s because
    the %s rotates around its own axis when it orbits %s.""" % ('Moon', 'Earth', 'Moon', 'Earth'))

print("with .format()")

mass_percentage = '1/6'
print('On the Moon, you would weigh about {} of your weight on Earth'.format(mass_percentage))

print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

print('Interpolacion de variables em cadenas con f-string')

print(f'On the Moon, you would weigh about {mass_percentage} of your weight on Earth')

print(f'On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth')

subject = 'interesting facts about the moon'
print(f'{subject.title()}')