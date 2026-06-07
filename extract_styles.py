def extract_styles(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    import re
    style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    if style_match:
        style_content = style_match.group(1)
        lines = style_content.splitlines()
        print(f"Total lines in style tag: {len(lines)}")
        print("First 150 lines of style tag:")
        for idx in range(min(150, len(lines))):
            print(f"{idx+1:3d}: {lines[idx]}")
    else:
        print("No style tag found!")

if __name__ == "__main__":
    extract_styles("index.html")
