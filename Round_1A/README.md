# 🔍 Adobe Hackathon 2025 – Round 1A Submission
## 📘 Project: Academic PDF Outline Extraction

### 📌 Objective
The aim of this module is to extract structured hierarchical outlines (H1, H2, H3) from academic PDF documents. This aids in indexing, summarization, and persona-driven search features.

---

### 📁 Directory Structure

Round_1A/
├── input/
│ ├── DBMS_Full_Notes.pdf
│ ├── DBMS_gfg.pdf
│ └── OS_Full_Notes.pdf
│
├── output/
│ ├── DBMS_Full_Notes.json
│ ├── DBMS_gfg.json
│ └── OS_Full_Notes.json
│
├── extractor.py
├── Dockerfile
├── README.md
└── requirements.txt



---

## 🛠️ Requirements

- Python 3.11+
- PyMuPDF
- pdfplumber (optional fallback for extraction)

Install with:

```bash
pip install -r requirements.txt


🚀 Run Instructions
🐳 Using Docker (Preferred)
# Inside Round_1A directory
docker build --no-cache --platform linux/amd64 -t outline-extractor .

docker run --rm \
  -v ${PWD}/input:/app/input \
  -v ${PWD}/output:/app/output \
  --network none \
  outline-extractor


🐍 Run Locally (Without Docker)
python extractor.py
Make sure input/ folder contains the PDF files and output/ folder is present before running.


✅ Output Example

{
  "title": "OS Full Notes",
  "outline": [
    {
      "level": "H1",
      "text": "1 Introduction",
      "page": 1
    },
    {
      "level": "H2",
      "text": "1.1 Types of OS",
      "page": 2
    },
    {
      "level": "H3",
      "text": "1.1.1 Real-time Systems",
      "page": 3
    }
  ]
}
👨‍💻 Developed By
Sanjana and Ritik 
B.Tech CSE, NIT Delhi

📌 Status
 Dockerized Extraction Pipeline

 Successfully tested on 3 PDFs

 Submission-ready