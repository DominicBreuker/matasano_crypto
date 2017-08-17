import base64

def hex2b64(s):
    raw = bytes.fromhex(hex_string)
    return base64.b64encode(raw).decode("utf-8")

if __name__ == "__main__":
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    base64_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert hex2b64(hex_string) == base64_string, "Error!!!"
