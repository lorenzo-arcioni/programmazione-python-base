import nbformat
import sys

if len(sys.argv) < 2:
    print("Utilizzo: python script.py <nomefile.ipynb>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

for cell in notebook.cells:
    if cell.cell_type == "markdown":
        print(cell.source)
        print("\n" + "-"*80 + "\n")  # Separatore opzionale

with open("solo_markdown.md", "w", encoding="utf-8") as out:
    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            out.write(cell.source + "\n\n")
    out.close()