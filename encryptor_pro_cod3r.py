# coding: utf-8

__author__ = '@pro.cod3r'  # Instagram

import os
import stdiomask

from time import sleep
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2 as KDF2
from Crypto.Random import get_random_bytes


class Encryptor():
    """Encripta e decripta arquivos."""

    def __init__(self, key):
        self.key = key
        self.list_roots = []
        self.list_errors = []

    def encrypt_files(self, file_name):

        # verificando se o arquivo recebido por file_name existe
        if os.path.isfile(file_name):
            # verificando se o arquivo já não está encriptado
            if not file_name.endswith('.enc'):
                # lendo o arquivo como sequência binária
                with open(file_name, 'rb') as file_object:
                    plaintext = file_object.read()  # conteúdo do arquivo

                # verificando possíveis erros ao encriptar [ValueError]
                try:
                    # criando um objeto cifra com a chave no MODE_CBC
                    cipher = AES.new(self.key, AES.MODE_CBC)  # inicialização da criptografia

                    # === criptografando os dados === #
                    data_ciphered = cipher.encrypt(pad(plaintext, AES.block_size))

                    # adicionando a extensão '.enc' no arquivo
                    with open(file_name + '.enc', 'wb') as file_object:
                        # escrevendo o vetor de inicialização e os dados encriptados no arquivo
                        file_object.write(cipher.iv)
                        file_object.write(data_ciphered)
                    # deletando o arquivo original
                    os.remove(file_name)
                # caso ocorra um error de valor e não seja possível encriptar
                except ValueError:
                    # adicionando os arquivos que não puderam ser encriptados
                    self.list_errors.append('[ ERRO AO ENCRIPTAR ]' + ' >>> ' + file_name)
                else:
                    # se nenhum erro ocorrer, irá imprimir [ ok ] + file_name,
                    # exceto na verificação de senha com o arquivo 'data_enc.txt'
                    if file_name != 'data_enc.txt':
                        print(f'[ OK ]  {file_name}')

        else:
            print('\n[ ERRO ]  O arquivo não existe. Tente com outro nome..')

    def decrypt_files(self, file_name):

        # verificando se o arquivo recebido por file_name existe
        if os.path.isfile(file_name):
            # verificando se o file_name está encriptado para seguir com a decriptação
            if file_name.endswith('.enc'):
                # lendo o arquivo como sequência binária
                with open(file_name, 'rb') as file_object:
                    # vetor de inicialização com os 16 bytes necessários
                    iv = file_object.read(16)
                    # leitura do resto dos dados
                    data_ciphered = file_object.read()

                # verificando possíveis erros ao decriptar [ValueError]
                try:
                    # criando um objeto cifra com a chave no MODE_CBC
                    cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)  # inicialização da criptografia
                    # dados restaurados prontos para a saída
                    data_restore = unpad(cipher.decrypt(data_ciphered), AES.block_size)

                    # reescrevendo o arquivo sem a extensão '.enc'
                    with open(file_name[:-4], 'wb') as file_object:
                        file_object.write(data_restore)
                    # deletando o arquivo original
                    os.remove(file_name)
                # tratando o erro de Valor
                except ValueError:
                    # caso o ValueError seja com o arquivo que contém a senha [data_enc.txt.enc],
                    # quer dizer que a senha inserida está incorreta, então o script deve fechar
                    if file_name == 'data_enc.txt.enc':
                        print('\n[ ERRO ]  Acesso negado.')
                        exit()
                    # adicionado os arquivos que não puderam ser decriptados
                    self.list_errors.append('[ ERRO AO DECRIPTAR ]' + ' >>> ' + file_name)
                else:
                    # se nenhum erro ocorrer, irá imprimir [ ok ] + file_name,
                    # exceto na verificação de senha com o arquivo 'data_enc.txt.enc'
                    if file_name != 'data_enc.txt.enc':
                        print(f'[ OK ]  {file_name}')

        else:
            print('\n[ ERRO ]  O arquivo não existe. Tente com outro nome..')

    def get_all_files(self, *args):
        """Busca todos os caminhos dos arquivos de uma ou mais raízes."""

        dirs = []
        for item in args:
            for p, _, files in os.walk(os.path.abspath(item)):
                for file in files:
                    if file != 'encryptor_pro_cod3r.py' and file != 'data_enc.txt.enc':
                        dirs.append(os.path.join(p, file))
        return dirs

    def insert_roots(self, index_option):

        # limpa a lista antes de receber novos itens
        self.list_roots.clear()
        # duas opções para dois métodos diferentes => encrypt_all_files() e decrypt_all_files()
        option = ['criptografado', 'descriptografado']

        # leitura e adição de raízes em uma lista para encriptar ou decriptar
        while True:
            roots = str(input(f'Insira o diretório raiz a ser {option[index_option]}: '))
            self.list_roots.append(roots)
            while True:
                answer = str(input('Deseja inserir mais diretórios? [S/N]: ')).upper().strip()[0]
                if answer in 'SN':
                    break
                else:
                    print('\nOpção inválida. Apenas [S/N].\n')
            if answer == 'N':
                break

    def encrypt_all_files(self):

        # index_option=0 >>> "criptografado"
        self.insert_roots(index_option=0)
        print('\n => CRIPTOGRAFANDO ARQUIVOS\n')

        # percorrendo a lista de raízes recebidas por insert_roots()
        for root in self.list_roots:
            # passando cada uma das raízes para get_all_files()
            # e armazenando o retorno com todos os arquivos, caso existam
            roots_return = self.get_all_files(root)

            # verificando se em alguma das raízes não foi encontrado nenhum arquivo
            if len(roots_return) == 0:
                print(f'[ ERRO ]  Nenhum arquivo encontrado no diretório "{root}".\n')
            # caso tenha encontrado algum arquivo na raiz inserida
            else:
                # percorrendo cada caminho absoluto da raiz
                for item in roots_return:
                    # criptografando cada um dos arquivos
                    self.encrypt_files(item)
                print()

    def decrypt_all_files(self):

        # index_option=1 >>> "descriptografado"
        self.insert_roots(index_option=1)
        print('\n => DESCRIPTOGRAFANDO ARQUIVOS\n')

        # percorrendo a lista de raízes recebidas por insert_roots()
        for root in self.list_roots:
            # passando cada uma das raízes para get_all_files()
            # e armazenando o retorno com todos os arquivos, caso existam
            roots_return = self.get_all_files(root)

            # verificando se em alguma das raízes não foi encontrado nenhum arquivo
            if len(roots_return) == 0:
                print(f'[ ERRO ]  Nenhum arquivo encontrado no diretório "{root}".\n')
            # caso tenha encontrado algum arquivo na raiz inserida
            else:
                # percorrendo cada caminho absoluto da raiz
                for item in roots_return:
                    # descriptografando cada um dos arquivos
                    self.decrypt_files(item)
                print()

