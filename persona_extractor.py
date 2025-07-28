import fitz
import os
import json
from sentence_transformers import SentenceTransformer, util
from datetime import datetime

# Load small CPU-compatible transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def extract_sections(text):
    return [section.strip() for section in text.split("\n\n") if len(section.strip()) > 30]

def process_documents(input_dir, persona, job):
    query = f"{persona}: {job}"
    query_embedding = model.encode(query)
    
    ranked_sections = []

    for filename in os.listdir(input_dir):
        if not filename.endswith(".pdf"):
            continue
        full_path = os.path.join(input_dir, filename)
        text = extract_text_from_pdf(full_path)
        sections = extract_sections(text)

        for section in sections:
            score = util.cos_sim(model.encode(section), query_embedding).item()
            ranked_sections.append((score, filename, section))

    ranked_sections.sort(reverse=True)

    top_sections = ranked_sections[:10]
    output = {
        "metadata": {
            "documents": [filename for filename in os.listdir(input_dir) if filename.endswith(".pdf")],
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": []
    }

    for i, (score, doc, section) in enumerate(top_sections, 1):
        output["extracted_sections"].append({
            "document": doc,
            "importance_rank": i,
            "refined_text": section
        })

    return output

if __name__ == "__main__":
    persona = "Investment Analyst"
    job = "Analyze revenue trends, R&D investments, and market positioning strategies"

    input_dir = "input"
    output_file = "output/persona_output.json"

    result = process_documents(input_dir, persona, job)

    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)
