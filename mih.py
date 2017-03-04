import heapq
import numpy as np
from bitstring import BitArray

def str_hamming(s1, s2):
	"""Calculate the Hamming distance between two bit strings"""
	return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def int_hamming(x,y):
	count, z = 0, x ^ y
	
	while z:
		count += 1
		z &= z-1 # magic!

	return count

sub_len = 16
m = 256 / sub_len
hash_bucket = {}
database = []

def construct_mih(lines):
	global hash_bucket
	global database
	database = lines

	for i in xrange(len(lines)):
		for j in xrange(m):
			start = j * sub_len
			end = start + sub_len

			sub_string = lines[i][start:end]
			tmp = BitArray(bin=sub_string).uint

			if (j, tmp) not in hash_bucket:
				hash_bucket[(j, tmp)] = [i]
			else:
				hash_bucket[(j, tmp)].append(i)

def mih_knn(input_codes, query_code, k):
	construct_mih(input_codes)

	bins = []
	for i in xrange(m / 2):
		bins.append(set())

	sub_codes = []
	for i in xrange(m):
		start = i * sub_len
		end = start + sub_len

		sub_string = query_code[start:end]
		tmp = BitArray(bin=sub_string).uint
		sub_codes.append(tmp)

	for key, value in hash_bucket.iteritems():
		hamming_dist = int_hamming(key[1], sub_codes[key[0]])

		# r / m ; 50%
		for i in xrange(m / 2 - 1, 0, -1):
			if hamming_dist / sub_len <= i:
				bins[i] |= set(value)
			else:
				break

	candidates = set()
	used = set()
	for i in xrange(m / 2):
		radius = (i + 1) * sub_len
		for candidate in bins[i]:
			if candidate in used:
				continue

			hamming_dist = str_hamming(database[candidate], query_code)

			if hamming_dist < radius:
				candidates.add((candidate, hamming_dist))
				used.add(candidate)

		if len(candidates) >= k:
			print radius
			candidates = list(candidates)
			result = heapq.nsmallest(8, candidates, key=lambda x: x[1])

			knn_result = [res[0] for res in result]
			return knn_result