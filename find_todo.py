import os
import json

found_any = False

print("Scanning for TODOs...")
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ipynb"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    notebook = json.load(f)
                    
                cells = notebook.get("cells", [])
                for i, cell in enumerate(cells):
                    source = cell.get("source", [])
                    if isinstance(source, str):
                        source = source.splitlines()
                        
                    for line_idx, line in enumerate(source):
                        code_line = line.strip()
                        lower_line = code_line.lower()
                        
                        # Logic to capture various TODO formats
                        if "todo" in lower_line:
                            # 1. Look for "# TODO" or "#TODO"
                            if "#todo" in lower_line.replace(" ", ""):
                                print(f"MATCH: {path} (Cell {i}): {code_line}")
                                found_any = True
                            # 2. Look for "TODO:"
                            elif "todo:" in lower_line:
                                print(f"MATCH: {path} (Cell {i}): {code_line}")
                                found_any = True
                            # 3. Look for "TODO" + "morsa"/"walrus"
                            elif ("morsa" in lower_line or "walrus" in lower_line):
                                print(f"MATCH: {path} (Cell {i}): {code_line}")
                                found_any = True

            except Exception as e:
                print(f"Error reading {path}: {e}")

if not found_any:
    print("Zero matches found.")
