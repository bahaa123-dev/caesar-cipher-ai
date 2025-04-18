from cipher import decrypt_caesar
from ngram_model import NGramLanguageModel
import nltk
from nltk.corpus import gutenberg, words

# Ensure required corpora are downloaded
nltk.download('punkt')
nltk.download('gutenberg')
nltk.download('words')

# Build English vocabulary for word segmentation
english_vocab = set(w.lower() for w in words.words())

def segment_text(text: str) -> str:
    """
    Greedy word segmentation using a dictionary of English words.
    Tries to find the longest match from left to right.
    """
    text = text.lower()
    i = 0
    result = []

    while i < len(text):
        for j in range(len(text), i, -1):
            word = text[i:j]
            if word in english_vocab:
                result.append(word)
                i = j
                break
        else:
            # No match found; treat single character as unknown word
            result.append(text[i])
            i += 1

    return ' '.join(result)


def ai_caesar_crack(ciphertext: str) -> tuple[str, int, float]:
    # Load and combine multiple texts from the Gutenberg corpus
    print("Training language model on multiple Gutenberg books...")
    corpus_text = ''
    for file_id in gutenberg.fileids():
        corpus_text += gutenberg.raw(file_id)

    # Train N-gram model
    model = NGramLanguageModel(n=4)
    model.train(corpus_text)

    best_score = float('-inf')
    best_plaintext = ""
    best_shift = 0

    # Try all 26 Caesar shifts
    for shift in range(26):
        decrypted = decrypt_caesar(ciphertext, shift)
        segmented = segment_text(decrypted)
        score = model.score(segmented)

        print(f"Shift {shift:2d} ➔ Score: {score:.2f} ➔ {segmented[:50]}...")

        if score > best_score:
            best_score = score
            best_plaintext = segmented
            best_shift = shift

    return best_plaintext, best_shift, best_score


if __name__ == "__main__":
    # Test input: encrypted without spaces
    encrypted = "OAZHHLEOLEXLZHLEXKMVOLJ"
  # "cybersecurity" with Caesar shift 1
    result, shift_used, score = ai_caesar_crack(encrypted)

    print("\n🧠 AI Caesar Crack Result:")
    print(f"Best Decryption: {result}")
    print(f"Detected Shift: {shift_used}")
    print(f"Score: {score:.2f}")
