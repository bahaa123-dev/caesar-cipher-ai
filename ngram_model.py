import math
from collections import Counter
from nltk import ngrams, word_tokenize

class NGramLanguageModel:
    def __init__(self, n=2, delta=0.1):
        self.n = n
        self.delta = delta
        self.counts = Counter()
        self.context_counts = Counter()
        self.vocab = set()

    def train(self, corpus_text: str):
        try:
            tokens = word_tokenize(corpus_text.lower())
        except LookupError:
            import nltk
            nltk.download('punkt')
            tokens = word_tokenize(corpus_text.lower())

        self.vocab.update(tokens)
        for ngram in ngrams(tokens, self.n):
            context = ngram[:-1]
            self.counts[ngram] += 1
            self.context_counts[context] += 1

    def trigram_prob(self, ngram):
        context = ngram[:-1]
        num = self.counts[ngram] + self.delta
        den = self.context_counts[context] + self.delta * len(self.vocab)
        return num / den

    def score(self, text: str) -> float:
        tokens = word_tokenize(text.lower())
        print("Scoring tokens:", tokens)  # Optional debug
        score = 0.0
        for ngram in ngrams(tokens, self.n):
            score += math.log(self.trigram_prob(ngram))

        return score


if __name__ == "__main__":
    import nltk
    from nltk.corpus import gutenberg

    # Combine multiple books from Gutenberg
    print("Training trigram model on multiple Gutenberg books...")
    corpus_text = ''
    for file_id in gutenberg.fileids():
        corpus_text += gutenberg.raw(file_id)



    model = NGramLanguageModel(n=2)
    model.train(corpus_text)

    test_sentence = "to be or not to be"
    score = model.score(test_sentence)

    print(f"Score for: '{test_sentence}' ➔ {score}")
