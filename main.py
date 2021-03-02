# -*- coding: utf-8 -*-
from sys import exit
from os import system, mkdir
from codecs import open as openc
from random import randint as rnt
import psutil

def getPython():
	procs = psutil.pids()
	for proc in procs:
		try:
			p = psutil.Process(proc)
			if p.name().__contains__('python'):
				return p.exe()
		except:
			pass
	return 0

def install(package):
	python = getPython()
	system(python + ' -m pip install ' + package)

try:
	from colorama import init, Fore
except:
	try:
		print('Colorama is not defined. Install...')
		install('colorama')
		from colorama import init, Fore
	except:
		print('Failed :(')
		system('pause')
		exit()
init()

def importCards(file):
	cards = []
	with openc(file, 'r', 'utf-8') as f:
		src = f.read()
	content = src.split(sep)
	for card in content:
		if card != '':
			cards.append(card)
	return cards

def choice(arr):
	index = rnt(0, len(arr)-1)
	value = arr[index]
	arr.pop(index)
	return value

def notify(color, text):
	print(color + text + Fore.RESET)

notify(Fore.LIGHTCYAN_EX, 'GreekMemo v1.0\nCreated by Maehdakvan\n\n\n')
sep = input('Enter a separator of cards (default is /): ')
if sep == '':
	sep = '/'
delim = input('Enter a delimiter of card (default is |): ')
if delim == '':
	delim = '|'

try:
	cards = importCards(input('Enter a path to file with cards: '))
	notify(Fore.LIGHTGREEN_EX, '\n{} cards loaded!'.format(len(cards)))
	rights = []
	fails = []
except:
	notify(Fore.LIGHTRED_EX, '\nFailed to load cards :(')
	system('pause')
	exit()

def session(cards):
	global rights, fails
	i = 0
	lns = len(cards)
	while i != lns:
		card = choice(cards)
		dem = card.split(delim)
		if input(dem[0] + ': ') == dem[1]:
			notify(Fore.LIGHTGREEN_EX, 'Right!')
			rights.append(card)
		else:
			notify(Fore.LIGHTRED_EX, 'Fail!')
			fails.append(card)
		i += 1

input(Fore.LIGHTCYAN_EX + 'Start memorize?')
system('cls')
notify(Fore.LIGHTCYAN_EX, '\nMemorize cards: ')
for card in cards:
	dem = card.split(delim)
	notify(Fore.LIGHTGREEN_EX, 'Question: {}\nAnswer: {}'.format(dem[0], dem[1]))
	input(Fore.LIGHTCYAN_EX + 'Revised? (ENTER)')
	system('cls')
session(cards)
lns = len(fails)
while lns != 0:
	system('cls')
	notify(Fore.LIGHTCYAN_EX, '\nMemorize fails: ')
	for fail in fails:
		dem = fail.split(delim)
		notify(Fore.LIGHTGREEN_EX, 'Question: {}\nAnswer: {}'.format(dem[0], dem[1]))
		input(Fore.LIGHTCYAN_EX + 'Revised? (ENTER)')
		system('cls')
	session(fails)
	lns = len(fails)

notify(Fore.LIGHTGREEN_EX, '\nAll Rights!!!')
system('pause')