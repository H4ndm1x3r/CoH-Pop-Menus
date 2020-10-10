import os, fnmatch, json, shutil

mainDir = os.getcwd()
templatesFolder = mainDir+"\\templates"
directory = os.listdir(templatesFolder)

filePattern = "*.template"
mnu = ".mnu"

configFile = open(templatesFolder + "\\config.json")
config = json.load(configFile)
configFile.close()

for file in fnmatch.filter(directory, filePattern):
    filePath = templatesFolder + "\\" + file
    print(filePath)
    openFile = open(filePath, "r")
    readFile = openFile.read()
    name, extension = os.path.splitext(file)
    print(name, extension)
    outName = name + mnu
    outFile = open(mainDir + "\\" + outName, "w+")
    output = readFile
    
    for key, value in config.items():
        output = output.replace(key, value)

    outFile.write(output)