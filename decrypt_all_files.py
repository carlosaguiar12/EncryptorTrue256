# coding: utf-8

from insert_user_roots import insert_user_roots
from get_all_files import get_all_files
from decrypt_data import decrypt_data


def decrypt_all_files(key):
	"""Decripta todos os arquivos de uma ou mais raízes."""
	__roots__ = insert_user_roots(index_option=1)

	if len(__roots__) > 0:
		print('\n<<<<< DECRIPTANDO ARQUIVOS >>>>>\n')

		for root in __roots__:
			# Armazena o retorno com todos os arquivos, caso existam
			__files__ = get_all_files(root)

			if len(__files__) == 0:
				print(f'[ ERRO ]  Nenhum arquivo encontrado no diretório "{root}".\n')
			# Caso tenha encontrado algum arquivo na raiz inserida
			else:
				# Percorrendo cada caminho absoluto da raiz
				for file in __files__:
					# Descriptando cada um dos arquivos
					decrypt_data(file, key)
				print()
