import os

from c7 import decrypt_aes_ecb

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "data", "8.txt")

block_size = 16


def read_ciphertexts():
    with open(data_file, "r") as f:
        for line in f:
            yield line.strip()


def guess_aes_ecb_ciphertext():
    """Find the ciphertext with the highest number of duplicates"""
    duplicate_block_scores = [(ciphertext, score(ciphertext))
                              for ciphertext in read_ciphertexts()]
    return sorted(duplicate_block_scores, reverse=False,
                  key=lambda x: x[1])[0]


def score(ciphertext):
    """The score is the number of unique blocks"""
    b = bytes.fromhex(ciphertext)
    chunks = {b[i:i+block_size] for i in range(0, len(b), block_size)}
    return len(chunks)


if __name__ == "__main__":
    print("c8")
    print("For each ciphertext, we split it into blocks of 16 bytes.")
    print("We count the number of unique blocks in the ciphertext.")
    print("Under ECB, two identical plaintext blocks will have identical ciphertext.")
    print("Therefore, our best ECB candidate ciphertext is that with the lowest number of unique blocks, i.e., the highest number of duplicate ciphertext blocks.")
    print("Identical ciphertext blocks are usually very unlikely!")
    result = guess_aes_ecb_ciphertext()
    print("RESULT is:", result)
    assert result[0][:10] == 'd880619740'
    assert result[1] == 7
