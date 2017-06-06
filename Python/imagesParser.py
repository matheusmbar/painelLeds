
###############################################################################
## This is a script that will generate image files to be read through an
## Arduino from an SD card, based on PNG images present on folder CONVERT
## The images will be saved on folder READY
###############################################################################

## just to check if the Python3 is being used
#import sys
#print(sys.version)

from os import listdir
from os import mkdir
from PIL import Image  #lib tutorial http://effbot.org/imagingbook/image.htm

IMAGES_FOLDER_NAME = "Images"
IMAGES_READY_FOLDER_NAME = "READY"
IMAGES_CONVERT_FOLDER_NAME = "CONVERT"

LED_ARRAY_HEIGHT = 10
LED_ARRAY_LENGTH = 10


# Check if 'Images' folder exists

dir_list = listdir('.')
#print (list1)

if (IMAGES_FOLDER_NAME in dir_list):
    print (IMAGES_FOLDER_NAME + " exists")
else:
    try:
        mkdir (IMAGES_FOLDER_NAME)
        print (IMAGES_FOLDER_NAME + " was created")
    except Exception as e:
        print ("Could not create folder " + IMAGES_FOLDER_NAME)
        print (e)
del dir_list

# check if subfolders exists
sub_dir_list = listdir (IMAGES_FOLDER_NAME)
if (IMAGES_READY_FOLDER_NAME in sub_dir_list):
    print (IMAGES_READY_FOLDER_NAME + " exists")
else:
    try:
        mkdir (IMAGES_FOLDER_NAME + "/" + IMAGES_READY_FOLDER_NAME)
        print (IMAGES_READY_FOLDER_NAME + " was created")
    except Exception as e:
        print ("Could not create folder " + IMAGES_READY_FOLDER_NAME)
        print (e)

if (IMAGES_CONVERT_FOLDER_NAME in sub_dir_list):
    print (IMAGES_CONVERT_FOLDER_NAME + " exists")
else:
    try:
        mkdir (IMAGES_FOLDER_NAME + "/" + IMAGES_CONVERT_FOLDER_NAME)
        print (IMAGES_CONVERT_FOLDER_NAME + " was created")
    except Exception as e:
        print ("Could not create folder " + IMAGES_CONVERT_FOLDER_NAME)
        print (e)
del sub_dir_list
#all needed folders exists now

to_convert_path = IMAGES_FOLDER_NAME + "/" + IMAGES_CONVERT_FOLDER_NAME
to_convert_files = listdir(to_convert_path)
#print (to_convert_files)

for filename in to_convert_files:
    full_path = to_convert_path + "/" + filename
    #print (full_path)
    im = Image.open (full_path)
    image_height = im.size[0]
    image_length = im.size[1]

    print (full_path + "\t" + str(image_height) + " x " + str(image_length))
