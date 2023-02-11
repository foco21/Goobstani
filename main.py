import os

def encode_goobistani(english_text):
    mapping = {
        "a": "ا",
        "b": "б",
        "c": "ч",
        "d": "д",
        "e": "ع",
        "f": "ف",
        "g": "غ",
        "h": "ه",
        "i": "и",
        "j": "й",
        "k": "к",
        "l": "л",
        "m": "м",
        "n": "н",
        "o": "أ",
        "p": "п",
        "q": "ق",
        "r": "р",
        "s": "س",
        "t": "т",
        "u": "у",
        "v": "в",
        "w": "ш",
        "x": "خ",
        "y": "ы",
        "z": "з"
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
