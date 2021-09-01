def cesar_encrypt(plain, n):
    key = 'abcdefghijklmnñopqrstuvwxyz'
    plain = plain.lower()
    cipher = ""
    for x in plain:
        if x in plain:
            cipher = cipher + key[((key.index(x)+n)%26)]
        else:
            cipher = cipher + x
    return (cipher)

def cesar_decrypt(cipher,n):
    key = 'abcdefghijklmnñopqrstuvwxyz'
    plain = ""
    for x in cipher:
        if x in key:
            plain = plain + key[((key.index(x)-n)%26)]
        else:
            cipher = cipher + x
    return (cipher)

cifrado = cesar_encrypt('el passworD es 5',3)
print(cifrado)
plano = cesar_decrypt(cifrado,3)
print(plano)