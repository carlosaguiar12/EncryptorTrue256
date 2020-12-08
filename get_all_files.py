# coding: utf-8


import os

EXCEPTION_FILES = ("decrypt_data.py", "encrypt_data.py",
                   "main.py", "get_all_files.py", "ET256.exe",
                   "EncryptorTrue256.exe")


def get_all_files(root):
    """Encontra os caminhos absolutos de cada arquivo da raiz."""

    dirs = []
    for item in root:
        for p, _, files in os.walk(os.path.abspath(item)):
            for file in files:
                if file not in EXCEPTION_FILES:
                    dirs.append(os.path.join(p, file))

    return dirs
