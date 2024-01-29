from pathlib import Path
from zipfile import ZipFile
from tempfile import mkdtemp
import shutil

def extract_xml(path_docx) -> Path:
    # 一時的なディレクトリを作成
    temp_dir = Path(mkdtemp())
    xml_file_path = None

    # docxファイルをzipとして開く
    with ZipFile(path_docx, 'r') as zip_ref:
        # ZIP内のすべてのファイルを一時ディレクトリに解凍
        zip_ref.extractall(temp_dir)
        # document.xmlを探す
        xml_file = temp_dir / 'word' / 'document.xml'
        if xml_file.exists():
            xml_file_path = xml_file

    # 一時ディレクトリを削除
    shutil.rmtree(temp_dir)

    return xml_file_path

# 使用例
path_docx = Path("path/to/your/docxfile.docx")
document_xml = extract_xml(path_docx)
if document_xml:
    print(f"Found document.xml at: {document_xml}")
else:
    print("document.xml not found in the docx file.")