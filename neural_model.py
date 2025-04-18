import numpy as np
from sklearn.neural_network import MLPClassifier
from cipher import decrypt_caesar

class ShiftClassifier:
    def __init__(self):
        self.model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)

    def featurize(self, texts):
        # Simple char‑level one‑hot: map 'a'–'z' to 0–25, pad/truncate to length L
        L = 100
        X = np.zeros((len(texts), L * 26))
        for i, t in enumerate(texts):
            for j, ch in enumerate(t.lower()[:L]):
                if ch.isalpha():
                    X[i, j * 26 + (ord(ch) - ord('a'))] = 1
        return X

    def train(self, plaintexts):
        # plaintexts: list of clean English strings
        X_texts, y = [], []
        for pt in plaintexts:
            for shift in range(26):
                X_texts.append(decrypt_caesar(pt, shift))
                y.append(shift)
        X = self.featurize(X_texts)
        y = np.array(y)
        self.model.fit(X, y)

    def predict_scores(self, candidates):
        # candidates: list of (shift, plaintext)
        texts = [pt for _, pt in candidates]
        X = self.featurize(texts)
        probs = self.model.predict_proba(X)
        # score = probability of correct shift
        return [probs[i, shift] for i, (shift, _) in enumerate(candidates)]