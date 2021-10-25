def cuentaLetraLista(lista, letra):
    num_letras = 0
    for palabra in lista:
        lst = []
        for i in palabra:
            lst.append(i)
        num_letras += lst.count(letra)
    return num_letras

def main():
    lista = ["Hola","Como","Estas","alla","aaaah"]
    letra = "a"
    cuenta = cuentaLetraLista(lista,letra)
    print(cuenta)

main()