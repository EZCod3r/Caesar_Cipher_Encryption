letter_to_num = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
    'w': 23, 'x': 24, 'y': 25, 'z': 26
}

print("______________Caesar Cipher Tool______________")
while True:
    second_code = ""
    message = ""
    result = ''
    new_num = 0
    key = 0
    print("1. Encrypt")
    print("2. Decrypt")
    choice = str(input("Choose an option (1 or 2): "))
    message = input("Enter the string: ")
    key = int(input("Enter the key: "))
    for char in message:
        if char.lower() in letter_to_num:
            num = letter_to_num[char.lower()]
            if choice == '1':  # Encrypt
                second_code = str(input("create a second code for authentication (3 numbers, 3 letters, 2 symbols): "))
                new_num = (num + key - 1) % 26 + 1
            elif choice == "2":  # Decrypt
                second_ask = input("Enter the second code: ")
                if second_ask == second_code:
                    print("Second code is correct!")
                    new_num = (num - key - 1) % 26 + 1

            new_char = list(letter_to_num.keys())[new_num - 1]

            if char.isupper():
                new_char = new_char.upper()

            result += new_char
        else:
            result += char

    if choice == '1':
        print('Encrypted string:', result)
    else:
        print('Decrypted string:', result)