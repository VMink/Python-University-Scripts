def primo(num):
    contador = 2
    while contador < num:
        if num % contador == 0:
            return False
        contador += 1
    return True

def primos(num):
    ultimoPrimo = 0
    if primo(num) == True:
        ultimoPrimo = num
        print("El ultimo numero primo es:", ultimoPrimo)
        return
    contador = 2
    while contador < num:
        if primo(contador) == True:
            ultimoPrimo = contador
        contador += 1
    print("El ultimo numero primo es:", ultimoPrimo)

def main():
    n = int(input("Ingrese un numero: "))
    primos(n)

main()