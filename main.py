# -*- coding: utf-8 -*-
from sys import exit
from os import system, mkdir
from codecs import open as openc
from random import randint as rnt
import psutil, ctypes

def initConsole():
	LF_FACESIZE = 32
	STD_OUTPUT_HANDLE = -11

	class COORD(ctypes.Structure):
	    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

	class CONSOLE_FONT_INFOEX(ctypes.Structure):
	    _fields_ = [("cbSize", ctypes.c_ulong),
	                ("nFont", ctypes.c_ulong),
	                ("dwFontSize", COORD),
	                ("FontFamily", ctypes.c_uint),
	                ("FontWeight", ctypes.c_uint),
	                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

	font = CONSOLE_FONT_INFOEX()
	font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
	font.nFont = 16
	font.dwFontSize.X = 11
	font.dwFontSize.Y = 18
	font.FontFamily = 54
	font.FontWeight = 400
	font.FaceName = "Consolas"

	handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	ctypes.windll.kernel32.SetCurrentConsoleFontEx(handle, ctypes.c_long(False), ctypes.pointer(font))

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
initConsole()
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

input('Start memorize? (ENTER)')
system('cls')
notify(Fore.LIGHTCYAN_EX, '\nMemorize cards: ')
for card in cards:
	dem = card.split(delim)
	notify(Fore.LIGHTGREEN_EX, 'Question: {}\nAnswer: {}'.format(dem[0], dem[1]))
	input('Revised? (ENTER)')
	system('cls')
session(cards)
lns = len(fails)
while lns != 0:
	system('cls')
	notify(Fore.LIGHTCYAN_EX, '\nMemorize fails: ')
	for fail in fails:
		dem = fail.split(delim)
		notify(Fore.LIGHTGREEN_EX, 'Question: {}\nAnswer: {}'.format(dem[0], dem[1]))
		input('Revised? (ENTER)')
		system('cls')
	session(fails)
	lns = len(fails)

notify(Fore.LIGHTGREEN_EX, '\nAll Rights!!!')
system('pause')