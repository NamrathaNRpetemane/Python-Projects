# Alphabet list for Caesar cipher
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

def caesar(original_text, shift_amount, encode_or_decode):
    """
    Perform Caesar cipher encoding or decoding.
    """
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            # Handle characters not in the alphabet (numbers, symbols, spaces)
            output_text += letter
        else:
            # Shift the position while ensuring it wraps around using modulus
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Cipher program loop
should_continue = True

while should_continue:
    # Get user input for direction, text, and shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ["encode", "decode"]:
        print("Invalid input! Please type 'encode' or 'decode'.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Invalid input! Please enter a valid number for the shift.")
        continue

    # Call the Caesar cipher function
    caesar(original_text = text, shift_amount=shift, encode_or_decode=direction)

    # Ask user if they want to restart
    restart = input("Type 'yes' if you want to continue the game, or type 'no' to exit:\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
