f = open("adobe_sample_result.txt", "r")
f2 = open("res.txt", "w")
line = f.readline()
base = int(line.strip().split(",")[1])
line = f.readline()
count = 0
while line:
	count += 1
	num = int(line.strip().split(",")[1])
	f2.write("%d, %d\n"%(count, num-base))
	line = f.readline()
f.close()
f2.close()