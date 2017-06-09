
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


LED_ARRAY_HEIGHT = 10
LED_ARRAY_LENGTH = 10
R = 0
G = 1
B = 2

def addRootPath (rootPath, path):
    return (rootPath + "/" + path)


def showImageBigger(im, size):
    im.resize(size, Image.NEAREST).show()


def flipEvenLines (im):
    im2 = im.copy()
#    pix = im2.load()

    image_height = im2.size[0]
    image_length = im2.size[1]

    for y in range (0, image_height):
        if (not y%2):
            line_copy = []
            for x in range (image_length):
                line_copy.append(im2.getpixel((x,y)))
            for x in range(image_length):
                im2.putpixel((x,y), line_copy[image_length -1 - x])

    return im2

def resizeImage (im, size):
    return im.resize(size, Image.ANTIALIAS)

def resizeImageDisplay (im):
    return resizeImage(im, (LED_ARRAY_LENGTH,LED_ARRAY_HEIGHT))

def resizeImageThumb (im, size):
    return im.resize(size, Image.NEAREST)

F_IMAGES = "Images"
SUBF_OUTPUT = "OUTPUT"
SUBF_CONVERT = "CONVERT"
SUBF_THUMBS = "THUMBS"

subfolders_list = [SUBF_OUTPUT, SUBF_CONVERT, SUBF_THUMBS]

full_subfolders_list = list()

for subf in subfolders_list:
    full_subfolders_list.append(addRootPath(F_IMAGES, subf))

print(full_subfolders_list)




# Check if 'Images' folder exists

dir_list = listdir('.')
#print (list1)

if (F_IMAGES in dir_list):
    print (F_IMAGES + " exists")
else:
    try:
        mkdir (F_IMAGES)
        print (F_IMAGES + " was created")
    except Exception as e:
        print ("Could not create folder " + F_IMAGES)
        print (e)
del dir_list

# check if subfolders exists
sub_dir_list = listdir (F_IMAGES)

for subfolder in subfolders_list:
    full_subfolder = addRootPath(F_IMAGES,subfolder)
    if (subfolder in sub_dir_list):
        print (full_subfolder + " exists")
    else:
        try:
            mkdir (full_subfolder)
            print (full_subfolder + " was created")
        except Exception as e:
            print ("Could not create folder " + full_subfolder)
            print (e)
del sub_dir_list

print ("\n")

#all needed folders exists now

#starting to deal with images to be converted
to_convert_path = addRootPath(F_IMAGES , SUBF_CONVERT)
output_path = addRootPath (F_IMAGES, SUBF_OUTPUT)
thumb_path = addRootPath (F_IMAGES, SUBF_THUMBS)

to_convert_files = listdir(to_convert_path)

for filename in to_convert_files:
    full_to_convert_path = addRootPath(to_convert_path, filename)
    full_to_output_path = addRootPath(output_path, filename)
    full_thumb_path = addRootPath(thumb_path, filename)

    im = Image.open (full_to_convert_path)
    image_height = im.size[0]
    image_length = im.size[1]

    print (full_to_convert_path + "\t" + str(image_height) + " x " + str(image_length))


    im_display = resizeImageDisplay(im)
    # showImageBigger(im_display, (300,300))
    #im_display.save(full_to_output_path,"PNG")

    #create thumbnail
    im_resize_big = resizeImageThumb(im_display, (300,300))
    im_resize_big.save(full_thumb_path,"PNG")

    #prepare image to create string
    im_flip = flipEvenLines (im_display)
    # showImageBigger(im_flip, (300,300))

    pix = im_display.load()
    image_height = im_display.size[0]
    image_length = im_display.size[1]
    image_string = ""
    for y in range (0, image_height):
        for x in range (0, image_length):
            red = pix[x,y][R]
            green = pix[x,y][G]
            blue = pix[x,y][B]

            image_string += str("{0:02X}{1:02X}{2:02X}".format(red, green, blue))

    #save string on a file
    file_out_name = full_to_output_path.split('.')[0] + ".txt"
    file_out = open(file_out_name, 'w')
    file_out.write(image_string)
    file_out.close()

exit()
