
SHELL := /bin/bash

list.txt: wortliste.txt makelist.py
	python ./makelist.py


passwords: list.txt exclude.txt
	python ./passwords.py --passwords=20 --length=3

