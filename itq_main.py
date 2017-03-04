import sys
import numpy as np
from pca import PCA
from itq import ITQ

def writeMatrixToFile(filename, matrix, sep=","):
	file = open(filename, "w")
	row, col = matrix.shape

	for i in range(row):
		for j in range(col):
			file.write(str(matrix[i, j]))
			if j != col - 1:
				file.write(sep)
		file.write("\n")
	file.close()

def strListToFloatList(line):
    temp = []
    for item in line:
        temp.append(float(item))
    return temp

def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    data = []
    for line in lines:
        items = line.split()
        data.append(strListToFloatList(items))
    mx = np.mat(data)
    return mx

iterations = 50
c = 256

input_features = readFile('res_features.txt')
pca_features = PCA(input_features, c)
(binary_features, rotation_mat) = ITQ(pca_features, iterations)

writeMatrixToFile('res_binary_features.txt', binary_features, "")
writeMatrixToFile('res_rotation_mat.txt', rotation_mat)
