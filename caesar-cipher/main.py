import caesar

def main():

    tfile1 = open("original.txt", "r")
    text = tfile1.read()
    tfile1.close()

    caesar_cipher1 = caesar.CaesarCipher(text, 16)
    encrypted_text = caesar_cipher1.encrypt()

    tfile2 = open("encrypted.txt", "w")
    tfile2.write(encrypted_text)
    tfile2.close()

main()
