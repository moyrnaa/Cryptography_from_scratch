# Caesar Cipher 

-This is my Python implementation of the Caesar Cipher, one of the oldest and simplest encryption methods.
⚠️ Note: The Caesar Cipher is not secure and should only be used for educational purposes or fun, as it can be easily decrypted."

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

## How to decrypt a Caesar cipher :
To decrypt a Caesar cipher, find out how many steps the letters were shifted. 
You can do this by looking for common letters or words in the encrypted text and comparing them to expected letters in the language.
Once you find the shift, move each letter back by that many steps to get the original text.

For example :
Suppose you see the encrypted text: "Wklv lv d whvw"
You notice that "lv" appears multiple times, which might be "is" in English.
If "l" was shifted to "i" and "v" to "s", that means the shift is 3.
Now, shift each letter back by 3:

W → T, k → h, l → i, v → s → "This"
l → i, v → s → "is"
d → a → "a"
w → t, h → e, v → s, w → t → "test"
So, the decrypted message is: "This is a test".
