def multiplos3o5():
    suma = 0
    for x in range(0,1000):
        if x % 3 == 0 or x % 5 == 0:
            suma += x
    return suma

def main():
    suma = multiplos3o5()
    print(suma)

main()