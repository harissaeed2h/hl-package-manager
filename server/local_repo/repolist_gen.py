import subprocess, json

lsOutput = ""

oldPercentage = 0
newPercentage = 0

def displayProgress(packages, packagesTemp):
	global oldPercentage, newPercentage
	oldPercentage = newPercentage
	newPercentage = int(len(packages.keys())/len(packagesTemp)*100)
	if oldPercentage != newPercentage:
		print(f"{newPercentage}%")

def initialize():
	lsOutput = subprocess.run("find ./ubuntu/ -type f".split(" "), stdout=subprocess.PIPE, text=True)
	lsOutput = lsOutput.stdout

	with open("repo.map", "w") as f:
		f.write(lsOutput)

def runCommand(command):
	return subprocess.run(command.split(" "), stdout=subprocess.PIPE, text=True).stdout

def getPackageDetails(packageLocation):
	packageInfo = runCommand(f"dpkg-deb -I {packageLocation}")
	packageDependencies = [line.replace("Depends: ", "") for line in packageInfo.split("\n") if "Depends:" in line]
	packageDependencies = [line.replace("(", "☕").replace(")", "☕").replace(" ", "") for line in packageDependencies]
	packageDependencies = [line.split(",") for line in packageDependencies]

	packageName = [line.replace("Package: ", "") for line in packageInfo.split("\n") if "Package: " in line]
	packageName = packageName[0].replace(" ", "")

	packageVersion = [line.replace("Version: ", "") for line in packageInfo.split("\n") if "Version: " in line]
	packageVersion = packageVersion[0].replace(" ", "")
	return packageName, packageVersion, packageDependencies

def savePackagesData(packages):
	with open("repo.list", "w") as f:
		json.dump(packages, f)

def main():
	initialize()
	with open("repo.map", "r") as f:
		lsOutput = f.read()
	packagesTemp = lsOutput.split("\n")

	packages = {}
	savePackagesData(packages)
	for package in packagesTemp:
		if not package == "":
			packageName, packageVersion, packageDependencies = getPackageDetails(package)
			packages[packageName] = { "file":str(package), "version":packageVersion, "Depends":packageDependencies}
			displayProgress(packages, packagesTemp)
			savePackagesData(packages)

main()