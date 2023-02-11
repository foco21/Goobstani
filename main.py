import os

def decode_goobistani(goobistani_text):
    mapping = {
        "ا": "a",
        "В": "b",
        "Д": "c",
        "Ж": "d",
        "ه": "e",
        "ف": "f",
        "и": "g",
        "ح": "h",
        "ي": "i",
        "З": "j",
        "ک": "k",
        "Л": "l",
        "م": "m",
        "ن": "n",
        "ء": "o",
        "پ": "p",
        "з": "q",
        "ر": "r",
        "س": "s",
        "ت": "t",
        "ع": "u",
        "و": "v",
        "کس": "x",
        "Ф": "y",
        "ز": "z"
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
