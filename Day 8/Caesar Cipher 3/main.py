
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = []
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:

        if letter.isalpha():
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text.append(alphabet[shifted_position])
        else:
            output_text.append(letter)
    output_text = "".join(output_text)
    print(f"Here is the {encode_or_decode}d result: {output_text}")

resume = "yes"
while resume == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    resume = input("Will you want to continue?").lower()





