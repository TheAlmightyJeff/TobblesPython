#----------------------------
# PYSave
# © 2025 - do not redistribute
#----------------------------

#VERSION BETA! THINGS WILL CHANGE.

def _Createfile():
    
    try:
        
        open("storage.pysave", "x")
        print("Couldn't find storage file... creating file...")
        
    except FileExistsError:
        
        print("Storage file exists!")


def writeData(varName, data):
    
    with open("storage.pysave", "r") as storage:
        storageContent = storage.readlines()


    storageContent = [line.rstrip("\n") for line in storageContent]

    if varName in storageContent:
        
        lineToModify = storageContent.index(varName)

        if lineToModify + 1 < len(storageContent):
            
            data = storageContent[lineToModify + 1]
            
        else:
        
            storageContent.append(data)
            
    else:

        storageContent.append(varName)
        storageContent.append(data)


    with open("storage.pysave", "w") as storage:
        for line in storageContent:
            storage.write(line + "\n")

def readData(varName):
    
    with open("storage.pysave", "r") as storage:
        storageContent = storage.readlines()

    storageContent = [line.rstrip("\n") for line in storageContent]

    lineToRead = storageContent.index(varName) + 1

    return storageContent[lineToRead]



_Createfile()
writeData("var1", "hello!")
print(readData("var1"))

