# recurso
# https://github.com/LaunchX-InnovaccionVirtual/CursoIntroPython/blob/main/M%C3%B3dulo%206%20-%20Introducci%C3%B3n%20a%20las%20listas/M%C3%B3dulo%206-%20Introducci%C3%B3n%20a%20las%20listas.md

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print('The first planet is', planets[0])
print('The second planet is', planets[1])
print('The third planet is', planets[2])

# modificar el valor de un item
planets[3] = 'Red Planet'
print('Mars is also known as', planets[3])

print('planets: ', planets)

number_of_planets = len(planets)
print('There are', number_of_planets, 'planets in the solar system.')

# agregar elementos al final de la lista  con append

planets.append('Pluto')
number_of_planets = len(planets)
print('There are actually', number_of_planets, 'planets in the solar system.')

# eliminar el ultimo item de una lista con pop()
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print('No, there are definitely', number_of_planets, 'planets in the solar system.')

# Índices negativos

print("The first planet is", planets[0])

print(planets)
print(len(planets) - 1)
print('get last item', planets[len(planets) - 1])
print('get last item', planets[- 1]) # better
print('The penultimate planet is', planets[-2])

# Buscar un valor en una lista - si no encuentra devuelve -1
jupiter_index = planets.index('Jupiter')
print('Jupiter is the', jupiter_index + 1, 'planet from the sun')

# numeros en listas
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]

bus_weight = 12650 # in kilograms, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('On Mercury, a double-decker bus weighs', bus_weight * gravity_on_planets[0], 'kg')

# max() y min()

bus_weight = 12650 # in kilograms, on Earth
# El siguiente código calcula los pesos mínimos y máximos en el sistema solar mediante el uso de esas funciones:

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('The lightest a bus would be in the solar system is', bus_weight * min(gravity_on_planets), 'kg')
print('The heaviest a bus would be in the solar system is', bus_weight * max(gravity_on_planets), 'kg')

# Manipular datos de lista

# slice[index_inicial:index_final_no_incluido]

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_before_earth = planets[0:2]
print('planetas antes de la tierra: ', planets_before_earth)

planets_after_earth = planets[3:8]
print('planetas despues de la tierra: ', planets_after_earth)

# Si no coloca el índice de detención en el slice, Python asume que deseas ir al final de la lista:

planets_after_earth = planets[3:]
print('planetas despues de la tierra: ', planets_after_earth)

# Uniendo listas con el operador +

amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

# Ordenar listas

# Python ordenará una lista de cadenas en orden alfabético y una lista de números en orden numérico

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)