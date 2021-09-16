def piramide(n):
    for x in range(1,n):
        print(x*"*")
    for x in range(n,0,-1):
        print(x*"*")

def main():
    n = int(input("Ingrese un numero: "))
    piramide(n)

main()