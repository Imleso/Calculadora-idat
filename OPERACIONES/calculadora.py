def sumar(a,b):
    try:
        resultado = int(a) + int(b)
    except:
        print("Ingrese solo números")
    else:
        return resultado 

def restar(a,b):
    try:
        resultado = int(a) - int(b)
    except:
        print("Ingrese solo números")
    else:
        return resultado 

def multiplicar(a,b):
    try:
        resultado = int(a) * int(b)
    except:
        print("Ingrese solo números")
    else:
        return resultado 
    
def dividir(a,b):
    try:
        resultado = int(a) / int(b)
    except ValueError:
        print("Ingrese solo números")
    except ZeroDivisionError:
        print("El numero no puede ser divisible entre 0")
    else:
        return resultado 