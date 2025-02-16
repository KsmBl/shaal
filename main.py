#!/usr/bin/python

from os.path import expanduser
import subprocess
import sys
import os

HELP_MESSAGE = "usage:\nTODO\n"

#result = subprocess.run(['python3', '-m', 'http.server', '-d', '/shaal/'], capture_output=True, text=True, check=True)
#print(result.stdout)

def main():
	createShallDir()

	argv = sys.argv
	if len(argv) <= 1:
		print(HELP_MESSAGE)
		sys.exit(1)

	if argv[1] == "start":
		print("TODO")

	if argv[1] == "stop":
		print("TODO")

	if argv[1] == "add":
		if not len(argv) == 3:
			print(HELP_MESSAGE)
		else:
			filePath = argv[2]
			lnCommand = f"ln -s {filePath} ~/.shaal/"
			os.system(lnCommand)
			print(f"add {filePath} as a symlink to ~/.shaal/")

	if argv[1] == "remove":
		if not len(argv) == 3:
			print(HELP_MESSAGE)
		else:
			fileName = argv[2]
			if fileName.endswith("/"):
				fileName = fileName.rstrip("/")

			rmCommand = f"rm ~/.shaal/{fileName}"
			os.system(rmCommand)
			print(f"removed {fileName} as a symlink from ~/.shaal/")

	if argv[1] == "list":
		homeDir = expanduser("~")
		linkPath = os.path.join(homeDir, ".shaal")

		allLinks = [
			f for f in os.listdir(os.path.join(linkPath))
		]
		
		for i in allLinks:
			print(i)

def createShallDir():
	homeDir = expanduser("~")
	fullPath = os.path.join(homeDir, ".shaal")

	try:
		os.mkdir(fullPath)
		print("~/.shaal/ created. Here will land your symlinks to all files and directorys you wanna share")
	except FileExistsError:
		pass

main()
