from lab1.config import alphabet

def vigenere_encryption(text, key):
    res = ""
    key_repeated = (key * (len(text) // len(key) + 1))[:len(text)]

    for p, k in zip(text, key_repeated):
        if p.isalpha():
            is_upper = p.isupper()
            p_idx = alphabet.index(p.upper())
            k_idx = alphabet.index(k.upper())
            encrypted_letter = alphabet[(p_idx + k_idx) % len(alphabet)]
            if not is_upper:
                encrypted_letter = encrypted_letter.lower()
            res += encrypted_letter
        else:
            res += p

    return res


def vigenere_decryption(encrypted_text, key):
    res = ""
    key_repeated = (key * (len(encrypted_text) // len(key) + 1))[:len(encrypted_text)]

    for c, k in zip(encrypted_text, key_repeated):
        if c.isalpha():
            is_upper = c.isupper()
            c_idx = alphabet.index(c.upper())
            k_idx = alphabet.index(k.upper())
            decrypted_letter = alphabet[(c_idx - k_idx + len(alphabet)) % len(alphabet)]
            if not is_upper:
                decrypted_letter = decrypted_letter.lower()
            res += decrypted_letter
        else:
            res += c

    return res
