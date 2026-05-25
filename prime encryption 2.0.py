import random
import math

def is_prime(n, k=40):
    """Miller-Rabin primality test"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_large_prime(digits):
    """Generate a prime with approximately 'digits' decimal digits"""
    print(f"Generating a ~{digits}-digit prime (this may take 30-90 seconds depending on your computer)...")
    while True:
        lower = 10 ** (digits - 1)
        upper = 10 ** digits - 1
        candidate = random.randint(lower, upper)
        if candidate % 2 == 0:
            candidate += 1
        if is_prime(candidate):
            return candidate


# ====================== RSA KEY GENERATION ======================
print("=== RSA Key Generation with Large Primes ===\n")

prime_digits = 256          # Change to 20 for fast testing

p = generate_large_prime(prime_digits)
q = generate_large_prime(prime_digits)

n = p * q
phi = (p - 1) * (q - 1)

e = 65537
while math.gcd(e, phi) != 1:
    e += 2

d = pow(e, -1, phi)

print(f"\n✅ Keys generated successfully!")
print(f"Semiprime n has {len(str(n))} digits\n")


# ====================== HELPER FUNCTIONS ======================
def text_to_int(text):
    return int.from_bytes(text.encode('utf-8'), 'big')


def int_to_text(num):
    try:
        byte_length = (num.bit_length() + 7) // 8
        return num.to_bytes(byte_length, 'big').decode('utf-8')
    except:
        return "[Decoding Error]"


# ====================== MAIN PROGRAM ======================
while True:
    print("\n1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Quit")
    choice = input("\nChoose an option: ").strip()

    if choice == '3':
        print("\nGoodbye!")
        break

    if choice == '1':  # ====================== ENCRYPT ======================
        message = input("\nEnter the message to encrypt: ")
        m = text_to_int(message)

        if m >= n:
            print("❌ Message is too long for this key size!")
            print("   Try a shorter message or use smaller test primes.")
            continue

        ciphertext = pow(m, e, n)
        print("\n✅ Encrypted successfully!")
        print(f"Ciphertext:\n{ciphertext}")

    elif choice == '2':  # ====================== DECRYPT ======================
        try:
            ciphertext_str = input("\nPaste the ciphertext (big number): ").strip()
            ciphertext = int(ciphertext_str)

            decrypted_int = pow(ciphertext, d, n)
            decrypted_text = int_to_text(decrypted_int)

            print("\n✅ Decrypted successfully!")
            print(f"Original message: {decrypted_text}")

        except ValueError:
            print("❌ Invalid ciphertext! Please paste only numbers.")
        except Exception as ex:
            print(f"❌ Decryption failed: {ex}")

    else:
        print("Invalid option. Please choose 1, 2, or 3.")