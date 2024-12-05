import os
import shutil

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