import os, fnmatch, json, shutil

char = "$"

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
    openFile = open(filePath, "r")
    readFile = openFile.read()
    name, extension = os.path.splitext(file)
    outName = name + mnu
    outFile = open(mainDir + "\\" + outName, "w+")
    output = readFile
    for key, value in config.items():
        var = char + key
        output = output.replace(var, value)

    outFile.write(output)