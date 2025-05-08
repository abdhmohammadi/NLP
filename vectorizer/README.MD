## Simple Text Vectorizer in Python

This project demonstrates how to build a basic text vectorizer **from scratch**, without using external libraries like `scikit-learn` or `transformers`. It is ideal for students beginning their journey into **Natural Language Processing (NLP)**.


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
