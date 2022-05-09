import json
import os

P1='infered_type'
P2='ground_truth'

global_fname = 'tmpresult.txt'
correct_report = {}
typeoracle = {}
truth = {}
TypeNum2Str = {'0': "Boolean", '1': "Number", '2': "builtin-obj", '3': "String", '220': "Array", '221': "Array", '222': "Array", '223': "Array", '231': "Object",'5': "Value", '50': "Value", '210': "Value"}

def dump_file(content):
    with open(global_fname, 'a') as f:
        f.write(content)

def calculate_arg_type_num(self, arg_type_set):
    res_set = set()
    primitive = ['0', '1', '2', '3']
    for i in arg_type_set:
        if i in primitive:
            res_set.add(i)
        elif i.startswith('23'):
            res_set.add('23')
        elif i.startswith('22'):
            res_set.add('22')

    return len(res_set)

def count_type(dir1):
    all_info = {}
    res = {}

    for fname in os.listdir(dir1):
        fpath = os.path.join(dir1,fname)
        tmp = readjson(fpath)
        apiname = tmp['api']
        all_info[apiname] = tmp
    for api in all_info.keys():
        d = all_info[api]
        apitype = d['apitype'] # select method
        # print(d['api'])
        if apitype == 0:
            root_type = d['root']
            root_obj = d['info'][root_type]
            if 'req_type' not in root_obj.keys():
                continue
            for typeid in root_obj['req_type']:
                if typeid in res:
                    res[typeid] += 1
                else:
                    res[typeid] = 1
            for typeid in root_obj['opt_type']:
                if typeid in res:
                    res[typeid] += 1
                else:
                    res[typeid] = 1
        elif apitype == 1:
            typeid = d['root']
            if typeid in res:
                res[typeid] += 1
            else:
                res[typeid] = 1
    # print(res)
    return res


def parse_type(typeid):
    if typeid == '2':
        return '20'
    elif typeid == '5':
        return '50'
    elif typeid[0] == '5' and len(typeid) > 1:
        return '51'
    elif len(typeid) > 1:
        return typeid[:2]
    else:
        return typeid


def compare_value(typeid1, typeid2):
    t1 = parse_type(str(typeid1))
    t2 = parse_type(str(typeid2))
    if t1 == t2:
        return True
    else:
        return False


def print_info(typeid, dic):
    if typeid in dic['info']:
        return repr(dic['info'][typeid])
    else:
        return str(typeid)


def compare_setter(dic1, dic2):
    apiname = dic1['api']
    t1 = dic1['root']
    t2 = dic2['root']
    flag = compare_value(t1, t2)
    if flag == False:
        tmp = 'setter:%s\n- p1: %s\n- p2: %s\n' % (
            apiname, print_info(t1, dic1), print_info(t2, dic2))
        dump_file(tmp)


def compare_json(dic1, dic2):
    apiname = dic1['api']
    r1 = dic1['info'][dic1['root']]
    r2 = dic2['info'][dic2['root']]
    d1 = {}
    d2 = {}
    for k, v in zip(r1['req_key'], r1['req_type']):
        d1[k] = v
    for k, v in zip(r1['opt_key'], r1['opt_type']):
        d1[k] = v
    for k, v in zip(r2['req_key'], r2['req_type']):
        d2[k] = v
    for k, v in zip(r2['opt_key'], r2['opt_type']):
        d2[k] = v
    sumk = set(d1.keys()) | set(d2.keys())
    flag = 0
    content = 'binding call: %s\n' % apiname
    index = 0
    for k in sumk:
        content += "- parameter%d:\n"%(index)
        index += 1
        if k not in d1:
            # content += '- p1 lack key: %s\n' % (k)
            content += '  - %s: Missing\n' % (P1)
            content += '  - %s: %s\n' % (P2, TypeNum2Str[d2[k]])
            flag = 1
        elif k not in d2:
            content += '- p2 lack key: %s\n' % (k)
            flag = 1
        else:
            tp = compare_value(d1[k], d2[k])
            content += '  - %s: %s\n' % (P1, TypeNum2Str[d1[k]])
            content += '  - %s: %s\n' % (P2, TypeNum2Str[d2[k]])
            if tp == False:
                flag = 1
                # content += '- key:%s\tp1: %s\tp2: %s\n' % (
                #     k, print_info(d1[k], dic1), print_info(d2[k], dic2))
                correct_report[d1[k]] -= 1
    # if flag == 1:
    dump_file(content)
