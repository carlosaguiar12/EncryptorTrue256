# coding: utf-8

__author__ = "@humanodev"  # Instagram

from options_menu import options_menu
from verify_password import verify_password


class ET256():
	"""Encripta e decripta arquivos a 256 Bits."""

	def __init__(self, key):
		options_menu(key)


if __name__ == "__main__":
	# Dado aleatório de tamanho 256 Bits
	salt = b'*\xbf\xc2\xb6i`\x86\x96\xd8\x9d?\xb1/\xb9\xf7\xe38\x90\xc2m\xae\x99t\x92\xf6P\xc8\xaa\xf5\x8e\xd16'

	# Caso seja o primeiro acesso, irá para a criação de senha
	# Caso a senha já exista, será feita a tentativa de login
	ET256(key=verify_password(salt))
