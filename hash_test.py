import sys
import numpy as np
import random
import cv2
from mih import mih_knn

def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    data = []
    for line in lines:
        data.append(line)
    return data

image_names = readFile("images.txt")
binary_codes = readFile("binary_features.txt")

idx = random.randint(0, 149999)

source = (idx, binary_codes[idx], image_names[idx])

del image_names[idx]
del binary_codes[idx]

print here
exit()

result = mih_knn(binary_codes, source[1], 8)
result = [image_names[x] for x in result]
result = [source[2]] + result

for i in xrange(len(result)):
	img = cv2.imread('final/' + result[i].split("/",1)[1].strip())
	print img
	cv2.imshow('test', img)
	cv2.imwrite(str(i) + '.png', img)