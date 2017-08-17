# Matasano Crypto Challenges

https://cryptopals.com/

## Set 1 - Basics

### Convert Hex to Base64

Convert the hex string `49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d` to Base64 representation `SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t`.

### Fixed XOR

Write a function to compute the XOR of two equal length buffers.

Hex strings `1c0111001f010100061a024b53535009181c` and `686974207468652062756c6c277320657965` should produce `746865206b696420646f6e277420706c6179`.

### Single byte XOR cipher

The hex encoded string `1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736` contains a message that was encrypted by XORing it with a single character. Break it. Automatically, e.g., by scoring with respect to character frequencies.

### Detect single character XOR

One of the 60 hex strings in `set1/data/4.txt` contains a message encrypted with single byte XOR. Find it!

### Implement repeating-key XOR

Encrypt the following text with repeating-key XOR and use key `ICE`:

```
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
```

The result will be:

```
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```

Encrypt more stuff with it to get a feeling for it.

### Break repeating-key XOR