# ==== gerando dado aleatório (salt) ==== #
# salt = get_random_bytes(32)  # 32 bytes => 256 bits
# executar somente a linha acima, copiar o dado do terminal e salvar em uma variável, como feito abaixo

# dado aleatório de tamanho 256 bits
salt = b'\xfa\x01\x86\x8c\x84\xcdE\xac\x0e\xc4\xdeO\xfc\x14\xd3\xc7^\x7f\xab\x96\xear\x0c\xb8\x1e\xe8</\xf9\xa3\xcc\xff'

# arquivo usado para guardar a senha de acesso
file_txt = 'data_enc.txt'

# verificando se o arquivo que guarda a senha de acesso não existe
# se não existir, será criado o arquivo e uma nova senha para acesso
if not (os.path.isfile(file_txt) or os.path.isfile(file_txt + '.enc')):

    print('\n==== Criptografia / Descriptogafia ====')
    while True:
        """Criação e validação de uma nova senha para acesso."""

        # password = str(input('\n=> Insira uma nova senha: '))
        # confirm_password = str(input('=> Confirme a senha: '))

        password = stdiomask.getpass(prompt='\n=> Insira uma nova senha: ')
        confirm_password = stdiomask.getpass(prompt='=> Confirme a senha: ')

        if password == confirm_password:
            print('\nReinicie o script para começar a usar.\nBoa sorte!\n')
            break
        else:
            print('\n[ ERRO ]  AS SENHAS DIGITADAS SÃO DIFERENTES!')
            print('Tente novamente..')

    # escrevendo a senha de acesso no arquivo 'data_enc.txt
    with open(file_txt, 'w') as file_object:
        file_object.write(password)

    # combinando senha + salt e criando a chave
    key = KDF2(password, salt, dkLen=32)
    # Instanciando a classe e passando a chave para 'self.key'
    crypt = Encryptor(key)
    # criptografando o arquivo 'data_enc.txt' com a senha de acesso
    crypt.encrypt_files(file_txt)

    sleep(4)

# neste ponto o arquivo com a senha de acesso já existe
else:
    # lendo a senha de acesso
    password = stdiomask.getpass(prompt='\nSenha: ')
    # combinando novamente senha + salt
    # (caso a senha seja incorreta, uma exceção ValueError será levantada)
    key = KDF2(password, salt, dkLen=32)
    # Instaciando a classe e passando a chave
    crypt = Encryptor(key)

    # ===== verificando a senha inserida ===== #

    # caso a senha inserida esteja correta,
    # o arquivo de dados será descriptografado (por pouco tempo)
    crypt.decrypt_files(file_txt + '.enc')

    # caso a senha esteja incorreta, a decriptação do arquivo de dados não funcionará
    # uma exceção ValueError será levantada e o script irá fechar

    # caso a senha esteja correta, a decriptação anterior funcionou,
    # então é o momento de encriptar os dados novamente e seguir com o acesso ao script
    crypt.encrypt_files(file_txt)

    # menu de opções
    while True:
        print("""
    > 1. Digite 1 para criptografar um arquivo
    > 2. Digite 2 para descriptografar um arquivo
    > 3. Digite 3 para criptografar TODOS os arquivos
    > 4. Digite 4 para descriptografar TODOS os arquivos
    > 5. Digite 5 para sair do script
        """)

        choice = str(input('Sua escolha: '))
        if choice in ('1', '2', '3', '4', '5'):
            if choice == '1':
                file_name = str(input('Nome ou caminho do arquivo para encriptar: '))
                crypt.encrypt_files(file_name)
            elif choice == '2':
                file_name = str(input('Nome ou caminho do arquivo para decriptar: '))
                crypt.decrypt_files(file_name)
            elif choice == '3':
                crypt.encrypt_all_files()
            elif choice == '4':
                crypt.decrypt_all_files()
            elif choice == '5':
                exit()

            # verificando se existe algum erro na lista de erros
            if len(crypt.list_errors) > 0:
                print('\n => Um ou mais arquivos não puderam ser processados.\n')
                # percorrendo a lista de erros e imprimindo-os na tela
                for error in crypt.list_errors:
                    print(error)
                print()
                # limpando a lista no final do processo para não haver redundâncias
                crypt.list_errors.clear()
        else:
            print('Opção inválida! Apenas 1, 2, 3, 4 ou 5.')
