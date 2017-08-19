import os

from c3 import decypt_single_byte_xor

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "data", "4.txt")

def read_ciphertexts():
    with open(data_file, "r") as f:
        for line in f:
            yield line.strip()

def guess_xor_ciphertext():
    decrypt_scores = []
    for ciphertext in read_ciphertexts():
        b = bytes.fromhex(ciphertext)
        decrypt = decypt_single_byte_xor(b, 1)[0]
        print(ciphertext, decrypt)
        decrypt_scores.append((ciphertext, decrypt))
    return sorted(decrypt_scores, reverse=True, key=lambda x: x[1][2])[0]

if __name__ == "__main__":
    print("c4")
    result = guess_xor_ciphertext()
    print("RESULT is:", result)
    assert result[1][0] == b'Now that the party is jumping\n', "ERROR !!!"
