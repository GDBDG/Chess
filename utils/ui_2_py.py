"""
Translate all ui files to python files
"""
from os import path, listdir, system
from pathlib import Path

PROJECT_DIR = next(p for p in Path(__file__).parents if p.name == "Chess")
UI_FILES_DIR = PROJECT_DIR / "src/ui"
IHM_PATH = PROJECT_DIR / "src" / "ihm"


def list_ui_file() -> [str]:
    """
    List all ui files in the directory
    @return: None
    """
    files = listdir(UI_FILES_DIR)
    return [UI_FILES_DIR / filename for filename in files if path.splitext(filename)[1] == ".ui"]


def trans_py_file(filename: Path):
    """
    Convert the file with the extension .ui into a file with the extension .py
    @param filename: name of the ui file to translate to python file
    @return:
    """
    return IHM_PATH / f"{filename.stem}.py"


# Call the system command to change the UI file to a Python file with the extension
def ui_2_py():
    """
    Translate all ui files to python files
    @return: None
    """
    ui_file_list = list_ui_file()
    for ui_file in ui_file_list:
        pyfile = trans_py_file(ui_file)
        print(ui_file, pyfile)
        system("ls")
        cmd = f"pyside6-uic {ui_file} -o {pyfile}"
        system(cmd)


# Entry of the program
if __name__ == '__main__':
    ui_2_py()
