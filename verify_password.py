# coding: utf-8

import os
from login import login
from create_password import create_password


def verify_password(salt):
	"""Verifica a existência da senha de acesso."""

	__PASSWORD_FILE = "DATA_GHOST.txt"

	if os.path.isfile(__PASSWORD_FILE + ".enc"):
		return login(salt)
	else:
		create_password(salt)
