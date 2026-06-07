def check_css_imports(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    print("CSS imports in index.html:")
    for idx, line in enumerate(lines):
        line_strip = line.strip()
        if 'rel="stylesheet"' in line_strip or '<style' in line_strip:
            print(f"Line {idx+1:4d}: {line_strip[:200]}")

if __name__ == "__main__":
    check_css_imports("index.html")
