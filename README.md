# NLP Fundamentals with Practical Implementations

This repository offers a hands-on exploration of fundamental Natural Language Processing (NLP) techniques. Through practical examples implemented in Jupyter Notebooks, it demonstrates how to preprocess text, analyze linguistic features, and extract meaningful information using popular NLP libraries.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [References](#references)
- [License](#license)

## Overview

The project encompasses a range of NLP tasks, including:

- Text preprocessing
- Tokenization
- Lemmatization and stemming
- Stopwords removal
- Named Entity Recognition (NER)
- Topic modeling
- Sentiment analysis

By utilizing libraries such as Hugging Face Transformers, spaCy, and NLTK, the repository provides insights into the practical application of these techniques.

## Features

- **Tokenization**: Breaking down text into tokens using Hugging Face's BERT tokenizer.
- **Lemmatization**: Reducing words to their base forms with spaCy.
- **Stemming**: Simplifying words to their root forms using NLTK's PorterStemmer.
- **Stopwords Removal**: Eliminating common words that may not add significant meaning.
- **Named Entity Recognition (NER)**: Identifying entities like names, organizations, and dates using spaCy and Hugging Face Transformers.
<!-- 
- **Topic Modeling**: Discovering abstract topics within text data.
- **Sentiment Analysis**: Assessing the emotional tone behind a body of text.
 -->

## Installation

To set up the environment and run the notebooks:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/abdhmohammadi/NLP.git
   cd NLP
   ```

2. **Create and activate a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   Ensure you have the necessary libraries installed. You can install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If a `requirements.txt` file is not present, you may need to install the libraries manually, such as `transformers`, `spacy`, and `nltk`.*

## Usage

Open the Jupyter Notebook to explore the NLP techniques:

```bash
jupyter notebook NLP-Fundamentals.ipynb
```

Follow the notebook cells sequentially to understand and experiment with various NLP processes.

## References

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [spaCy Documentation](https://spacy.io/)
- [NLTK Documentation](https://www.nltk.org/)

- ## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
