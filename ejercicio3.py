while(True):
    try:
        num = int(input("ingresa un número"))
        resultado = "No es primo"
        for n in range(2, num):
            if(num % n == 0):
             resultado 
    except: 
        print("Error al ingresar el numero")
    else: 
        print("El numero {} es {}".format(num, resultado))
    finally:
        break
        