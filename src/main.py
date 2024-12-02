from textnode import *
from htmlnode import *

print("hello world")

def main():
    test = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank"})
    print(test)

main()