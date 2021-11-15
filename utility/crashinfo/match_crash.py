import json
import re
import os


cve_info = {}

with open("cve.json", "r") as f:
	cve_info = json.load(f)


def match_cve(module_name, exception_code, offset):
	match = []
	for cve_id in cve_info.keys():
		info = cve_info[cve_id]
		if module_name == info["module_name"]:
			if exception_code == info["exception_code"]:
				if offset == info["offset"]:
					match.append(cve_id)
	return match



def get_info(filename):
	results = set()

	f = open(filename, "r")
	f.readline()
	banner = f.readline()
	while banner:
		tmp = f.readline()
		# print(tmp)
		module_name = re.search(r"[^\s]*\.?(?:api|dll|DLL|exe|unknow|EXE)", tmp).group()
		tmp = f.readline()
		exception_code = re.search(r"0x[^\s]*", tmp).group()
		tmp = f.readline()
		offset = re.search(r"0x[^\s]*", tmp).group()
		res = set(match_cve(module_name, exception_code, offset))
		results = results|res
		for i in range(7):
			f.readline()
		banner = f.readline()
		# print("%d module_name: %s\texception_code: %s\toffset: %s" % (num, module_name, exception_code, offset))

	f.close()
	return results

results_oracle = set()
for file in os.listdir("crashinfo_typeoracle"):
	tmp = get_info(os.path.join("crashinfo_typeoracle", file))
	results_oracle = results_oracle | tmp
# for i in range(1, 26):
# 	tmp = get_info("crashinfo_typeoracle%d.txt"%i)
# 	results_oracle = results_oracle | tmp

results_favocado = set()
for file in os.listdir("crashinfo_favocado"):
	tmp = get_info(os.path.join("crashinfo_favocado", file))
	results_favocado = results_favocado | tmp
# for i in range(1, 4):
# 	tmp = get_info("crashinfo_favocado%d.txt"%i)
# 	results_favocado = results_favocado | tmp

results_favocadooracle = set()
for file in os.listdir("crashinfo_favocadotypeoracle"):
	tmp = get_info(os.path.join("crashinfo_favocadotypeoracle", file))
	results_favocadooracle = results_favocadooracle | tmp
# for i in range(1, 4):
# 	tmp = get_info("crashinfo_favocadooracle%d.txt"%i)
# 	results_favocadooracle = results_favocadooracle | tmp

print("results_oracle:")
print(results_oracle)
print(len(results_oracle))
print("=========================")
print("results_favocado:")
print(results_favocado)
print(len(results_favocado))
print("=========================")
print("results_favocadotypeoracle")
print(results_favocadooracle)
print(len(results_favocadooracle))