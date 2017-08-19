import binascii

from c2 import xor


def repeating_key_xor(b, key):
    key_length = len(key)
    result = []
    for i, char in enumerate(b):
        result.append(char ^ key[i % key_length])
    return bytes(result)


if __name__ == "__main__":
    plaintext = str.encode("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
    key = str.encode("ICE")
    ciphertext = bytes.fromhex("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")
    assert repeating_key_xor(plaintext, key) == ciphertext, "ERROR!!!"
