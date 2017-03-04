import sys
from bitstring import BitArray

def int_hamming(x,y):
	count, z = 0, x ^ y
	
	while z:
		count += 1
		z &= z-1 # magic!

	return count

def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    data = []
    for line in lines:
        data.append(line)
    return data

def construct_radius_table(filename, s):
	global radius_table
	global dist_table
	file = open(filename, 'w')
	sz = 2 ** s
	for i in xrange(sz):
		dist = []
		print i
		for j in xrange(sz):
			dist.append(int_hamming(i, j))

		file.write(str(i) + '\n')
		dist0 = []
		dist1 = []
		dist2 = []
		dist3 = []
		for j in xrange(sz):
			if dist[j] == 0:
				dist0.append(j)
			if dist[j] == 1:
				dist1.append(j)
			if dist[j] == 2:
				dist2.append(j)
			if dist[j] == 3:
				dist3.append(j)

		file.write(str(dist0[0]) + '\n')
		file.write(' '.join(str(x) for x in dist1) + '\n')
		file.write(' '.join(str(x) for x in dist2) + '\n')
		file.write(' '.join(str(x) for x in dist3) + '\n')
	
	file.close()

multi_index_table = {}
def construct_multi_index_hash(input_filename, sub_len, m):
	lines = read_file(input_filename)

	for i in xrange(len(lines)):
		for j in xrange(m):
			start = j * sub_len
			end = start + sub_len

			sub_string = lines[i][start:end]
			tmp = BitArray(bin=sub_string).uint

			if (j, tmp) not in multi_index_table:
				multi_index_table[(j, tmp)] = [i]
			else:
				multi_index_table[(j, tmp)].append(i)

	sz = 2 ** sub_len
	for j in xrange(m):
		file = open(str(j) + '.txt', 'w')

		for i in xrange(sz):
			if (j, i) not in multi_index_table:
				continue

			tmp = [i] + [x for x in multi_index_table[(j, i)]]
			file.write(' '.join(str(x) for x in tmp) + '\n')

		file.close()

def split_database(input_filename, output_filename, sub_len, m):
	lines = read_file(input_filename)
	file = open(output_filename, 'w')
	for i in xrange(len(lines)):
		line = []
		for j in xrange(m):
			start = j * sub_len
			end = start + sub_len

			sub_string = lines[i][start:end]
			tmp = BitArray(bin=sub_string).uint

			line.append(tmp)

		file.write(' '.join(str(x) for x in line) + '\n')

	file.close()

#construct_radius_table('radius_table.txt', 16)
#construct_multi_index_hash('res_binary_features.txt', 16, 16)
#split_database('res_binary_features.txt', 'splited_res_features.txt', 16, 16)
exit()