import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64) # digest_size=64 means a 512-bit hash
    blake2_hash.update(message)
    return blake2_hash.digest()

def main():
    # Get input text from the user and encode it to UTF-8
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')

    # Compute the BLAKE2b hash
    hashed_text = blake2(text)

    # Print the original text and its BLAKE2b hash
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("BLAKE2 Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()