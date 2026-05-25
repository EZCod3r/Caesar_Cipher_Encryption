letter_to_num = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
    'w': 23, 'x': 24, 'y': 25, 'z': 26
}

print("______________ Caesar Cipher Tool ______________")

# This variable will remember the second code across multiple operations
second_code = ""

while True:
    print("\n1. Encrypt")
    print("2. Decrypt")
    choice = input("\nChoose an option (1 or 2): ").strip()

    if choice not in ['1', '2']:
        print("Invalid option! Please choose 1 or 2.")
        continue

    message = input("Enter the string: ")
    try:
        key = int(input("Enter the key: "))
    except ValueError:
        print("Error: Key must be a number!")
        continue

    result = ''

    if choice == '1':  # ==================== ENCRYPT ====================
        # Ask for second code only during encryption
        second_code = input("Create a second code for authentication: ").strip()

        for char in message:
            if char.lower() in letter_to_num:
                num = letter_to_num[char.lower()]
                new_num = (num + key - 1) % 26 + 1
                new_char = list(letter_to_num.keys())[new_num - 1]

                if char.isupper():
                    new_char = new_char.upper()

                result += new_char
            else:
                result += char

        print("\n✅ Encryption successful!")
        print(f"Encrypted string : {result}")
        print(f"Second auth code : {second_code}")
        print("(Remember this second code! You will need it to decrypt)")

    elif choice == '2':  # ==================== DECRYPT ====================
        if second_code == "":
            print("❌ No second code was set during encryption!")
            print("Please encrypt a message first.")
        else:
            second_ask = input("Enter the second code: ").strip()

            if second_ask == second_code:
                print("✅ Second code is correct! Decrypting...\n")

                for char in message:
                    if char.lower() in letter_to_num:
                        num = letter_to_num[char.lower()]
                        new_num = (num - key - 1) % 26 + 1
                        new_char = list(letter_to_num.keys())[new_num - 1]

                        if char.isupper():
                            new_char = new_char.upper()

                        result += new_char
                    else:
                        result += char

                print(f"Decrypted string: {result}")
            else:
                print("❌ Incorrect second code! Decryption denied.")

    # Ask to continue
    again = input("\nDo you want to encrypt/decrypt another message? (y/n): ").strip().lower()
    if again != 'y':
        print("\nThank you for using Caesar Cipher Tool. Goodbye!")
        break