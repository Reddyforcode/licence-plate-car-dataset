from os import listdir
from os.path import isfile, join
import cv2

mypath = "/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

cont = 0
for name in onlyfiles:
    print("entering")
    name1 = "/home/docout/Downloads/cars/to_git/imageclipper/"+name
    img = cv2.imread(name1)
    cv2.imwrite("{}.jpg".format(cont), img)
    cont = cont + 1