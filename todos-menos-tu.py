def todos_menos_tu(n):
    for x in range(0, 101):
        if x != n:
            print(x)

def main():
    n = int(input("Ingrese un numero: "))
    todos_menos_tu(n)

main()