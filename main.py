#!/usr/bin/python

from os.path import expanduser
import subprocess
import signal
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
		killHTTPServers()
		pid = os.fork()
		if pid > 0:
			print("python HTTP server started")
			sys.exit(0)
		else:
			homeDir = expanduser("~")
			fullPath = os.path.join(homeDir, ".shaal")

			result = subprocess.run(
				['python3', '-m', 'http.server', '-d', fullPath],
				capture_output=True,
				text=True,
				check=True,
				stderr=subprocess.DEVNULL
			)

	if argv[1] == "stop":
		killHTTPServers()
		sys.exit(0)

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


def killHTTPServers():
	command = ["pgrep", "-f", "python.*-m http.server -d /home/"]

	try:
		result = subprocess.run(command, 
			capture_output=True, 
			text=True, 
		check=True)

		PIDs = result.stdout.strip().split('\n')
		PIDs = [int(pid) for pid in PIDs]
	except:
		PIDs = []

	for pid in PIDs:
		os.kill(pid, 9)
		print("old HTTP Server terminated")

main()
