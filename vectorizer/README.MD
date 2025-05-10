## Text Vectorization Methods

This project demonstrates how to build a basic text vectorizer **from scratch**, without using external libraries like `scikit-learn` or `transformers`. It is ideal for students beginning their journey into **Natural Language Processing (NLP)**.


## History

The concept of **text vectorization** in Natural Language Processing (NLP) has evolved over several decades, with contributions from various researchers and institutions.

### Early Foundations

The foundational idea that "a word is characterized by the company it keeps" was proposed by British linguist **John Rupert Firth** in 1957. This principle, known as the *distributional hypothesis*, suggests that words used in similar contexts tend to have similar meanings. It laid the groundwork for representing words numerically based on their contextual usage.([Wikipedia][1], [Wikipedia][2])

### Latent Semantic Analysis (LSA)

In the late 1980s, researchers **Scott Deerwester**, **Susan Dumais**, **George Furnas**, **Richard Harshman**, **Thomas Landauer**, **Karen Lochbaum**, and **Lynn Streeter** developed **Latent Semantic Analysis (LSA)**. LSA is a technique that analyzes relationships between a set of documents and the terms they contain by producing a set of concepts related to the documents and terms. It uses singular value decomposition (SVD) to reduce the dimensionality of the term-document matrix, capturing the underlying semantic structure in the data. ([Wikipedia][2])

### Neural Probabilistic Language Models

In 2003, **Yoshua Bengio** and colleagues introduced the **Neural Probabilistic Language Model**, which aimed to address the curse of dimensionality in language modeling. This model proposed learning a distributed representation for words, allowing for better generalization to unseen word sequences. It marked a significant shift towards using neural networks for learning word representations.([Wikipedia][1])

### Word2Vec

A major advancement came in 2013 when **Tomáš Mikolov** and his team at Google developed **Word2Vec**, a set of models that produce word embeddings. Word2Vec introduced two architectures: Continuous Bag of Words (CBOW) and Skip-Gram, both of which efficiently learn word representations that capture semantic and syntactic relationships. This work significantly popularized the use of dense vector representations in NLP. ([Wikipedia][3], [Haystack][4])

### GloVe

In 2014, researchers at Stanford University, including **Jeffrey Pennington**, **Richard Socher**, and **Christopher Manning**, developed **GloVe (Global Vectors for Word Representation)**. GloVe combines the benefits of global matrix factorization and local context window methods, producing word embeddings by aggregating global word-word co-occurrence statistics from a corpus. ([Wikipedia][5])

### Summary

While the idea of representing text numerically has roots in the mid-20th century, significant milestones include:

* **1957**: Distributional hypothesis by John Rupert Firth.
* **Late 1980s**: Development of LSA by Deerwester et al.
* **2003**: Neural Probabilistic Language Model by Bengio et al.
* **2013**: Introduction of Word2Vec by Mikolov et al.
* **2014**: Development of GloVe by Pennington et al.([Wikipedia][1], [Wikipedia][2], [Wikipedia][3])

Each of these contributions has played a pivotal role in shaping the methods used for text vectorization in NLP today.

[1]: https://en.wikipedia.org/wiki/Word_embedding?utm_source=chatgpt.com "Word embedding"
[2]: https://en.wikipedia.org/wiki/Latent_semantic_analysis?utm_source=chatgpt.com "Latent semantic analysis"
[3]: https://en.wikipedia.org/wiki/Word2vec?utm_source=chatgpt.com "Word2vec"
[4]: https://haystack.deepset.ai/blog/what-is-text-vectorization-in-nlp?utm_source=chatgpt.com "What Is Text Vectorization? Everything You Need to Know | Haystack"
[5]: https://en.wikipedia.org/wiki/GloVe?utm_source=chatgpt.com "GloVe"


## 📌 What You’ll Learn

- How to preprocess text (lowercase + punctuation removal)
- How to tokenize text into words
- How to build a vocabulary from a dataset
- How to encode words into numbers
- How to decode numbers back into words
- How to handle unknown or unseen words

---

## 🧪 Usage Example (from the notebook)

```python
import TextVectorization as tv

vectorizer = tv.Vectorizer()

dataset = [
    "I write, erase, rewrite",
    "Erase again, and then",
    "A poppy blooms."
]

# Build vocabulary
vectorizer.make_vocabulary(dataset)

# Encode a sentence
encoded = vectorizer.encode("I write again")
print(encoded)  # Output: [2, 3, 6] (example)

# Decode back to text
print(vectorizer.decode(encoded))  # Output: i write again
```

---

## 🔍 Special Tokens

* `[UNK]`: Used when a word is not found in the vocabulary
* `""` (empty string): Reserved for out of vocabulary(OOV) string, ID = 0

---

## 🧰 Requirements

This project uses only the Python standard library.

✅ No external packages required.

---

## 📘 For Educators

This project is intentionally written without high-level libraries to **teach students the fundamentals** of:

* Vocabulary building
* Tokenization logic
* How NLP models understand text as numbers

---

## ✅ Next Steps

Students can extend this project by:

* Adding stopword removal
* Using frequency thresholds for vocabulary
* Creating n-gram tokenizers
* Moving from word-level to subword-level tokenization
