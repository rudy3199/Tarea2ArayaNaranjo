def primos(a):
    # define funcion
    if a < 1:
        # condicional para detectar si a es menor a 1
        print('Rango no válido')
    elif a == 1:
        # condicional para detectar si a es igual a 1
        print('Fin')
    else:
        # si no se cumple ninguna condicion se
        count = 0
        for i in range(1, a+1):
            # se realiza un for
            if a % i != 0:
                pass
            else:
                count = count
                count = count + 1
    if count > 2:
        # condicional para determinar si el contador es mayor a 2
            primos(a-1)
    else:
            print(a)
            # imprime numero a
            primos(a-1)
