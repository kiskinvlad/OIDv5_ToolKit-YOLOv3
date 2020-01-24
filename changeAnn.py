import os
import sys
import argparse
import shutil

def changeClass(FolderPath,existingClass,toClass): 
    txtFiles = [txt for txt in os.listdir(FolderPath) if txt.endswith('.txt')] 
    for afile in txtFiles:
        afile=os.path.join(FolderPath,afile) 
        fileOpen = open(afile,'r') 
        lines=[line.strip() for line in fileOpen.readlines()] 
        fileOpen.close()
        for index,line in enumerate(lines): 
            if line.startswith(existingClass): 
                line = line.replace(existingClass,toClass,1) 
                lines[index]=line 
        writeFile = open(afile,'w') 
        print(*lines,sep='\n',file=writeFile)
        writeFile.close()                                                                                                      

def copyAnn(fromFolder,toFolder):
    fromFolder = os.path.join(fromFolder,'Label')
    fromTXT = [txt for txt in os.listdir(fromFolder) if txt.endswith('.txt')]
    toTXT = [txt for txt in os.listdir(toFolder) if txt.endswith('.txt')]
    for fromFile in fromTXT:
        if fromFile in toTXT:
            appendFile = open(os.path.join(fromFolder,fromFile),'r')
            appendFile = [line.strip() for line in appendFile.readlines()]
            existFile = open(os.path.join(toFolder,fromFile),'r')
            existFile = [line.strip() for line in existFile.readlines()]
            allAnno = set(existFile+appendFile)
            existFile = open(os.path.join(toFolder,fromFile),'w')
            print(*allAnno,sep='\n',file=existFile)
        else:
            shutil.copyfile(os.path.join(fromFolder,fromFile),toFolder)

