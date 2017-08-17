from collections import defaultdict

from c2 import xor

# https://en.wikipedia.org/wiki/Letter_frequency
english_letter_frequency = {
    'e': 12.70,
    't': 9.06,
    'a': 8.17,
    'o': 7.51,
    'i': 6.97,
    'n': 6.75,
    's': 6.33,
    'h': 6.09,
    'r': 5.99,
    'd': 4.25,
    'l': 4.03,
    'c': 2.78,
    'u': 2.76,
    'm': 2.41,
    'w': 2.36,
    'f': 2.23,
    'g': 2.02,
    'y': 1.97,
    'p': 1.93,
    'b': 1.29,
    'v': 0.98,
    'k': 0.77,
    'j': 0.15,
    'x': 0.15,
    'q': 0.10,
    'z': 0.07
    }

other_characters = ' .,:;!?()[]{}#$*\''
base_score = 0.1

def get_letter_scores():
    letter_scores = defaultdict(lambda: 0)
    for letter, frequency in english_letter_frequency.items():
        letter_scores[ord(letter)] = float(frequency) / 100.0 + base_score
    for letter in other_characters:
        letter_scores[ord(letter)] = base_score
    return letter_scores


def score_decrypted_bytes(b):
    letter_scores = get_letter_scores()
    return sum([letter_scores[ord(chr(x).lower())] for x in b])


def decrypt_single_btye_xor_with_key(b, key_byte):
    length = len(b)
    key = bytes([key_byte] * length)
    return xor(b, key)

def decypt_single_byte_xor(b, num_candidates=1):
    key_scores = {}
    for key_byte in range(256):
        decrpytion = decrypt_single_btye_xor_with_key(b, key_byte)
        key_scores[key_byte] = score_decrypted_bytes(decrpytion)
    result = sorted([(key_byte, score) for key_byte, score in key_scores.items()], reverse=True, key=lambda tuple: tuple[1])[0:num_candidates]
    return [(decrypt_single_btye_xor_with_key(b, key_byte), score) for key_byte, score in result]

def decypt_single_byte_xor_best_guess(b):
    return decypt_single_byte_xor(b, 1)[0][0]

if __name__ == "__main__":
    b = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    assert decypt_single_byte_xor_best_guess(b) == b"Cooking MC's like a pound of bacon"
