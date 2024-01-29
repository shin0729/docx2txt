from pathlib import Path
import re
import extract_xml
# document.xmlは二行目にすべての情報がminifyされて記述されているのでそれを抽出する
def extract_target_row(file_path):
    with open(file_path, encoding="utf-8") as f:
        contents_list = f.readlines()
        target_row = contents_list[1]
        return target_row


def split_into_tag_and_content(target_row):
    target_list = re.split(">|<", target_row)
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


def main():
    path__str_list = list(map(str, input("ファイルパスを入力して下さい，複数の場合はコンマで区切って下さい: ").split(",")))
    path_list = [Path(p) for p in path__str_list]
    for path in path_list:
        path_docx = path
        path_zip = extract_xml.convert_to_zip(path_docx)
        file_path = extract_xml.extract_xml(path_zip)
        target_row = extract_target_row(file_path)
        target_list = split_into_tag_and_content(target_row)
        tagged_contents = get_tagged_contents(target_list)
        for content in get_tagged_contents(target_list):
            print(content)
            print("\n")


if __name__ == "__main__":
    main()
