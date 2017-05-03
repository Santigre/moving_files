import shutil
import os

src = 'C:\Users\Santiago B\Desktop\python\py_practice\File transfer\Folder A'
dst = 'C:\Users\Santiago B\Desktop\python\py_practice\File transfer\Folder B'

fA = os.listdir(src) #gets a list containing the names of the entries in the directory
fB = os.listdir(dst) #for each source and dst 

for f in fA:
    if f.endswith('.txt'): #checks what the file ends with so it can move all the txt files
        shutil.move(src+'\\'+f, dst) # once its gets the file name i have to add \\ for it to be added onto the address corectly
    print"File address:", src+"\\"+f #prints address
print"Files can now be found at", dst#prints destination

for b in fB: #put this here so i wouldnt have to go into the file a manuley move them back for testing
    if b.endswith('.txt'):
        shutil.move(dst+'\\'+b, src)
    print"They are moved back for further testing"


        
    


