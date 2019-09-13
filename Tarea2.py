def Func(A, B):
    # Una función que reciba dos números de entrada A, B.
    # Retorna la resta, suma y multiplicación de ambos números.
    # Retorna -1 si A<B o si alguna de las entradas es literal.
    try:
        if A >= B:
            C = A - B
            D = A + B
            E = A * B
            return C, D, E
        else:
            return -1
    except ValueError:
        return -1
    except TypeError:
        return -1
