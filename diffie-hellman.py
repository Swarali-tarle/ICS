def diffie_hellman():
    print("=== Diffie-Hellman Key Exchange ===")

    p = int(input("Enter a large prime number (p): "))
    g = int(input("Enter a primitive root modulo p (g): "))

    a = int(input("User A, enter your private key (a): "))
    b = int(input("User B, enter your private key (b): "))

    A = pow(g, a, p)  # A = g^a mod p
    B = pow(g, b, p)  # B = g^b mod p

    print(f"User A sends public key: {A}")
    print(f"User B sends public key: {B}")

    shared_key_a = pow(B, a, p)  # (B^a) mod p
    shared_key_b = pow(A, b, p)  # (A^b) mod p

    print(f"User A computes shared key: {shared_key_a}")
    print(f"User B computes shared key: {shared_key_b}")

    if shared_key_a == shared_key_b:
        print(f"\nShared secret established successfully! Key: {shared_key_a}")
    else:
        print("\nError: Keys do not match.")

diffie_hellman()

















































































































'''
# Define the function for Diffie-Hellman Key Exchange
def diffie_hellman():
    print("=== Diffie-Hellman Key Exchange ===")

    # Step 1: Get a large prime number and a primitive root from the user
    p = int(input("Enter a large prime number (p): "))  # Public prime number (modulus)
    g = int(input("Enter a primitive root modulo p (g): "))  # Generator (base)

    # Step 2: Both users choose their private keys (kept secret)
    a = int(input("User A, enter your private key (a): "))  # User A's private key
    b = int(input("User B, enter your private key (b): "))  # User B's private key

    # Step 3: Compute public keys to be exchanged
    A = pow(g, a, p)  # A = g^a mod p → User A's public key
    B = pow(g, b, p)  # B = g^b mod p → User B's public key

    # Step 4: Exchange public keys
    print(f"User A sends public key: {A}")
    print(f"User B sends public key: {B}")

    # Step 5: Compute the shared secret key using the received public key
    shared_key_a = pow(B, a, p)  # User A computes: (User B's public key)^a mod p
    shared_key_b = pow(A, b, p)  # User B computes: (User A's public key)^b mod p

    # Step 6: Display computed shared keys
    print(f"User A computes shared key: {shared_key_a}")
    print(f"User B computes shared key: {shared_key_b}")

    # Step 7: Validate if both users have derived the same shared key
    if shared_key_a == shared_key_b:
        print(f"\nShared secret established successfully! Key: {shared_key_a}")
    else:
        print("\nError: Keys do not match.")

# Call the function to execute the key exchange
diffie_hellman()

'''