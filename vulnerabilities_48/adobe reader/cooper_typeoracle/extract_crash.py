import json
import re
import os



def parse_crashfile(filename):
	crash_info = {}
	f = open(filename, "r")
	head = f.readline()
	banner = f.readline()
	while banner:
		# crash_info[num] = {}
		app_name = re.search(r"[^\s]*\.(?:api|dll|DLL|exe)", banner).group()
		# crash_info[num]["app_name"] = app_name
		tmp = f.readline()
		#print(tmp)
		module_name = re.search(r"[^\s]*\.(?:api|dll|DLL|exe)", tmp).group()
		# crash_info[num]["module_name"] = module_name
		tmp = f.readline()
		exception_code = re.search(r"0x[^\s]*", tmp).group()
		# crash_info[num]["exception_code"] = exception_code
		tmp = f.readline()
		offset = re.search(r"0x[^\s]*", tmp).group()
		# crash_info[num]["offset"] = offset
		for i in range(7):
			f.readline()
		banner = f.readline()
		crash_key = "{}_{}_{}_{}".format(app_name, module_name, exception_code, offset)
		if "AcroRd32" not in app_name:
			continue
		if crash_key in crash_info.keys():
			crash_info[crash_key] = crash_info[crash_key] + 1
		else:
			crash_info[crash_key] = 1
		print("app_name:%s\tmodule_name: %s\texception_code: %s\toffset: %s" % (app_name,module_name, exception_code, offset))

	f.close()
	return crash_info

def join_dict(dict1, dict2):
	for key in dict2.keys():
		if key not in dict1.keys():
			dict1[key] = dict2[key]
		else:
			dict1[key] += dict2[key]
	return dict1

all_crash = {}

for file in os.listdir("crashinfo"):
	tmp = parse_crashfile(os.path.join("crashinfo", file))
	all_crash = join_dict(all_crash, tmp)

print(all_crash)
print("unique crash:{}".format(len(all_crash.keys())))
all_num = 0
for key in  all_crash.keys():
	all_num += all_crash[key]
print("all crash:{}".format(all_num))
