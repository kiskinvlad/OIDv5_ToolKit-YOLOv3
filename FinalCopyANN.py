import os
import shutil
#file of same name but different paths merger
#use find <Path to all the annotations segragated by classes> -name "*.txt" > trainAnno.txt
root_path = "/media/user1/storage-1/Rajashekar/OIDv4_ToolKit/OID/csv/trainAnno.txt"
final_path = "/media/user1/storage-1/Rajashekar/OIDv4_ToolKit/OID/csv/Annotations/"
txt = open(root_path,'r')

for path in txt.readlines():
    path = path.strip()
    baseName = os.path.basename(path)
    finalPath = os.path.join(final_path,baseName)
    if os.path.exists(finalPath):
        command = "cat {} >> {}".format(path,finalPath)
        os.system(command)
    else:
        shutil.copyfile(path,finalPath)