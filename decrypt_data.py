# coding: utf-8

import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from time import sleep


def decrypt_data(file_name, key):
    """Decripta os dados do arquivo."""

    # Verifica se o arquivo existe e se já está encriptado
    if os.path.isfile(file_name):
        if file_name.endswith(".enc"):

            # Leitura da sequência binária
            with open(file_name, "rb") as fo:
                # Inicialização do vetor de inicialização com
                # os 16 bytes necessários
                iv = fo.read(16)

                # Leitura do resto dos dados
                data_ciphered = fo.read()

            # Verifica erros de valor ao decriptar
            try:
                # Inicializa um objeto cifra com a chave
                cipher = AES.new(key, AES.MODE_CBC, iv=iv)

                # Dados restaurados
                data_restore = unpad(cipher.decrypt(data_ciphered), AES.block_size)

                # Reescrevendo os dados restaurados no arquivo
                with open(file_name[:-4], "wb") as fo:
                    fo.write(data_restore)

                # Deletando o arquivo original
                os.remove(file_name)

            except ValueError:
                # Se o erro de valor ocorrer no arquivo que guarda a senha,
                # quer dizer que a senha está incorreta, então o script deve fechar.

                if file_name == "DATA_GHOST.txt.enc":
                    print("\n[ ERRO ]  Acesso negado.")
                    sleep(2)

                    # Matando o processo no Windows
                    os.system(f"Taskkill /PID {os.getppid()} /F")
                    sys.exit(0)

                else:
                    # Escrever arquivo de erros
                    pass

            else:
                # Mostra que a decriptação ocorreu com sucesso
                if file_name != "DATA_GHOST.txt.enc":
                    print(f"[ OK ]  {file_name}")
        else:
            print(f"\n[ ? ]  É necessário que o arquivo esteja encriptado\n"
                  "       para seguir com a decriptação.\n"
                  "\n=> Arquivo conflitante: {file_name}\n")

    else:
        print(f"[ ERRO ]  O arquivo '{file_name}' não existe. Tente com outro nome.")
