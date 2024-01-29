from pathlib import Path
from zipfile import ZipFile
from pathlib import Path
from zipfile import ZipFile
from tempfile import mkdtemp

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



    return xml_file_path, temp_dir
