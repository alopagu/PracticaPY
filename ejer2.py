def esBinario(strbinario):
    for char in strbinario:
        if char not in ['0', '1']:
            return False
    return True

def binarioADecimal(binario):
    return int(binario, 2)

def main():
    strbinario = input("Introduce un número binario: ")
    if esBinario(strbinario):
        print("El número decimal equivalente es:", binarioADecimal(strbinario))
    else:
        print("La entrada no es un número binario válido.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
