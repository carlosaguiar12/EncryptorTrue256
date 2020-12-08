# coding: utf-8

import stdiomask
from Crypto.Protocol.KDF import PBKDF2 as KDF2
from encrypt_data import encrypt_data
from decrypt_data import decrypt_data


def login(salt):
	"""Verifica se a senha inserida pelo usuário está correta."""

	__PASSWORD_FILE = "DATA_GHOST.txt"

	print("\n==== ET256  [ @humanodev ]  ====")
	__password = stdiomask.getpass(prompt="\n=> Senha: ")

	# Combina senha + salt
	__KEY = KDF2(__password, salt, dkLen=32)
	
	# ===== Verificação da senha ===== #

	# Se, e somente se, a senha inserida estiver correta,
	# o arquivo de dados será decriptado (por pouco tempo)

	# Caso a senha esteja incorreta, a decriptação do arquivo de
	# dados não funcionará. Uma exceção ValueError será levantada
	# e o script irá fechar.
	decrypt_data(__PASSWORD_FILE + ".enc", __KEY)

	# Caso a senha esteja correta, a decriptação anterior funcionou,
	# então é o momento de encriptar o arquivo de dados novamente.
	encrypt_data(__PASSWORD_FILE, __KEY)

	return __KEY
