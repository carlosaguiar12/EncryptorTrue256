# coding: utf-8

import stdiomask
from Crypto.Protocol.KDF import PBKDF2 as KDF2
from time import sleep
from encrypt_data import encrypt_data


def create_password(salt):
	"""Cria uma nova senha de acesso para o ET256."""

	__PASSWORD_FILE = "DATA_GHOST.txt"

	print("\n==== ET256  [ @humanodev ]  ====")
	while True:
		"""Criação e validação de uma nova senha para acesso."""

		print("\n[ + ]  Criando senha para acesso.")
		print("[ ! ]  NÃO PERCA OU COMPARTILHE A SUA SENHA.")

		__password = stdiomask.getpass(prompt="\n=> Insira uma nova senha: ")
		__confirm_password = stdiomask.getpass(prompt="=> Confirme a senha: ")

		if __password == __confirm_password:
			print("\nExecute novamente o script para começar a usar...\nBoa sorte!\n")
			break
		else:
			print("\n[ ERRO ]  AS SENHAS DIGITADAS SÃO DIFERENTES!")
			print("Tente novamente..")

	# Escreve a senha de acesso no arquivo
	with open(__PASSWORD_FILE, "w") as fo:
		fo.write(__password)

	# Combina senha + salt e cria a chave
	__KEY = KDF2(__password, salt, dkLen=32)

	# Encripta o arquivo com a senha de acesso
	encrypt_data(__PASSWORD_FILE, __KEY)

	sleep(4)
