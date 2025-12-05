import betterConsole as bc
from time import sleep
import random



binarynum = random.randint(0,1)
print(binarynum)




bc.customise(bgCol="black", title="Matrix Loader V4")

bc.write("@green-@bold-matrix loader v4 boooting...",0.05)
bc.write("@green-main bootstrap loading...",0.05)
bc.write("@green-loading main kernel...",0.05)
bc.write("@green-loading file system...",0.05)
sleep(1)

usr = bc.ask("@green-Username:")

if usr != "gerd":
    bc.write("@red-@bold-@underlined-!NO!")
    bc.byebye()

pswd = bc.ask("@green-Password:")

if pswd != "1234":
    bc.write("@red-@bold-@underlined-!NO!")
    bc.byebye()

bc.clear()
bc.write("@green-@bold-Welcome To The Matrix")

bc.write("@green-@underline-Select Function")
bc.write("@green-[1] 101")
bc.write("@green-[2] Comming Soon")
bc.write("@green-[3] Comming Soon")

app = bc.ask("@green-@italic-Select Function:")

bc.write(" ")

if app == "1":
    bc.write("@green-Loading 101...",0.1)
    bc.write("@green-Loaded 101")
    bc.clear()
    
if app == "2":
    bc.write("@green-Loading Comming Soon...",0.1)
    
if app == "3":
    bc.write("@green-Loading Comming Soon...",0.1)

