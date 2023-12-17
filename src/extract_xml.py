from pathlib import Path
def convert_to_zip(txt) -> Path:
    new_xml = txt.with_suffix(".zip")
    txt.rename(new_xml)

def extract_xml(txt):
    base_folder = txt.parent
    for p in base_folder.glob("**/document.xml"):
        return p