def count_in_list(alist, target):
    res = 0
    for i in alist:
        if i in target:
            res += 1
    return res

def output_missing(alist):
    content = ''
    if '0' in alist:
        tmp = count_in_list(alist, '0')
        content += '- missing %d Boolean\n' % (tmp)
    if '1' in alist:
        tmp = count_in_list(alist, '1')
        content += '- missing %d Number\n' % (tmp)
    if '3' in alist:
        tmp = count_in_list(alist, '3')
        content += '- missing %d String\n' % (tmp)
    array_num = 0
    json_num = 0
    for i in alist:
        if i.startswith('22'):
            array_num += 1
        if i.startswith('23'):
            json_num += 1
    if array_num != 0:
        content += '- missing %d Array\n' % (array_num)
    if json_num != 0:
        content += '- missing %d Object\n' % (json_num)
    return content



def compare_array(dic1, dic2):
    apiname = dic1['api']
    r1 = dic1['info'][dic1['root']]
    r2 = dic2['info'][dic2['root']]
    l1 = []
    l2 = []
    l1.extend(r1['req_type'])
    l1.extend(r1['opt_type'])
    l2.extend(r2['req_type'])
    l2.extend(r2['opt_type'])

    sumk = max(len(l1), len(l2))

    flag = 0
    content = 'binding call: %s\n' % apiname

    if len(l1) != len(l2):
        flag = 1
        content += '- diff in arg length: %s - %s , %s - %s\n' % (P1, 
            len(l1), P2, len(l2))
        # content += output_missing(l2)

    for ind in range(sumk):
        content += "- parameter%d:\n"%(ind)
        if ind >= len(l1):
            content += '  - %s: Missing\n' % (P1)
            t1 = 'cc'
        else:
            content += '  - %s: %s\n' % (P1, TypeNum2Str[l1[ind]])
            t1 = l1[ind]
        content += '  - %s: %s\n' % (P2, TypeNum2Str[l2[ind]])
        t2 = l2[ind]
        tp = compare_value(t1, t2)
        if tp == False:
            flag = 1
            # content += '- ind:%d\t%s: %s\t%s: %s\n' % (
            #     ind, P1, print_info(t1, dic1), P2, print_info(t2, dic2))

    # if flag == 1:
    dump_file(content)


def compare_json_and_array(dic1, dic2):
    apiname = dic1['api']
    r1 = dic1['info'][dic1['root']]
    r2 = dic2['info'][dic2['root']]
    l1 = []
    l2 = []
    k1 = []
    l1.extend(r1['req_type'])
    l1.extend(r1['opt_type'])
    k1.extend(r1['req_key'])
    k1.extend(r1['opt_type'])
    l2.extend(r2['req_type'])
    l2.extend(r2['opt_type'])

    sumk = min(len(l1), len(l2))

    flag = 0
    content = 'method json-arr: %s\n' % apiname

    if len(l1) != len(l2):
        flag = 1
        content += '- diff in arg length: %s - %s , %s - %s\n' % (P1, 
            len(l1), P2, len(l2))

    for ind in range(sumk):
        t1 = l1[ind]
        t2 = l2[ind]
        tp = compare_value(t1, t2)
        if tp == False:
            flag = 1
            content += '- ind:%d key:%s\t%s: %s\t%s: %s\n' % (
                ind, k1[ind], P1, print_info(t1, dic1), P2, print_info(t2, dic2))

    if flag == 1:
        dump_file(content)


