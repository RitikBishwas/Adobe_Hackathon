import fitz
import json
import re
import sys
import os  # ADD THIS AT THE TOP if not already

def extract_outline(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get("title", "Untitled Document")
    outline = []
    heading_patterns = {
        "H1": re.compile(r"^\d+\s.+"),
        "H2": re.compile(r"^\d+\.\d+\s.+"),
        "H3": re.compile(r"^\d+\.\d+\.\d+\s.+")
    }

    for page_num, page in enumerate(doc, start=1):
        for block in page.get_text("blocks"):
            for line in block[4].split("\n"):
                for level, pattern in heading_patterns.items():
                    if pattern.match(line.strip()):
                        outline.append({
                            "level": level,
                            "text": line.strip(),
                            "page": page_num
                        })

    with open(output_path, "w") as f:
        json.dump({"title": title, "outline": outline}, f, indent=2)

if __name__ == "__main__":
    input_dir = "input"
    output_dir = "output"

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            input_pdf = os.path.join(input_dir, filename)
            output_json = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.json")
            extract_outline(input_pdf, output_json)
            print(f"✅ Extracted outline from {filename} → {os.path.basename(output_json)}")
