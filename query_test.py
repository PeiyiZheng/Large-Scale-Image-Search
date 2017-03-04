import sys
import numpy as np
import cv2
import heapq
import random
import time

def hamming(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    data = []
    for line in lines:
        data.append(line)
    return data

image_names = readFile("images.txt")
binary_codes = readFile("res_binary_features.txt")

idx = random.randint(0, 149999)

s = time.time()
source = (idx, binary_codes[idx])
database = []
for i in xrange(len(binary_codes)):
	if i == idx:
		continue

	database.append((i, hamming(source[1], binary_codes[i])))

result = heapq.nsmallest(8, database, key=lambda x: x[1])
result = [source] + result
print "time used:%f seconds\n" % (e - s)
for i in xrange(len(result)):
	img = cv2.imread(image_names[result[i][0]].split("/",1)[1].strip())
	cv2.imwrite(str(i) + '.png', img)

