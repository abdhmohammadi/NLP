# NLP Fundamentals – Core Concepts and Techniques

This subdirectory provides foundational materials for Natural Language Processing (NLP), focusing on essential concepts and practical implementations. It serves as a starting point for those new to NLP or looking to reinforce their understanding of basic techniques.

## Contents

- **Tokenization**: Dividing text into meaningful units.
- **Lemmatization**: Reducing words to their base or dictionary form.
- **Stemming**: Trimming words to their root forms.
- **Stopwords Removal**: Eliminating common words that may not add significant meaning.
- **Named Entity Recognition (NER)**: Identifying entities like names, organizations, and dates.

## Getting Started

### Prerequisites

Ensure you have Python installed. It's recommended to use a virtual environment to manage dependencies.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/abdhmohammadi/NLP.git
   cd NLP/fundamental
   ```

2. **Create and activate a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   If a `requirements.txt` file is present:

   ```bash
   pip install -r requirements.txt
   ```

   If not, you may need to install libraries manually, such as `nltk`, `spacy`, and `transformers`:

   ```bash
   pip install nltk spacy transformers
   ```

   Additionally, download necessary resources for `nltk` and `spacy`:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')

   import spacy
   spacy.cli.download("en_core_web_sm")
   ```

## Usage

Open the Jupyter Notebook(s) in this directory to explore and experiment with various NLP techniques:

```bash
jupyter notebook
```

Navigate to the desired notebook and follow the instructions provided in each section.

## References

- [NLTK Documentation](https://www.nltk.org/)
- [spaCy Documentation](https://spacy.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
