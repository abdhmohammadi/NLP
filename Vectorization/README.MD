## Text Vectorization Methods

This notebook demonstrates the basic concepts of building a basic text vectorizer **from scratch**, without using external libraries like `scikit-learn` or `transformers`. It then explores traditional and advanced methods for a deeper understanding. If you are interested, a brief history of its emergence is also provided in [Text vectorization history](/History.html).


### Word2Vec

A major advancement came in 2013 when **Tomáš Mikolov** and his team at Google developed **Word2Vec**, a set of models that produce word embeddings. Word2Vec introduced two architectures: Continuous Bag of Words (CBOW) and Skip-Gram, both of which efficiently learn word representations that capture semantic and syntactic relationships. This work significantly popularized the use of dense vector representations in NLP. ([Wikipedia][3], [Haystack][4])

### GloVe

In 2014, researchers at Stanford University, including **Jeffrey Pennington**, **Richard Socher**, and **Christopher Manning**, developed **GloVe (Global Vectors for Word Representation)**. GloVe combines the benefits of global matrix factorization and local context window methods, producing word embeddings by aggregating global word-word co-occurrence statistics from a corpus. ([Wikipedia][5])

### Summary

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

## ✅ Next Steps
....
