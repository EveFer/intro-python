def main():
    try:
        configuration = open('config.txt')
        print('configuration:', configuration)
    except FileNotFoundError as err:
        print("no pudo leer el archivo config.txt: ", err)
    except IsADirectoryError:
        print('Encontro config.txt pero es un directorio y no es posible leerlo')
    except (BlockingIOError, TimeoutError):
        print("Paso mucho tiempo D:")


if __name__ == '__main__':
    main()