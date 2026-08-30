# 🔎 Semantic Search Engine

A lightweight semantic search engine built with **Python**, **Sentence Transformers**, **scikit-learn**, and **Streamlit**.

The project demonstrates how text can be converted into vector embeddings and searched using **cosine similarity** instead of exact keyword matching.



---

## 🎯 Project Goal

The goal of this project is to build a semantic search system over a collection of documents.

Unlike traditional keyword search, semantic search focuses on the **meaning of the query** and the **meaning of the documents**.

### Basic workflow

```text
User Query
    ↓
Embedding Model
    ↓
Query Vector
    ↓
Cosine Similarity
    ↓
Top-K Documents
```

---

## ✨ Current Features

* Generate text embeddings using `sentence-transformers`
* Semantic similarity using cosine similarity
* Top-K document retrieval
* CSV-based document loading
* Configurable embedding model
* Configurable number of search results
* Streamlit web interface
* Modular project architecture

---

## 🏗️ Project Structure

```text
semantic-search/
│
├── data/
│   └── documents.csv
│
├── src/
│   ├── __init__.py
│   ├── app.py
│   │
│   ├── enums/
│   │   └── __init__.py
│   │
│   ├── helpers/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── data_loader.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── embedding_model.py
│   │   └── document_embedder.py
│   │
│   ├── search/
│   │   ├── __init__.py
│   │   └── engine.py
│   │
│   └── services/
│       ├── __init__.py
│       └── search_service.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### Architecture

The project follows a modular architecture where each component has a single responsibility:

* **Config** — Loads and validates application settings from `.env`.
* **Data Loader** — Loads documents from the CSV dataset.
* **Embedding Model** — Converts text into numerical vector representations.
* **Document Embedder** — Generates embeddings for the document collection.
* **Search Engine** — Calculates cosine similarity and retrieves the most similar documents.
* **Search Service** — Coordinates the different components.
* **Streamlit App** — Provides the user interface.

---

## 🧠 Embedding Model

The current implementation uses:

```text
all-MiniLM-L6-v2
```



### Environment Variables

| Variable          | Description                                    |
| ----------------- | ---------------------------------------------- |
| `EMBEDDING_MODEL` | Sentence Transformer model used for embeddings |
| `TOP_K`           | Number of search results returned              |
| `DATA_PATH`       | Path to the document dataset                   |





## 🚀 Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd semantic-search
```

### 2. Create the Conda environment

```bash
conda create -n semantic-search python=3.11 -y
conda activate semantic-search
```

### 3. Install PyTorch CPU

The current MVP is designed to run on CPU.

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### 4. Install project dependencies

```bash
pip install -r requirements.txt
```
### 5. Configure Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```


### 6. ▶️ Running the Application

From the project root:

```bash
python -m streamlit run src/app.py
```

Then open the local Streamlit URL shown in the terminal.

Example queries:

```text
routing protocols
```

```text
network loops
```

```text
Python programming
```

---

## 📊 Example

For a query such as:

```text
network protocol
```

the system generates an embedding for the query and compares it with the embeddings of all documents.

Example output:

```text
1. OSPF is a link-state routing protocol...
   Similarity Score: 0.5319

2. BGP is a path vector routing protocol...
   Similarity Score: 0.4209

3. VLANs allow a network to be logically divided...
   Similarity Score: 0.2599
```

Higher cosine similarity indicates greater semantic similarity between the query and the document.

---

## 🔬 How It Works

### 1. Document Embedding

Each document is converted into a numerical vector:

```text
Text
 ↓
Sentence Transformer
 ↓
Embedding Vector
```

For example, with `all-MiniLM-L6-v2`, each sentence is represented as a **384-dimensional vector**.

### 2. Query Embedding

The user's query is converted using the same embedding model.

### 3. Similarity Calculation

The query vector is compared with all document vectors using cosine similarity.

Conceptually:

```text
                    Query Vector
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       Vector 1       Vector 2       Vector 3
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                Cosine Similarity
                         ↓
                    Top-K Results
```

---




## 🧪 Learning Outcomes Covered

This project currently covers the core concepts of:

* Text embeddings
* Semantic similarity
* Cosine similarity
* Top-K retrieval
* Semantic search
* Embedding model selection
* Modular NLP application design

Future iterations will extend the project toward vector databases, metadata filtering, multilingual retrieval, and practical NLP tasks.

---

## 🛠️ Technologies

* **Python 3.11**
* **Sentence Transformers**
* **PyTorch (CPU)**
* **scikit-learn**
* **Pandas**
* **Pydantic Settings**
* **Streamlit**
* **Conda**
* **WSL**

---


