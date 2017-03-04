import sys
import numpy as np

def ITQ(V, iter_num):
	sample_sz, bit_num = V.shape

	# Generating rotation matrix with Gaussian distribution of mean 0 and variance 1
	R = np.random.randn(bit_num, bit_num)
	U, V2, S2 = np.linalg.svd(R)
	R = U[:, range(0, bit_num)]

	for i in xrange(iter_num):
		# Fix R and update B
		V_ = V * R
		B = np.ones((V_.shape[0], V_.shape[1])) * -1
		B[V_ >= 0] = 1

		# Fix B and update R
		C = B.T * V
		S, sigma, S_ = np.linalg.svd(C)
		R = S_ * S.T

		print 'Iteration ' + str(i + 1) + ' finished.'

	V_ = V * R
	B = np.ones((V_.shape[0], V_.shape[1]))
	B[V_ < 0] = 0
	B = B.astype(int)

	return (B, R)