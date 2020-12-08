# coding: utf-8


def insert_user_roots(index_option):
	"""Recebe diretórios raízes e os armazena em uma lista."""

	user_roots = []

	# limpa a lista para evitar redundâncias
	user_roots.clear()
	option = ("encriptado", "decriptado")

	# leitura e adição de raízes em uma lista para encriptar ou decriptar
	while True:
		try:
			roots = str(input(f"\nInsira o diretório raiz a ser {option[index_option]}: "))
		except (KeyboardInterrupt, EOFError, Exception):
			print("\n[ ? ]  Entrada Inválida..")
			continue
		else:
			user_roots.append(roots)

		while True:
			try:
				answer = str(input("\nDeseja inserir mais diretórios? [S/N]: ")).upper().strip()[0]
			except (KeyboardInterrupt, EOFError, Exception):
				print("\n[ ? ]  Entrada Inválida..")
			else:
				if answer in "SN":
					break
				else:
					print("\nOpção inválida. Apenas [S/N].")
		if answer == 'N':
			break

	return user_roots
