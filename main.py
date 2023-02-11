import os

def encode_goobistani(english_text):
    mapping = {
        "a": "ا",
        "b": "В",
        "c": "Д",
        "d": "Ж",
        "e": "ه",
        "f": "ف",
        "g": "и",
        "h": "ح",
        "i": "ي",
        "j": "З",
        "k": "ک",
        "l": "Л",
        "m": "م",
        "n": "ن",
        "o": "ء",
        "p": "پ",
        "q": "з",
        "r": "ر",
        "s": "س",
        "t": "ت",
        "u": "ع",
        "v": "و",
        "w": "و",
        "x": "کس",
        "y": "Ф",
        "z": "ز",
    }
    goobistani_text = ""
    for letter in english_text:
        if letter.lower() in mapping:
            goobistani_text += mapping[letter.lower()]
        else:
            goobistani_text += letter
    return goobistani_text

def main():
    os.system('clear')
    print("Goobistani Encoder\n")

    while True:
        # Get input from user
        english_text = input("Enter text in English: ")

        # Encode the input text
        goobistani_text = encode_goobistani(english_text)

        # Print the encoded text
        print(f"Encoded text: {goobistani_text}\n")

        # Ask if the user wants to encode more text
        response = input("Do you want to encode more text? (Y/N) ")
        if response.lower() != "y":
            break

if __name__ == "__main__":
    main()