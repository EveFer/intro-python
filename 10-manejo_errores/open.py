def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError:
        print('No se pudo encontrar el archivo')

if __name__ == '__main__':
    main()