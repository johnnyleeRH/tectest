import numpy as np 
from matplotlib import pyplot as plt
import sys

'''
variadic input, input file
time cost style: flag timecost xxx msec
'''
if __name__ == '__main__':
    flags = {}
    fd = open((sys.argv)[1], "rb")
    while True:
        line = fd.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            break

        if line.find(str.encode("timecost")) != -1 and line.find(str.encode("msec")) != -1:
            flag = line.split()[0]
            time = line.split()[-2]
            if flag not in flags.keys():
                flags[flag] = []
                flags[flag].append(float(time))
            else:
                flags[flag].append(float(time))
    if len(flags) > 0:
        plt.figure(50)
        row = 2
        col = (len(flags) + 1 ) / 2
        id = 0
        for flag in flags.keys():
            id = id + 1
            plt.subplot(row, col, id)
            plt.xlabel(flag)
            plt.ylabel("timecost (ms)")
            x = np.arange(0, len(flags[flag]))
            plt.plot(x, flags[flag], 'or')
        plt.legend()
        plt.show()
    else:
        print("no input flag")
