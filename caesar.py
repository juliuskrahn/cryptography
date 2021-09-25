def translate_char(char: str, ring_offset=1):
    ring = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        " ",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        ".",
        ",",
        ":",
        "?",
        "!",
        ";",
    ]
    index = ring.index(char.lower())
    index = (index + ring_offset) % len(ring)
    return ring[index]


def caesar(text: str, ring_offset=1):
    translated = ""
    for char in text:
        translated += translate_char(char, ring_offset)
    return translated


message = input("Enter a message: ")
secret = int(input("Enter a secret (integer): "))
encrypted_message = caesar(message, secret)
print(f"Encrypted message: {encrypted_message}")
decrypted_message = caesar(encrypted_message, -secret)
print(f"Decrypted message: {decrypted_message}")
