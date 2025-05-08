import string  # For handling punctuation

class Vectorizer:
    def stantardize(self, text: str):
        """
        Converts text to lowercase and removes punctuation.
        """
        text = text.lower() 
        # Remove all punctuation characters (e.g., !"#$%&'()*+,-./ etc.)
        text = ''.join(char for char in text if char not in string.punctuation)
        return text

    def tokenize(self, text: str):
        """
        Standardizes and splits the text into tokens (words).
        """
        text = self.stantardize(text)
        # Splits on any whitespace (space, tab, newline, etc.)
        # Empty strings are automatically discarded.
        return text.split()

    def make_vocabulary(self, dataset):
        """
        Builds a vocabulary dictionary from a list of text strings (dataset).
        Adds a special token [UNK] for unknown words.
        """
        # Initialize vocabulary with:
        # '' → 0 (optional, sometimes used as a padding token)
        # '[UNK]' → 1 (used for unknown tokens)
        self.vocabulary = {"": 0, "[UNK]": 1}

        for text in dataset:
            tokens = self.tokenize(text)
            for token in tokens:
                if token not in self.vocabulary:
                    # Assign each new token the next available integer ID
                    self.vocabulary[token] = len(self.vocabulary)

        # Create reverse mapping: ID → token
        self.inverse_vocabulary = {v: k for k, v in self.vocabulary.items()}

    def encode(self, text: str):
        """
        Converts input text into a list of integers (token IDs).
        Unknown tokens are replaced with 1 ([UNK]).
        """
        tokens = self.tokenize(text)
        return [self.vocabulary.get(token, 1) for token in tokens]

    def decode(self, int_sequence):
        """
        Converts a list of token IDs back into a string.
        Unknown IDs return '[UNK]' as the default.
        """
        return " ".join(self.inverse_vocabulary.get(i, "[UNK]") for i in int_sequence)

