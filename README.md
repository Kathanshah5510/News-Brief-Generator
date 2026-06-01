# 📰 News Brief Generator

A Generative AI project that automatically creates multiple styles of summaries from long-form text such as news articles, blogs, and reports using Groq's Llama 3.1 model.

---

## Features

This application generates three different types of summaries:

### 📌 Bullet-Point Summary
Extracts the key information into concise bullet points.

### 📄 Abstract Summary
Generates a formal abstract-style summary similar to research papers.

### 👦 Simple English Summary
Creates an easy-to-understand summary suitable for a 12-year-old reader.

---

## Technologies Used

- Python
- Groq API
- Llama 3.1 8B Instant
- Prompt Engineering

---

## Project Structure

```text
News-Brief-Generator/
│
├── news_brief_generator.py
├── article.txt
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Kathanshah5510/News-Brief-Generator.git
```

Move into the project folder:

```bash
cd News-Brief-Generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run:

```bash
python news_brief_generator.py
```

You will be prompted to enter your Groq API key:

```text
Enter your Groq API key:
```

After entering the API key, the application generates:

- Bullet-point Summary
- Abstract Summary
- Simple English Summary

---

## Example Use Cases

- News Summarization
- Blog Summarization
- Research Paper Overview
- Educational Content Simplification
- Content Digest Generation

---

## Model Configuration

| Parameter | Value |
|------------|------------|
| Model | llama-3.1-8b-instant |
| Temperature | 0.3 |
| Max Completion Tokens | 300 |

---

## Learning Outcomes

This project demonstrates:

- API Integration
- Large Language Models (LLMs)
- Prompt Engineering
- Text Summarization
- Python Development

---

## Author

**Kathan Shah**

M.Tech ICT (Machine Learning)
Dhirubhai Ambani University (Formerly DA-IICT)
Gandhinagar, Gujarat, India
