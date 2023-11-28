def estaEnRango(valor, minimo, maximo):
    return minimo <= valor <= maximo

def estaEnLista(valor, lista):
    return valor in lista

def main():
    valor = 5
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    minimo = 1
    maximo = 10

  
    if estaEnRango(valor, minimo, maximo):
        print(f"El valor {valor} está en el rango entre {minimo} y {maximo}.")
    else:
        print(f"El valor {valor} no está en el rango entre {minimo} y {maximo}.")

    if estaEnLista(valor, lista):
        print(f"El valor {valor} está en la lista.")
    else:
        print(f"El valor {valor} no está en la lista.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
