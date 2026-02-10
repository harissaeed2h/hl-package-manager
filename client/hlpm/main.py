import os, subprocess, json, requests
from pathlib import Path

from autocomplete import autocomplete
from config import repositorServerAddress, hlpmDefaultDir

repoListData = {}
userHomeDir = Path.home()
repoListFilePath = os.path.join(userHomeDir, "hlpm/repo.list")

def init():
	global repoListData
	try:
		response = requests.get(repositorServerAddress+"repo.list")
		with open(repoListFilePath, "wb") as f:
			f.write(response.content)
	except:
		with open(repoListFilePath, "wb") as f:
			json.dumps("{}")
		print("W: Unable to update the repolist. You may ignore this")
	try:
		with open(repoListFilePath) as f:
			repoListData = f.read()
			repoListData = json.loads(repoListData)
			for packageName in repoListData.keys():
				repoListData[packageName]["file"] = repositorServerAddress+repoListData[packageName]["file"][2:]
				#DEBUG?: print(f"{repoListData[packageName]["file"]}")
	except:
		print("error while trying to load repository list. Please try running the 'get repolist' command")
	try:
		tempResponse = runCommand(f"mkdir {userHomeDir}/.local/share/hlpm/ -p")
	except:
		return f"unable to create directory: {tempResponse}"

def runCommand(command):
	return subprocess.run(command.split(" "), stdout=subprocess.PIPE, text=True).stdout

def searchPackages(query):
	for item in repoListData.keys():
		if query in item:
			print(item)

def processDependencies(dependenciesRaw):
	dependencies = {}
	for dependency in dependenciesRaw:
		dependencyName = dependency.split("☕")[0]
		dependencyVersion = dependency.split("☕")[1]
		dependencies[dependencyName] = { "version" : dependencyVersion }
	return dependencies

def downloadPackage(packageName):
	url = repoListData[packageName]["file"]
	filename = f"{userHomeDir}/.local/share/hlpm/{url.split("/")[-1]}"
	with requests.get(url, stream=True) as response:
		response.raise_for_status()
		with open(filename, "wb") as f:
			for chunk in response.iter_content(chunk_size=8192):
				f.write(chunk)

def installPackage(packageName):
	packageInformation = repoListData[packageName]
	file = packageInformation["file"]
	dependenciesRaw = packageInformation["Depends"][0]
	dependencies = processDependencies(dependenciesRaw)
	for dependencyName in dependencies.keys():
		print(f"installing dependency: {dependencyName}")
		downloadPackage(dependencyName)
		runCommand(f"sudo dpkg -i {userHomeDir}/.local/share/hlpm/{repoListData[dependencyName]["file"].split("/")[-1]}")

	downloadPackage(packageName)
	runCommand(f"sudo dpkg -i {userHomeDir}/.local/share/hlpm/{repoListData[packageName]["file"].split("/")[-1]}")

def processCommand(command):
	command = command.split(" ")
	if command[0] == "search":
		try:
			query = command[1]
		except:
			return "Error in command, no query was provided"
		searchPackages(query)
	elif command[0] == "install":
		for packageName in command[1].split(","):
			installPackage(packageName)
	elif command[0] == "init":
		init()
	else:
		return "Command not found"
	return "Command Executed"

def main():
	init()
	autocomplete(list(repoListData.keys()))
	while True:
		command = input("> ")
		try:
			print(processCommand(command))
		except:
			print("Unknown error while executing command; E001")

main()