"""
Location: OIDv4_ToolKit parent directory


Usage: 
    Start from OIDv4_ToolKit root directory.

    The script will create directories called To_PASCAL_XML (similar to the Label directories) in the Dataset Subdirectories.
    These directories contain the XML files.
    You need to download the Images and generate ToolKit-Style-Labels via the OIDv4_ToolKit before using this script.
    """

import os
from tqdm import tqdm
from sys import exit
import argparse
import cv2
from textwrap import dedent
from lxml import etree


# XML_DIR = os.path.join(label_dir,XML_annotations)#'To_PASCAL_XML'


# os.chdir(os.path.join("OID", "Dataset"))
# DIRS = os.listdir(os.getcwd())

# for DIR in DIRS:
#     if os.path.isdir(DIR):
#         os.chdir(DIR)

#         print("Currently in Subdirectory:", DIR)

#         CLASS_DIRS = os.listdir(os.getcwd())
        
#         for CLASS_DIR in CLASS_DIRS:
#             if os.path.isdir(CLASS_DIR):
#                 os.chdir(CLASS_DIR)

#                 print("\n" + "Creating PASCAL VOC XML Files for Class:", CLASS_DIR)
#                 # Create Directory for annotations if it does not exist yet
#                 if not os.path.exists(XML_DIR):
#                     os.makedirs(XML_DIR)

#                 #Read Labels from OIDv4 ToolKit
#                 os.chdir("Label")

#                 #Create PASCAL XML
def createXML(class_name,image_path,image_shape,bounding_box,XML_path):
        # for filename in tqdm(os.listdir(os.getcwd())):
        #     if filename.endswith(".txt"):
            filename_str = image_path.split("/")[-1].split('.')[0]


            annotation = etree.Element("annotation")
            
            # os.chdir("..")
            folder = etree.Element("folder")
            folder.text = os.path.basename(os.getcwd())
            annotation.append(folder)

            filename_xml = etree.Element("filename")
            filename_xml.text = os.path.basename(image_path) #"image name"
            annotation.append(filename_xml)

            path = etree.Element("path")
            path.text = os.path.join(image_path)
            annotation.append(path)

            source = etree.Element("source")
            annotation.append(source)

            database = etree.Element("database")
            database.text = "Open_Images_Dataset_V5"
            source.append(database)

            size = etree.Element("size")
            annotation.append(size)

            width = etree.Element("width")
            height = etree.Element("height")
            depth = etree.Element("depth")

            # img = cv2.imread(filename_xml.text)
            image_shape = image_shape.shape

            width.text = str(image_shape[1])
            height.text = str(image_shape[0])
            depth.text = str(image_shape[2])

            size.append(width)
            size.append(height)
            size.append(depth)

            segmented = etree.Element("segmented")
            segmented.text = "0"
            annotation.append(segmented)

            xmin_l = str(float(bounding_box[0]))
            ymin_l = str(float(bounding_box[1]))
            xmax_l = str(float(bounding_box[2]))
            ymax_l = str(float(bounding_box[3]))
            
            obj = etree.Element("object")
            annotation.append(obj)

            name = etree.Element("name")
            name.text = class_name
            obj.append(name)

            pose = etree.Element("pose")
            pose.text = "Random"
            obj.append(pose)

            truncated = etree.Element("truncated")
            truncated.text = "0"
            obj.append(truncated)

            difficult = etree.Element("difficult")
            difficult.text = "0"
            obj.append(difficult)

            bndbox = etree.Element("bndbox")
            obj.append(bndbox)

            xmin = etree.Element("xmin")
            xmin.text = xmin_l
            bndbox.append(xmin)

            ymin = etree.Element("ymin")
            ymin.text = ymin_l
            bndbox.append(ymin)

            xmax = etree.Element("xmax")
            xmax.text = xmax_l
            bndbox.append(xmax)

            ymax = etree.Element("ymax")
            ymax.text = ymax_l
            bndbox.append(ymax)

            s = etree.tostring(annotation, pretty_print=True)
            with open(XML_path+'/'+filename_str + ".xml", 'ab') as f:
                f.write(s)
                f.close()

                   
