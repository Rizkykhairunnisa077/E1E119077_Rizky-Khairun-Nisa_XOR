def encript(plaintext, key):
    encoded = []

    for i in range(len(plaintext)):
        xor = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encoded.append(chr(xor))

    return ''.join(encoded)

def decript(chipertext, key):
    return encript(chipertext, key)

def main():
    print("Silahkan Pilih Perintah = \n1. Enkripsi\n2. Dekripsi")
    pilih = int(input("Pilih = "))

    if pilih == 1:
        plaintext = str(input("Masukkan Plaintext =  "))
        key = str(input("Masukkan Key =  "))

        print("Plaintext =  ", plaintext)
        print("Enkripsi = ", encript(plaintext, key))
        
    elif pilih == 2:
        chipertext = str(input("Masukkan Chipertext =  "))
        key = str(input("Masukkan Key =  "))

        print("Chipertext =  ", chipertext)
        print("Dekripsi =  ", decript(chipertext, key))
        
    else:
        exit()

main()
