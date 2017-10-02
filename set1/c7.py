import os
import base64

from Crypto.Cipher import AES

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "data", "7.txt")


def read_ciphertext():
    with open(data_file, "r") as f:
        return base64.b64decode(f.read())


def decrypt_aes_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)



if __name__ == "__main__":
    ciphertext = read_ciphertext()
    key = b"YELLOW SUBMARINE"

    decryption = decrypt_aes_ecb(ciphertext, key)

    print(decryption.decode("utf-8"))
    assert decryption[:100] == b" ringin' the bell \nA rockin' on the mike while the fly girls yell \nIn ecstasy in the back of me \nWel"
