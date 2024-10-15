def ingresar_puntuacion():
    while True:
        point=str(input("Por favor, introduzca una puntuación en una escala de 1 a 5: "))
        
        if point.isdecimal():
            point = int(point)
            
            if point < 1 or point > 5:
                print('Por favor, introduzca un valor entre 1 y 5')
                continue  # Vuelve al inicio del bucle para pedir de nuevo
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post} \n')
                break  # Salir del bucle una vez que se introduce correctamente
        else:
            print('Por favor, introduzca la puntuación en números')


def resultados_a():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            resultados = read_file.read()
            if resultados:
                print(resultados)
            else:
                print("No hay resultados almacenados.")
    except FileNotFoundError:
        print("No se encontró el archivo de resultados.")


def seleccionar__proceso():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')

        num=int(input("ingrese numero del 1 al 3: "))
        if num == 1:
                ingresar_puntuacion()
        elif num == 2:
                resultados_a()
        elif num == 3:
                print('Finalizando')
                break
        else:
                print("ingrese un numero del 1 al 3, por favorr")
if __name__ == "__main__":
    seleccionar__proceso()
