# coding: utf-8


import os

EXCEPTION_FILES = ("create_password.py", "decrypt_all_files.py",
                   "decrypt_data.py", "encrypt_all_files.py",
                   "encrypt_data.py", "get_all_files.py",
                   "insert_user_roots.py", "login.py", "main.py",
                   "options_menu.py", "verify_password.py",
                   "EncryptorTrue256.exe", "ET256.exe")


def get_all_files(root):
    """Encontra os caminhos absolutos de cada arquivo da raiz."""

    dirs = []
    for item in root:
        for p, _, files in os.walk(os.path.abspath(item)):
            for file in files:
                if file not in EXCEPTION_FILES:
                    dirs.append(os.path.join(p, file))

    return dirs
