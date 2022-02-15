def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:
            raise TypeError('Todos los agumentos deben ser interos, recibi: ', argument)

    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f'No hay suficiente agua para los {astronauts} astronautas despues de de {days_left} días D:')
    return f'El total de agua despues de de {days_left} días es: {total_water_left}lts'

# water_left("10", 200, None)
# Traceback (most recent call last):
#   File "generador.py", line 4, in water_left
#     argument / 10
# TypeError: unsupported operand type(s) for /: 'str' and 'int'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "generador.py", line 15, in <module>
#     water_left("10", 200, None)
#   File "generador.py", line 6, in water_left
#     raise TypeError('Todos los agumentos deben ser interos, recibi: ', argument)
# TypeError: ('Todos los agumentos deben ser interos, recibi: ', '10')

water_left(10, 200, 10)
# Traceback (most recent call last):
#   File "generador.py", line 30, in <module>
#     water_left(10, 200, 10)
#   File "generador.py", line 12, in water_left
#     raise RuntimeError(f'No hay suficiente agua para los {astronauts} astronautas despues de de {days_left} días D:')
# RuntimeError: No hay suficiente agua para los 10 astronautas despues de de 10 días D: