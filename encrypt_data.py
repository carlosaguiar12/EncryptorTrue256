# coding: utf-8

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encrypt_data(file_name, key):
	"""Criptografa os dados do arquivo."""

	# Verifica se o arquivo existe e
	# se já não está encriptado.
	if os.path.isfile(file_name):
		if not file_name.endswith(".enc"):

			# Leitura da sequência binária
			with open(file_name, "rb") as fo:
				plaintext = fo.read() # Conteúdo do arquivo

			# Verifica erros de valor ao encriptar
			try:
				# Inicializa um objeto cifra com a chave
				cipher = AES.new(key, AES.MODE_CBC)

				# ==== Encriptando os dados ==== #
				data_ciphered = cipher.encrypt(pad(plaintext, AES.block_size))

				# Adiciona a extensão ".enc" ao arquivo
				with open(file_name + ".enc", "wb") as fo:
					# Escreve o vetor de inicialização e
					# os dados encriptados no arquivo
					fo.write(cipher.iv)
					fo.write(data_ciphered)

				# Deleta o arquivo original
				os.remove(file_name)

			except ValueError:
				# Adicionar arquivo para mostrar os erros
				pass

			else:
				# Mostra que a encriptação ocorreu com sucesso
				if file_name != "DATA_GHOST.txt":
					print(f"[ OK ]  {file_name}")

		else:
			print(f"\n[ ? ]  O arquivo {file_name} já foi encriptado.")

	else:
		print(f"[ ERRO ]  O arquivo '{file_name}' não existe. Tente com outro nome.")
