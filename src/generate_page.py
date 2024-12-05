from block_markdown import *
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return f'{line.lstrip("# ")}'
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file = (open(from_path)).read()
    with open(from_path, "r") as from_file:
        file_content = from_file.read()
        
    with open(template_path, "r") as template_file:
        template_content = template_file.read()
    node = markdown_to_html_node(file_content)
    html = node.to_html()
    title = extract_title(file_content)
    final_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html)
    os.makedirs(os.path.dirname(dest_path), exist_ok = True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(file_content)
        

