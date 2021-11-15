import json
import re


crash_info = {}

f = open("CVE.txt", "r")
banner = f.readline()
num = 0
while banner:
	crash_info[num] = {}
	tmp = f.readline()
	module_name = re.search(r"[^\s]*\.(?:api|dll|DLL)", tmp).group()
	crash_info[num]["module_name"] = module_name
	tmp = f.readline()
	exception_code = re.search(r"0x[^\s]*", tmp).group()
	crash_info[num]["exception_code"] = exception_code
	tmp = f.readline()
	offset = re.search(r"0x[^\s]*", tmp).group()
	crash_info[num]["offset"] = offset
	for i in range(7):
		f.readline()
	banner = f.readline()
	print("%d module_name: %s\texception_code: %s\toffset: %s" % (num, module_name, exception_code, offset))
	num += 1

f.close()

with open("cve.json", "w") as f:
	json.dump(crash_info, f)