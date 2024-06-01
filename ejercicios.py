lista = [1,20,15,10]
try:
    print(lista[100])
except IndexError:
    print("El indice no existe")

while(True):
    try:
        numero = float(input("Ingresa un número"))
        resultado = "IMPAR"
        if (numero % 2 == 0):
            resultado = "PAR"
        print("El número {} es {}".format(numero , resultado ))
        
        break
    except:
        print("Ocurrio un error!")