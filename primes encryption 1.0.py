import random


def is_prime(n, k=40):
    """Miller-Rabin primality test. Returns True if n is probably prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as d * 2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)  # fast modular exponentiation
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # composite
    return True  # probably prime


def generate_large_prime(digits=256):
    """Generate a random prime with exactly 'digits' decimal digits."""
    print(f"Generating a {digits}-digit prime... (this usually takes < 2 seconds)")

    while True:
        # Random number with exactly 'digits' digits
        lower = 10 ** (digits - 1)
        upper = 10 ** digits - 1
        candidate = random.randint(lower, upper)

        # Make it odd
        if candidate % 2 == 0:
            candidate += 1

        if is_prime(candidate):
            return candidate


# ====================== USAGE ======================
if __name__ == "__main__":
    prime = generate_large_prime(256)
    print("\n✅ Success! Here is your 256-digit prime number:\n")
    print(prime)
    print(f"\nNumber of digits: {len(str(prime))}")

    # Optional: save it to a file so you can reuse it
    with open("my_256_digit_prime.txt", "w") as f:
        f.write(str(prime))
    print("\n💾 Saved to 'my_256_digit_prime.txt'")