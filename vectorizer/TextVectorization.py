import string

class Vectorizer:
    def stantardize(self, text:str):
        text = text.lower()
        # punctuation---> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        # removeing punctuation
        text = ''.join(char for char in text if char not in string.punctuation)

        return text
    
    def tokenize(self, text:str):

        text = self.stantardize(text)
        # Simple tokenization with split the text 
        # split on any whitespace character (including \n \r \t \f and spaces) and 
        # will discard empty strings from the result.
        return text.split()
    
    def make_vocabulary(self, dataset):

        # Initalize the vocabulary with OOV(out of vocabulary) and UNK (unkown token)
        self.vocabulary = {"": 0, "[UNK]": 1}

        for text in dataset:

            tokens = self.tokenize(text)

            for token in tokens:
                if token not in self.vocabulary:
                    self.vocabulary[token] = len(self.vocabulary)
        
        self.inverse_vocabulary = dict((v,k) for k, v in self.vocabulary.items())
    
    def encode(self, text:str):
        
        tokens = self.tokenize(text)

        return [self.vocabulary.get(token,1) for token in tokens]

    def decode(self, int_sequence):
        # return decoded string from encoded values,
        # if a token not found in the vocabulary, returns [UNK] as default value.
        return " ".join(self.inverse_vocabulary.get(i,"[UNK]") for i in int_sequence)




print(string.punctuation)