from pathlib import Path
import re
def extract_target_row(file_path):
    with open(file_path) as f:
        contents_list = f.readlines()
        target_row = contents_list[1]
        print("target_row: " + target_row)
        return target_row

def split_into_tag_and_content(target_row):
    target_list = re.split(">|<", target_row)
    print("result: " + target_list)
    return target_list

def get_tagged_contents(target_list):
    tag_open = False
    for item in target_list:
        if item == "w:t":
            tag_open = True
        elif item == "/w:t":
            tag_open = False
        elif tag_open:
            yield item
