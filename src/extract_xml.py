from pathlib import Path
def convert_to_zip(path_docx) -> Path:
    new_xml = path_docx.with_suffix(".zip")
    path_docx.rename(new_xml)

def extract_xml(path_zip):
    base_folder = path_zip.parent
    for p in base_folder.glob("**/document.xml"):
        return p
