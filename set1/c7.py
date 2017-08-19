import os
import base64

from Crypto.Cipher import AES

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "data", "7.txt")

def read_ciphertext():
    with open(data_file, "r") as f:
        return base64.b64decode(f.read())


if __name__ == "__main__":
    ciphertext = read_ciphertext()
    key = b"YELLOW SUBMARINE"

    iv, ciphertext = ciphertext[:16], ciphertext[16:]
    cipher = AES.new(key, AES.MODE_ECB, iv)
    decryption = cipher.decrypt(ciphertext)

    print(decryption.decode("utf-8"))
    assert decryption[:100] == b" ringin' the bell \nA rockin' on the mike while the fly girls yell \nIn ecstasy in the back of me \nWel"
