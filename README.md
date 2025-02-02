# Cryptography_from_scratch
# Caesar Cipher , It’s named after Julius Caesar ...

- This is my Python implementation of the Caesar Cipher, one of the oldest and simplest encryption methods.
- the Caesar cipher should only be used for fun because it is very easy to solve ...

## What’s a Caesar Cipher?

So, the Caesar Cipher is basically a way to scramble text by shifting each letter by a certain number of places in the alphabet. For example, if you shift by 3:
- A becomes D
- B becomes E
- Z wraps around to C


## How Does It Work?

1. You take some text like "hello" and pick a number to shift the letters by (like 3).
2. Each letter in the text gets shifted by that number.
3. If you go past "Z" or "z", it wraps around to the beginning of the alphabet.
4. Numbers, symbols, and spaces stay the same.

For example:
- **Plaintext**: "hello"
- **Shift**: 3
- **Ciphertext**: "khoor"
for more infos: https://en.wikipedia.org/wiki/Caesar_cipher
