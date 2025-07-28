FROM --platform=linux/amd64 python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install PyMuPDF pdfplumber

ENTRYPOINT ["sh", "-c", "for file in input/*.pdf; do python extractor.py \"$file\" \"output/$(basename \"${file%.*}\").json\"; done"]
