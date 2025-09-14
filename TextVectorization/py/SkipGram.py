import numpy as np
from collections import Counter
import sys
import os
sys.path.append(os.path.abspath("./py"))
#from helpers import tokenize   # relative import
import helpers
class SkipGram:
    def __init__(self, corpus, vocab_size=None, embedding_dim=100, window_size=2, learning_rate=0.025, epochs=5, min_count=5):
        
        self.corpus = helpers.tokenize(corpus)        # Simple tokenization for educational porpose.
        self.embedding_dim = embedding_dim    # Size of embeddings
        self.window_size = window_size        # used to slide window over center words
        self.learning_rate = learning_rate    # learning rate
        self.epochs = epochs                  # training epochs
        self.min_count = min_count            # Filter words by limited repeatation
        
        self.build_vocab(vocab_size) 
        self.initialize_weights()

        print(f'    Input embedding: {self.W.shape}')
        print(f'   Output embedding: {self.W_out.shape}')
        print(f'        Corpus size: {self.vocab_size + self.filtered_words}')
        print(f'    Vocabulary size: {self.vocab_size}')
        print(f'Embedding dimention: {self.embedding_dim}')
        print(f'     Filtered words: {self.filtered_words}')
        print(f'             Epochs: {epochs}')
    
    def build_vocab(self, vocab_size=None):
        # Count word frequencies
        word_counts = Counter(self.corpus)
        # Filter words by min_count
        self.vocab = [word for word, count in word_counts.most_common(vocab_size) if count >= self.min_count]
        self.vocab_size = len(self.vocab)
        self.filtered_words = word_counts.total() - self.vocab_size 
        self.word_to_idx = {word: idx for idx, word in enumerate(self.vocab)}
        self.idx_to_word = {idx: word for word, idx in self.word_to_idx.items()}

    def initialize_weights(self):
        '''
            Inintalize default input and output weights
        '''
        # Input embeddings: d x |V|
        self.W = np.random.uniform(low=-0.5 / self.embedding_dim, high= 0.5 / self.embedding_dim,size= (self.embedding_dim, self.vocab_size))
        # Output embeddings: |V| x d
        self.W_out = np.random.uniform(low=-0.5 / self.embedding_dim,high= 0.5 / self.embedding_dim,size= (self.vocab_size, self.embedding_dim))

    # Generates training pairs ([context word indices], center word index)
    def generate_training_data(self):
        training_data = []
        for i in range(len(self.corpus)):
            word = self.corpus[i]
            # this eccures for filtered words(count < self.min_count is filtered in build_vocab)
            if word not in self.word_to_idx: continue

            # get index of selected word 
            target_idx = self.word_to_idx[word]
            context = []
            # generates 'context words'  
            for j in range(-self.window_size, self.window_size + 1):
                
                # J == 0 is equivalent to the center word
                if j == 0: continue

                if 0 <= i + j < len(self.corpus):
                    ctx_word = self.corpus[i + j]
                    if ctx_word in self.word_to_idx:
                        # append index to the 'context words' list
                        context.append(self.word_to_idx[ctx_word])
            # if context words is not empty ...
            if context: training_data.append((context, target_idx))
        # Each element contains a ([context word indices], center word index)
        return training_data  

    def forward(self, center_word_idx):

        # Get hidden layer h for the center word
        h = self.W[:, center_word_idx]  # Shape: (embedding_dim,)
        
        # Compute logits u = W'^T h
        u = np.dot(self.W_out, h)  # Shape: (vocab_size,)
        
        # Compute softmax probabilities y
        # Subtract max for numerical stability
        y = helpers.softmax(u)

        return h, u, y

    def compute_loss(self,y, context_word_indices):
        loss = 0
        for idx in context_word_indices:
            loss += -np.log(y[idx] + 1e-10)
        return loss
    

    def backward(self, center_word_idx, context_word_idx, y, learning_rate=0.01):
        # Compute gradient w.r.t. u
        t = np.zeros(self.vocab_size)  # One-hot vector for context word
        t[context_word_idx] = 1
        e = y - t  # Shape: (vocab_size,)
        
        # Get hidden layer h
        h = self.W[:, center_word_idx]  # Shape: (embedding_dim,)
        
        # Compute gradient w.r.t. W' (outer product: h * (y - t)^T)
        grad_W_out = np.outer(e, h.T)  # Shape: (embedding_dim, vocab_size)
        
        # Compute gradient w.r.t. h
        grad_h = np.dot(e,self.W_out)  # Shape: (embedding_dim,)
        
        # Compute gradient w.r.t. W (only center_word_idx column is updated)
        grad_W = np.zeros_like(self.W)  # Shape: (embedding_dim, vocab_size)
        grad_W[:, center_word_idx] = grad_h
        
        self.W_out -= learning_rate * grad_W_out

        self.W -= learning_rate * grad_W
        
        return grad_W, grad_W_out

    def train(self, verbose=True):
        
        training_data =  self.generate_training_data()
        print(f'       Running loop: {len(training_data)}x{self.epochs} = {len(training_data)*self.epochs}')
        print('Training ...')
        
        loss = []

        for epoch in range(self.epochs):
            epoch_loss = 0
            for context_words, center_word in training_data:
                # Forward
                h, u, y = self.forward(center_word)
        
                # Ensure context_words is a list
                #if isinstance(context_words, int): context_words = [context_words]

                # Compute average of loss over all context words
                e = self.compute_loss(y, context_words)/len(context_words)
                
                epoch_loss +=e
                
                # Backward: update for each context word
                for o in context_words:
                    self.backward(center_word, o, y, learning_rate=0.001)
                
            # average loss of epoch
            loss.append(epoch_loss / len(training_data))

            if verbose: print(f"Epoch {epoch + 1}/{self.epochs}, Loss: {epoch_loss / len(training_data):.4f}")

        print('Training ends.')
        
        self.loss = loss

    def get_embedding(self, word):
        """
        Get embedding for a word
        """
        if word in self.word_to_idx:
            return self.W[:, self.word_to_idx[word]]
        else:
            return None

    def most_similar(self, word, top_n=5):
        """
        Find most similar words
        """
        if word not in self.word_to_idx:
            return []
        
        # Get query embedding
        query_embedding = self.get_embedding(word)
        
        # Calculate cosine similarities
        similarities = {}
        for idx, other_word in self.idx_to_word.items():
            if other_word != word:
                other_embedding = self.W[:, idx]
                cosine_sim = np.dot(query_embedding, other_embedding) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(other_embedding)
                )
                similarities[other_word] = cosine_sim
        
        # Return top N most similar words
        return sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:top_n]
    