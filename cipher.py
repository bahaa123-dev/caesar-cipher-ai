import string

def decrypt_caesar(text: str, shift: int) -> str:
    alpha = string.ascii_lowercase
    shifted = alpha[-shift:] + alpha[:-shift]  # shift backwards
    trans = str.maketrans(alpha, shifted)
    return text.lower().translate(trans)

if __name__ == "__main__":
    # Smoke‐test: should print "hello"
    sample = "ifmmp"       # “hello” shifted by +1
    result = decrypt_caesar(sample, 1)
    print(f"decrypt_caesar('{sample}',1) ➔ '{result}'")