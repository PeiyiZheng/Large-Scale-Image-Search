import sys
import numpy as np

def PCA(matrix, k=256):
	matrix = matrix - np.mean(matrix, axis=0)

	cov = np.cov(matrix, rowvar = 0)

	eigen_val, eigen_vec = np.linalg.eig(cov)

	idx = np.argsort(-eigen_val)
	sorted_val = eigen_val[idx]
	sorted_vec = eigen_vec[:, idx]

	print 'PCA Contribution: %.4f' % (1.0 * sum(sorted_val[:k]) / sum(sorted_val))

	idx = idx[:k]
	P = sorted_vec[:, idx]
	return matrix * P