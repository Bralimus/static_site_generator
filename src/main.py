from textnode import *
from htmlnode import *
from copy_contents import *
from generate_page import *

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static files to public directory")
    copy_contents(dir_path_static, dir_path_public)
    generate_pages_recursive("./content", "template.html", "./public")
main()