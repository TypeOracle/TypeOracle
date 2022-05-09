import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import math
import os

LIMIT=100

def read_data(filename):
    f = open(filename, "r")
    line = f.readline().strip()
    x_points = []
    y_points = []
    base_x = int(line.split(',')[0])
    base_y = int(line.split(',')[1])
    line = f.readline().strip()
    read_num = 1
    while read_num < LIMIT:
        read_num += 1
        x_points.append(int(line.split(',')[0]))
        y_points.append(int(line.split(',')[1])-base_y)
        line = f.readline().strip()
    f.close()
    x_max = len(x_points)
    for i in range(x_max):
        x_points[i] = x_points[i] / x_max * 48
    return x_points, y_points

def parse_folder(folder_name):
    x_ordinates = []
    y_ordinates = []
    for i in os.listdir(folder_name):
        fname = os.path.join(folder_name, i)
        tmp_x, tmp_y = read_data(fname)
        x_ordinates = tmp_x
        y_ordinates.append(tmp_y)
    return x_ordinates, y_ordinates

def combine_array(arrs):
    length = len(arrs[0])
    min = [0xffffffff for i in range(length)]
    max = [0 for i in range(length)]
    sum = [0 for i in range(length)]
    test_len = len(arrs)
    for i in range(length):
        for arr in arrs:
            num = arr[i]
            sum[i] += num
            if num < min[i]:
                min[i] = num
            if num > max[i]:
                max[i] = num
    avg = [sum[i]/test_len for i in range(length)]
    return min, max, avg

def main():
    plt.rcParams['figure.figsize'] = (7.2, 4.05)
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 100
    hour_array, document_y_arr = parse_folder('adobe_manual')
    hour_array, random_y_arr = parse_folder('random')
    hour_array, typeoracle_adobe_y_arr = parse_folder('typeoracle_adobe')
    hour_array, typeoracle_foxit_y_arr = parse_folder('typeoracle_foxit')
    document_min, document_max, document_avg = combine_array(document_y_arr)
    random_min, random_max, random_avg = combine_array(random_y_arr)
    typeoracle_adobe_min, typeoracle_adobe_max, typeoracle_adobe_avg = combine_array(typeoracle_adobe_y_arr)
    typeoracle_foxit_min, typeoracle_foxit_max, typeoracle_foxit_avg = combine_array(typeoracle_foxit_y_arr)
    plt.plot(hour_array, random_avg, alpha = 0.9, color = "g", linestyle = "--", label =  "randomly fuzzing")
    plt.fill_between(hour_array, random_min, random_max, alpha = 0.4, color = "g", linestyle = "-")
    plt.plot(hour_array, document_avg, alpha = 0.9, color = "m", linestyle = ":", label =  "using Adobe manual")
    plt.fill_between(hour_array, document_min, document_max, alpha = 0.3, color = "m", linestyle = "-")
    plt.plot(hour_array, typeoracle_adobe_avg, alpha = 0.9, color = "c", linestyle = "-.", label =  "using TypeOracle on Adobe")
    plt.fill_between(hour_array, typeoracle_adobe_min, typeoracle_adobe_max, alpha = 0.4, color = "c", linestyle = "-")
    plt.plot(hour_array, typeoracle_foxit_avg, alpha = 0.9, color = "r", linestyle = "-", label =  "using TypeOracle on Foxit")
    plt.fill_between(hour_array, typeoracle_foxit_min, typeoracle_foxit_max, alpha = 0.4, color = "r", linestyle = "-")
    plt.legend(loc="best")
    x_major_locator = MultipleLocator(8)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.xlim(0, 49)
    plt.ylim(150000, 375000)
    plt.xlabel("Hours (h)")
    plt.ylabel("Coverage (# of instructions)")
    plt.savefig("foxit_type.pdf", bbox_inches = 'tight')
    typeoracle_incre = (typeoracle_foxit_avg[98] - random_avg[98]) / random_avg[98]
    print("argument info increment: {}".format(typeoracle_incre))
    plt.show()

if __name__ == "__main__":
    main()
