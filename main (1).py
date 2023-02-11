import os

def decode_goobistani(goobistani_text):
    mapping = {
        "ا": "a",
        "б": "b",
        "ч": "c",
        "д": "d",
        "ع": "e",
        "ف": "f",
        "غ": "g",
        "ه": "h",
        "и": "i",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "أ": "o",
        "п": "p",
        "ق": "q",
        "р": "r",
        "س": "s",
        "т": "t",
        "у": "u",
        "в": "v",
        "ш": "w",
        "خ": "x",
        "ы": "y",
        "з": "z",
    }
    english_text = ""
    for letter in goobistani_text:
        if letter in mapping:
            english_text += mapping[letter]
        else:
            english_text += letter
    return english_text

def main():
    os.system('clear')
    print("Goobistani Decoder\n")

    while True:
        # Get input from user
        goobistani_text = input("Enter text in Goobistani: ")

        # Decode the input text
        english_text = decode_goobistani(goobistani_text)

        # Print the decoded text
        print(f"Decoded text: {english_text}\n")

        # Ask if the user wants to decode more text
        response = input("Do you want to decode more text? (Y/N) ")
        if response.lower() != "y":
            break

if __name__ == "__main__":
    main()
