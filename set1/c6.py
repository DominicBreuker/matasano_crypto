import os
import base64
from collections import defaultdict

from c2 import xor
from c3 import decypt_single_byte_xor
from c5 import repeating_key_xor


data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "data", "6.txt")

def read_ciphertext():
    with open(data_file, "r") as f:
        return base64.b64decode(f.read())


def guess_keysize(b, keysize_range=range(2, 41)):
    keysize_distances = [(keysize, average_edit_distance(b, keysize))
                         for keysize in keysize_range]
    return sorted(keysize_distances, reverse=False,
                  key=lambda tuple: tuple[1])[0][0]


def average_edit_distance(b, keysize):
    distances = []
    previous_chunk = None
    for current_chunk in chunks(b, keysize):
        if previous_chunk is not None \
           and len(previous_chunk) == len(current_chunk):
            distances.append(float(edit_distance(previous_chunk, current_chunk))
                             / len(previous_chunk))
        previous_chunk = current_chunk
    return sum(distances) / len(distances)


def chunks(b, keysize):
    for i in range(0, len(b), keysize):
        yield b[i:i+keysize]


def edit_distance(s1, s2):
    assert len(s1) == len(s2), "ERROR: cannot compute distance - unequal length"
    return bitstring(xor(s1, s2)).count("1")


def bitstring(b):
    return "".join(["{0:b}".format(i) for i in b])


def decrypt_repeated_key_xor(b, keysize_range=range(2,41)):
    keysize = guess_keysize(ciphertext, keysize_range)
    print(keysize)
    chunks = transposed_chunks(b, keysize)
    key_bytes = []
    for i, chunk in enumerate(chunks):
        decryption, key_byte, _ = decypt_single_byte_xor(chunks[i], num_candidates=1)[0]
        print(i, decryption, key_byte)
        key_bytes.append(key_byte)
    key = bytes(key_bytes)
    return repeating_key_xor(b, key), key


def transposed_chunks(b, keysize):
    chunks = defaultdict(list)
    for i, byte in enumerate(b):
        chunks[i % keysize].append(byte)
    for i, bytear in chunks.items():
        chunks[i] = bytes(bytear)
    return chunks


if __name__ == "__main__":
    assert edit_distance(b"this is a test", b"wokka wokka!!!") == 37, "ERROR!!!"
    ciphertext = read_ciphertext()
    decryption, key = decrypt_repeated_key_xor(ciphertext)
    print("DECRYPTION", decryption.decode("utf-8"))
    print("KEY", key)
    true_key = b'Terminator X: Bring the noise'
    assert key == true_key, "ERROR"
