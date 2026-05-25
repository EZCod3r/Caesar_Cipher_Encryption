# Dictionary mapping letter to position (1-26)
letter_to_num = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
    'w': 23, 'x': 24, 'y': 25, 'z': 26
}

original_string = input('Enter a string to encrypt: ')
key = int(input('Enter a key (shift amount): '))

encrypted_string = ''

for char in original_string:
    if char.lower() in letter_to_num:
        num = letter_to_num[char.lower()]
        new_num = (num + key - 1) % 26 + 1
        new_char = list(letter_to_num.keys())[new_num - 1]
        if char.isupper():
            new_char = new_char.upper()
        encrypted_string += new_char
    else:
        encrypted_string += char

print('Encrypted string:', encrypted_string)