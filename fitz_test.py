import fitz

print(f"✅ Using fitz from: {fitz.__file__}")
doc = fitz.open("input/DBMS_Full_Notes.pdf") 
print(f"✅ PDF opened successfully with {doc.page_count} page(s)")
