import os

INPUT_DIR = 'adobe_sample_output'
OUTPUT_FNAME = 'adobe_sample_result.txt'

def parse(fpath):
	with open(fpath,'r') as f:
		raw = f.read()
	rlst = [i for i in raw.split('\n') if len(i)>0]
	nlst = []
	for i in rlst:
		a,b = i.split(',')
		nlst.append(int(b))

	return nlst

def combine(lst1,lst2):
	r = []
	for i,j in zip(lst1,lst2):
		r.append(i+j)
	return r

flst = os.listdir(INPUT_DIR)
plst = [os.path.join(INPUT_DIR,i) for i in flst]
datalst = [parse(i) for i in plst]

init = datalst[0][:]

for i in datalst[1:]:
	init = combine(init,i)

r = ['%d,%d'%(ind,i) for ind,i in enumerate(init)]

with open(OUTPUT_FNAME,'w') as f:
	f.write('\n'.join(r))