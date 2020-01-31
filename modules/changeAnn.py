# Author:Rajashekar Yadavalli
# URL: https://github.com/RajashekarY
# Manipulate annotations using the following functions
import os
import sys
import argparse
import shutil

def changeClass(folderPath,existingClass,toClass): #folderPath:where annotations are 
    '''if you have generated annotations using Openimages tool kit for custom 
    objects and you want to use the same data but annotatiosn for yolo need a 
    change in class num then this script will come handy'''
    txtFiles = [txt for txt in os.listdir(folderPath) if txt.endswith('.txt')] 
    for afile in txtFiles:
        afile=os.path.join(folderPath,afile) 
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
