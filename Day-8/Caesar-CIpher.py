alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def caesar(direction, text, shift):
    if direction == "encode":
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            cipher_text += alphabet[new_position]
        print(f"This is the cipher text: {cipher_text}")
    elif direction == "decode":
        plain_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            plain_text += alphabet[new_position]
        print(f"This is the plain text: {plain_text}")

caesar(direction,text,shift)