from block_markdown import *
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return f'{line.lstrip("# ")}'
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

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
        dest_file.write(final_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
       os.makedirs(dest_dir_path)
    dir_content = os.listdir(dir_path_content)
    for content in dir_content:
        source_path = os.path.join(dir_path_content, content)
        destination_path = os.path.join(dest_dir_path, content)
        if os.path.isdir(source_path):
            generate_pages_recursive(source_path, template_path, destination_path)
        if os.path.isfile(source_path):
            if source_path.endswith(".md"):
                destination_path = destination_path[:-3] + '.html'
            generate_page(source_path, template_path, destination_path)
        

