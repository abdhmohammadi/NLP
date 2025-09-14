from typing import List, Iterable, Tuple, Dict
import re
from collections import Counter
import numpy as np
import pandas as pd
# -----------------------------
# 2) Minimal tokenizer
# -----------------------------
def tokenize(s: str) -> List[str]:
    # Lowercase and keep only alphabetic tokens (very simple)
    return re.findall(r"[a-zA-Z']+", s.lower()) 


# 3) One-Hot Vectorizer (document-level multi-hot)
class OneHotVectorizer:
    def __init__(self, min_freq: int = 1, max_vocab: int | None = None, stopwords: Iterable[str] | None = None):
        self.min_freq = min_freq
        self.max_vocab = max_vocab
        self.stopwords = set(stopwords) if stopwords else set()
        self.vocab_: Dict[str, int] = {}
        self.inv_vocab_: List[str] = []
    
    
    def fit(self, texts: Iterable[str]) -> "OneHotVectorizer":
        '''
            This method takes raw texts, counts tokens, filters them, sorts them, applies limits, and builds two dictionaries:
        
            vocab_ (word → index)

            inv_vocab_ (index → word)

            This is the core of one-hot encoding: building a fixed vocabulary.
        '''
        # finding word(token) frequency
        freq = Counter()
        for s in texts:
            tokens = [t for t in tokenize(s) if t not in self.stopwords]
            freq.update(tokens)
        
        # Keeps only tokens that appear at least min_freq times.
        # For example, if min_freq=2, words that appear only once are removed.
        items = [(tok, c) for tok, c in freq.items() if c >= self.min_freq]

        # Sorts vocabulary:
        # First by frequency (-x[1] means descending order).
        # Then alphabetically (x[0]) to break ties.
        # So you get most frequent words first, in a consistent order.
        items.sort(key=lambda x: (-x[1], x[0]))
        
        # If a maximum vocabulary size is set (e.g., 10,000 words), it keeps only the top-N words.
        # Useful for memory and performance.
        if self.max_vocab is not None:
            items = items[: self.max_vocab]
        
        # Builds a dictionary mapping word → index.
        # Example: {'dog': 0, 'cat': 1, 'fish': 2}
        self.vocab_ = {tok: i for i, (tok, _) in enumerate(items)}
        self.inv_vocab_ = [tok for tok, _ in items]
        
        # also compute the multi-hot vectors for given texts and store them
        self.last_vectors_ = self.transform(texts)

        return self

    def vector_df(self, texts: Iterable[str] = None):
        """
        Print the one-hot / multi-hot vectors.
        If texts are provided, it will transform and print them,
        otherwise it prints the last fitted vectors.
        """
        if texts is not None:
            vectors = self.transform(texts)
        else:
            vectors = self.last_vectors_

        vecs = []
        for i, vec in enumerate(vectors):
            vecs.append(vec)
        
        return pd.DataFrame(data=vectors, columns=self.vocab_.keys())
            
    def transform(self, texts: Iterable[str]) -> np.ndarray:
        '''
        The main task of this function is to convert a list of input texts into a One-Hot encoded matrix 
        
        representation using the vocabulary that was built earlier in the fit() function.
        
        '''
        V = len(self.vocab_)
        texts_list = list(texts)
        X = np.zeros((len(texts_list), V), dtype=np.float32)
        for i, s in enumerate(texts_list):
            tokens = set(t for t in tokenize(s) if t in self.vocab_ and t not in self.stopwords)
            for t in tokens:
                X[i, self.vocab_[t]] = 1.0
        return X
    
    def fit_transform(self, texts: Iterable[str]) -> np.ndarray:
        self.fit(texts)
        return self.transform(texts)

STOPWORDS = {
    "the","is","a","an","and","or","to","for","in","on","of","it","this","that","i","my","do","you","have","with","after"
}