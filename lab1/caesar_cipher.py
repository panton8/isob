from lab1.config import alphabet


def caesar_encryption(text, k):
    res = ""
    alphabet_len = len(alphabet)
    for letter in text:
        if letter.isalpha():
            is_upper = letter.isupper()
            index = alphabet.index(letter.upper())
            new_index = (index + k) % alphabet_len
            encrypted_letter = alphabet[new_index]
            if not is_upper:
                encrypted_letter = encrypted_letter.lower()
            res += encrypted_letter
        else:
            res += letter
    return res


def caesar_decryption(encrypted_text, k):
    res = ""
    alphabet_len = len(alphabet)
    for letter in encrypted_text:
        if letter.isalpha():
            is_upper = letter.isupper()
            index = alphabet.index(letter.upper())
            new_index = (index - k + alphabet_len) % alphabet_len
            encrypted_letter = alphabet[new_index]
            if not is_upper:
                encrypted_letter = encrypted_letter.lower()
            res += encrypted_letter
        else:
            res += letter
    return res
