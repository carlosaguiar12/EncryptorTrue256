# coding: utf-8

import os
import sys
from encrypt_data import encrypt_data
from decrypt_data import decrypt_data
from encrypt_all_files import encrypt_all_files
from decrypt_all_files import decrypt_all_files


def options_menu(key):
    """..."""

    while True:
        print("""
	>>  Digite 1 para Encriptar UM arquivo
	>>  Digite 2 para Decriptar UM arquivo
	>>  Digite 3 para Encriptar VÁRIOS arquivos
	>>  Digite 4 para Decriptar VÁRIOS arquivos
	>>  Digite 99 para Sair
		""")

        try:
            __choice = str(input("Sua escolha: "))
        except (KeyboardInterrupt, EOFError, Exception):
            print("\n[ ? ]  Entrada Inválida..\n")
        else:
            if __choice in ("1", "2", "3", "4", "99"):
                if __choice == "1":
                    try:
                        __file_name = str(input("Nome ou caminho do arquivo para encriptar: "))
                    except (KeyboardInterrupt, EOFError, Exception):
                        print("\n[ ? ]  Entrada Inválida..\n")
                    else:
                        encrypt_data(__file_name, key)

                elif __choice == "2":
                    try:
                        __file_name = str(input("Nome ou caminho do arquivo para decriptar: "))
                    except (KeyboardInterrupt, EOFError, Exception):
                        print("\n[ ? ]  Entrada Inválida..\n")
                    else:
                        decrypt_data(__file_name, key)

                elif __choice == "3":
                    print("\n[ Dica ]  Se os arquivos estão na pasta abaixo..\n"
                          f"          => {os.getcwd()}\n"
                          f"          Basta pressionar [ENTER] para adicionar Todos.\n")
                    encrypt_all_files(key)

                elif __choice == "4":
                    print("\n[ Dica ]  Se os arquivos estão na pasta abaixo..\n"
                          f"          => {os.getcwd()}\n"
                          f"          Basta pressionar [ENTER] para adicionar Todos.\n")
                    decrypt_all_files(key)

                elif __choice == "99":
                    # Windows
                    os.system(f"Taskkill /PID {os.getppid()} /F")
                    sys.exit(0)

            else:
                print("Opção inválida! Apenas 1, 2, 3, 4 ou 99.")
