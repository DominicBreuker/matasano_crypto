def xor(b1, b2):
    assert len(b1) == len(b2), \
        "Can only XOR elements of equal length ({} / {})" \
        .format(len(b1), len(b2))
    return bytes([ a ^ b for (a,b) in zip(b1, b2)])

if __name__ == "__main__":
    b1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    b2 = bytes.fromhex("686974207468652062756c6c277320657965")
    result = bytes.fromhex("746865206b696420646f6e277420706c6179")
    assert xor(b1, b2) == result, "ERROR !!!"
