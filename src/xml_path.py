from pathlib import Path
import re
def extract_target_row(file_path):
    with open(file_path) as f:
        contents_list = f.read()
        target_row = contents_list[1]
        return target_row

def split_into_tag_and_content(target_row):
    target_list = re.split(">|<", target_row)
    return target_list

def get_bracket_contents(target_list):
    depth = 0
    f = 0
    for i, c in enumerate(target_list):
        if c == "w:t":
            depth += 1
            if depth == 1:
                f = i + 1
        




# from pathlib import Path
# import re

# def extract_contents(file_path):
#     pattern = re.compile(r"<w:t>(.*?)</w:t>")
#     contents_list = []

#     with open(file_path, mode="r", encoding="utf-8") as f:
#         text = f.read()
#         contents_list = [match.group(1) for match in pattern.finditer(text)]

#     return contents_list
