def primo(n):
    contador = 2
    while contador < n:
        if n % contador == 0:
            return False
        contador += 1
    return True

def main():
    n = int(input("Ingrese un numero: "))
    esPrimo = primo(n)
    print(esPrimo)

main()