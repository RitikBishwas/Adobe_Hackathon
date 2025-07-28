# 🧠 Adobe Hackathon 2025 – Round 1B Submission

## 📘 Project: Persona-Driven Document Intelligence

### 📌 Objective
This module is designed to extract the **most relevant textual content** from large academic PDF documents based on a **user-defined persona and job description**. It enables persona-aware summarization for intelligent document navigation.

---

### 💡 How It Works

1. Accepts input PDF documents along with a textual *persona* and *job role*.
2. Extracts raw text using PyMuPDF.
3. Uses a Sentence-BERT-based semantic similarity model to score content relevance.
4. Returns top-ranked sections tailored to the persona-job context.

---

### 📁 Directory Structure

Round_1B/
├── input/
│ ├── sample_resume.pdf
│ ├── persona.txt
│ └── job_description.txt
│
├── output/
│ └── results.json
│
├── persona_extractor.py
├── model/ (auto-downloaded on first run)
├── README.md
└── requirements.txt




---

## 🛠️ Requirements

- Python 3.11+
- torch
- sentence-transformers
- PyMuPDF

Install all dependencies with:

```bash
pip install -r requirements.txt


🚀 Run Instructions
python persona_extractor.py

✅ Make sure the input/ folder contains:
A PDF file
persona.txt
job_description.txt

The output will be generated in the output/results.json file.

✅ Output Example

{
  "matched_sections": [
    {
      "score": 0.87,
      "page": 2,
      "text": "Extensive hands-on experience with Operating Systems including Linux internals, scheduling algorithms..."
    },
    {
      "score": 0.84,
      "page": 5,
      "text": "Led backend engineering team in deploying scalable microservices used in cloud environments..."
    }
  ]
}


📌 Features
🔍 Contextual matching between persona and document

🧠 Semantic relevance scoring using Sentence-BERT

📄 Supports multi-page PDF inputs

✅ Output easily consumable for downstream applications (search, summarization, etc.)


👨‍💻 Developed By
Sanjana and Ritik
B.Tech CSE, NIT Delhi

Status
✅ Persona-based matching working end-to-end

✅ HuggingFace model auto-downloaded

✅ Works on any academic/job-related PDF

✅ Submission-ready