def readjson(fname):
    with open(fname, 'r') as f:
        return json.loads(f.read())
    
def compare_full(dic1,dic2):
    if dic1['apitype'] == 1:
        compare_setter(dic1, dic2)
        return
    f1 = dic1['root']
    f2 = dic2['root']

    if f1.startswith('22'):
        flag1 = 0 # array
    else:
        flag1 = 1 # json

    if f2.startswith('22'):
        flag2 = 0
    else:
        flag2 = 1
    
    if flag1 == 0 and flag2 == 0:
        compare_array(dic1, dic2)
    elif flag1 == 1 and flag2 == 1:
        compare_json(dic1, dic2)
    elif flag1 == 0 and flag2 == 1:
        compare_json_and_array(dic2, dic1)
    else:
        compare_json_and_array(dic1, dic2)
    
def main(dir1,dir2,output):
    global global_fname
    global_fname = output
    d1 = {}
    d2 = {}
    for fname in os.listdir(dir1):
        fpath = os.path.join(dir1,fname)
        tmp = readjson(fpath)
        apiname = tmp['api']
        d1[apiname] = tmp
    for fname in os.listdir(dir2):
        fpath = os.path.join(dir2,fname)
        tmp = readjson(fpath)
        apiname = tmp['api']
        d2[apiname] = tmp
    commonkey = set(d1.keys())&set(d2.keys())
    for key in sorted(list(commonkey)):
        # print(key)
        compare_full(d1[key],d2[key])

def get_array_num(count_dic):
    res = 0
    for i in count_dic.keys():
        if i.startswith("22"):
            res += count_dic[i]

    return res

def get_json_num(count_dic):
    res = 0
    for i in count_dic.keys():
        if i.startswith("23"):
            res += count_dic[i]

    return res

def get_all_num(count_dic):
    res = count_dic['0'] + count_dic['1'] + count_dic['3']
    res += get_array_num(count_dic)
    res += get_json_num(count_dic)
    return res

def calculate(correct_report, typeoracle):
    res = {}
    for i in ['0', '1', '3']:
        res[i] = correct_report[i] / typeoracle[i] * 100
    res['22'] = get_array_num(correct_report) / get_array_num(typeoracle) * 100
    res['23'] = get_json_num(correct_report) / get_json_num(typeoracle) * 100
    return res

def my_div(num1, num2):
    return num1 / num2 * 100

if __name__ == '__main__':
    typeoracle = count_type(P1)
    correct_report = count_type(P1)
    truth = count_type(P2)
    main(P1,P2,'foxit.txt')
    print("\t\t\tBoolean\tNumber\tString\tArray\tObject\tTotal")
    print("correctly report\t%d\t%d\t%d\t%d\t%d\t%d"%(correct_report['0'], correct_report['1'], correct_report['3'], 
        get_array_num(correct_report), get_json_num(correct_report), get_all_num(correct_report)))
    print("reported cases\t\t%d\t%d\t%d\t%d\t%d\t%d"%(typeoracle['0'], typeoracle['1'], typeoracle['3'], 
        get_array_num(typeoracle), get_json_num(typeoracle), get_all_num(typeoracle)))
    print("actual cases\t\t%d\t%d\t%d\t%d\t%d\t%d"%(truth['0'], truth['1'], truth['3'], 
        get_array_num(truth), get_json_num(truth), get_all_num(truth)))
    precision = calculate(correct_report, typeoracle)
    recall = calculate(correct_report, truth)
    print("precision\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f"%(precision['0'], precision['1'], precision['3'], 
        get_array_num(precision), get_json_num(precision), my_div(get_all_num(correct_report), get_all_num(typeoracle))))
    print("recall\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f"%(recall['0'], recall['1'], recall['3'], 
        get_array_num(recall), get_json_num(recall), my_div(get_all_num(correct_report), get_all_num(truth))))
