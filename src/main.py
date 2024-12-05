from textnode import *
from htmlnode import *
import os
import shutil

def overwrite_contents(source, destination):
    delete_contents(destination)
    copy_contents(source, destination)


def delete_contents(directory):
    contents = os.listdir(directory)
    for content in contents:
        path = os.path.join(directory, content)
        if os.path.isdir(path):
            shutil.rmtree(path)
        if os.path.isfile(path):
            os.remove(path)


def copy_contents(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    to_copy = os.listdir(source)
    for content in to_copy:
        source_path = os.path.join(source, content)
        destination_path = os.path.join(destination, content)
        if os.path.isdir(source_path):
            copy_contents(source_path, destination_path)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path) 

def main():
    overwrite_contents("static", "public")

main()