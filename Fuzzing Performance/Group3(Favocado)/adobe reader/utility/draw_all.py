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
    prefix = os.path.join('../', 'data')
    folder_name = os.path.join(prefix, folder_name)
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
    plt.rcParams['figure.figsize'] = (7.2, 1.85)
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 100
    hour_array, favocado_y_arr = parse_folder('favocado')
    hour_array, favocado_oracle_y_arr = parse_folder('favocado_typeoracle')
    favocado_min, favocado_max, favocado_avg = combine_array(favocado_y_arr)
    favocado_oracle_min, favocado_oracle_max, favocado_oracle_avg = combine_array(favocado_oracle_y_arr)
    plt.plot(hour_array, favocado_avg, alpha = 0.9, color = "b", linestyle = "--", label =  "Favocado")
    plt.fill_between(hour_array, favocado_min, favocado_max, alpha = 0.3, color = "b", linestyle = "-")
    plt.plot(hour_array, favocado_oracle_avg, alpha = 0.9, color = "r", linestyle = "-", label =  "Favocado+TypeOracle")
    plt.fill_between(hour_array, favocado_oracle_min, favocado_oracle_max, alpha = 0.4, color = "r", linestyle = "-")
    plt.legend(loc="best")
    x_major_locator = MultipleLocator(8)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.xlim(0, 49)
    plt.xlabel("Hours (h)")
    plt.ylabel("Coverage (# of instructions)")
    plt.savefig("adobe_favocado.pdf", bbox_inches = 'tight')
    random_incre = (favocado_oracle_avg[98] - favocado_avg[98]) / favocado_avg[98]
    print("increment: {}".format(random_incre))
    plt.show()

if __name__ == "__main__":
    main()
