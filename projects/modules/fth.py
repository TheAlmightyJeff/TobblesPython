def _Createfile():
    try:
        
        storage = open("storage.txt", "x")
        print("Couldnt find storage file... creating file...")
        
    except FileExistsError:
        
        print("storage file exists!")
        

def writeData(varName, data):

    """
    writes a value to a varible of the specified name
    """
    
    storage = open("storage.txt", "r")
    storageContent = storage.readlines()
    print(storageContent)
    
    lineToModify = storageContent.index(f"{varName}\n")
    print(lineToModify)
    
    storageContent[lineToModify + 1] = f"{data}\n"
    print(storageContent)

    storage = open("storage.txt", "w")
    storage.writelines(storageContent)
    
    
    

_Createfile()
writeData("hi", "sefsefsef")
