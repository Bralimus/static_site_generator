import re

from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:       
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif node.text_type == TextType.TEXT:
            list = node.text.split(delimiter)
            if len(list) % 2 == 0:
                raise ValueError("Invalid markdown, formatted section not closed")
            for i, text in enumerate(list):
                if text:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(text, TextType.TEXT))
                    if i % 2 == 1:
                        new_nodes.append(TextNode(text, text_type))
        else:
            raise Exception("Does not match any known text type.")
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        updating_text = node.text
        if extract_markdown_images(node.text):
            images = extract_markdown_images(node.text)
            for image in images:
                image_alt, image_link = image
                sections = updating_text.split(f"![{image_alt}]({image_link})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, image section not closed")
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                updating_text = sections[1]
        if len(updating_text) > 0:
            new_nodes.append(TextNode(updating_text, TextType.TEXT))   
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        updating_text = node.text
        if extract_markdown_links(node.text):
            links = extract_markdown_links(node.text)
            for link in links:
                link_text, link_url = link
                sections = updating_text.split(f"[{link_text}]({link_url})", 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                updating_text = sections[1]
        if len(updating_text) > 0:
            new_nodes.append(TextNode(updating_text, TextType.TEXT))   
    return new_nodes

def text_to_textnodes(text):
   nodes = [TextNode(text, TextType.TEXT)]
   nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
   nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
   nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
   nodes = split_nodes_image(nodes)
   nodes = split_nodes_link(nodes)   
   return nodes