import os 

def codi(x,y,cod):
    lenu = len(x)
    lend = len(y)
    resul = " "

    for z in range(0, lenu):
        for i in range(0, lend):
            if x[z] == y[i]:
                resul += cod[i] 
    respu = str(resul.strip())
    return respu

def deco(x,y,cod):
    lenu = len(x)
    lend = len(y)
    resul = " "

    for z in range(0, lenu):
        for i in range(0, lend):
            if x[z] == cod[i]:
                resul += y[i] 
    respu = str(resul.strip())
    return respu

try:
  while True:
    os.system('cls') 
    print("Bienvenido a mi Programa, que deseas Hacer?")
    print(" ")
    print("1. CODIFICAR \n2. DECODIFICAR \n3. SALIR DEL PROGRAMA")
    print(" ")
    opci = int(input())

    letras = 'abcdefghijklmnopqrstuvwxyz'
    codigo = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

    if opci == 1:
        os.system('cls')
        print("CODIFIQUEMOS!")
        print(" ")
        print("Ingrese la palabra que desea codificar...")
        print(" ")
        palabra = input().lower().strip()
        re = codi(palabra,letras, codigo)

        print(" ")
        print("La Codificación de: " + "'" + palabra + "'" + " es: " + re)
        print(" ")
        print("Presione Cualquier Tecla para volver al Menú Principal")
        input()

    elif opci == 2:
        os.system('cls')
        print("DECODIFIQUEMOS!")
        print(" ")
        print("Ingrese el codigo que desea decodificar...")
        print(" ")
        palabra = input().upper().strip()
        re = deco(palabra, letras, codigo).upper()

        print(" ")
        print("La Decodificación del codigo: " + "'" + palabra + "'" + " es: " + re)
        print(" ")
        print("Presione Cualquier Tecla para volver al Menú Principal")
        input()

    elif opci == 3:
        print(" ")
        print("Gracias por Utilizar mi Programa, espero haya sido de utilidad...")
        input()
    else:
        print(" ")
        print("La opcion ingresada no existe")
        input()
    
    if opci == 3:
        break

except Exception as e:
    print(e)