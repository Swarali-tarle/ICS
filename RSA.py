import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def generate_random_prime(start=100, end=300):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

def generate_keys():
    p = generate_random_prime()
    q = generate_random_prime()

    while q == p:
        q = generate_random_prime()

    print(f"Randomly chosen primes:\np = {p}, q = {q}")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = modinv(e, phi)

    return ((e, n), (d, n))

def encrypt(plaintext, public_key):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

def decrypt(ciphertext, private_key):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

def main():
    print("RSA Encryption/Decryption with Random Keys")

    public_key, private_key = generate_keys()
    print("\nPublic Key:", public_key)
    print("Private Key:", private_key)

    message = input("\nEnter message to encrypt: ")
    encrypted = encrypt(message, public_key)
    print("\nEncrypted:", encrypted)

    decrypted = decrypt(encrypted, private_key)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()











































































































    '''
    import random  # For generating random numbers

# Function to compute the Greatest Common Divisor (GCD) using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute modular inverse of 'a' under modulo 'm'
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:  # Check if x is the modular inverse of a
            return x
    return None

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# Generate a random prime number between start and end
def generate_random_prime(start=100, end=300):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

# Function to generate public and private keys
def generate_keys():
    # Step 1: Generate two distinct prime numbers
    p = generate_random_prime()
    q = generate_random_prime()
    while q == p:
        q = generate_random_prime()

    print(f"Randomly chosen primes:\np = {p}, q = {q}")

    # Step 2: Compute n = p * q and phi(n) = (p-1)*(q-1)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Step 3: Choose public exponent 'e' such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Step 4: Compute private exponent 'd' such that (e * d) % phi = 1
    d = modinv(e, phi)

    # Return public and private keys as tuples
    return ((e, n), (d, n))

# Function to encrypt a plaintext message using the public key
def encrypt(plaintext, public_key):
    e, n = public_key
    # Convert each character to its ASCII value, encrypt it using (char^e) % n
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# Function to decrypt ciphertext using the private key
def decrypt(ciphertext, private_key):
    d, n = private_key
    # Decrypt each character using (char^d) % n and convert back to character
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# Main function to run the encryption and decryption process
def main():
    print("RSA Encryption/Decryption with Random Keys")

    # Generate keys
    public_key, private_key = generate_keys()
    print("\nPublic Key:", public_key)
    print("Private Key:", private_key)

    # Take input message from user
    message = input("\nEnter message to encrypt: ")

    # Encrypt the message
    encrypted = encrypt(message, public_key)
    print("\nEncrypted:", encrypted)

    # Decrypt the message
    decrypted = decrypt(encrypted, private_key)
    print("Decrypted:", decrypted)

# Run the main function
if __name__ == "__main__":
    main()

    '''