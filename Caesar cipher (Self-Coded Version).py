dictionary_of_letters = {
    'a' or 'A': 1,
    'b' or 'B': 2,
    'c' or 'C': 3,
    'd' or 'D': 4,
    'e' or 'E': 5,
    'f' or 'F': 6,
    'g' or 'G': 7,
    'h' or 'H': 8,
    'i' or 'I': 9,
    'j' or 'J': 10,
    'k' or 'K': 11,
    'l' or 'L': 12,
    'm' or 'M': 13,
    'n' or 'N': 14,
    'o' or 'O': 15,
    'p' or 'P': 16,
    'q' or 'Q': 17,
    'r' or 'R': 18,
    's' or 'S': 19,
    't' or 'T': 20,
    'u' or 'U': 21,
    'v' or 'V': 22,
    'w' or 'W': 23,
    'x' or 'X': 24,
    'y' or 'Y': 25,
    'z' or 'Z': 26,}
original_string = str(input('Enter a string to encrypt: '))
key = int(input('Enter a key to encrypt: '))
encrypted_string = ''
for letter in original_string:
    if letter in dictionary_of_letters:
        letter = dictionary_of_letters
encrypted_string = letter
print(encrypted_string)
