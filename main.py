from lab1.caesar_cipher import caesar_encryption, caesar_decryption
from lab1.vigenere_cipher import vigenere_encryption, vigenere_decryption


def main():
    print("Enter k for caesar cipher:")
    k = int(input())
    print("Enter key word for vigenere cipher:")
    key = input()
    with open("data.txt", "r") as file:
        data = file.read()
        enc_caesar = caesar_encryption(data, k)
        dec_caesar = caesar_decryption(enc_caesar, k)
        enc_vigenere = vigenere_encryption(data, key)
        dec_vigenere = vigenere_decryption(enc_vigenere, key)
        print("Caesar encryption result:", enc_caesar)
        print("Caesar decryption result:", dec_caesar)
        print("Vigenere encryption result:", enc_vigenere)
        print("Vigenere decryption result:", dec_vigenere)


if __name__ == '__main__':
    main()


