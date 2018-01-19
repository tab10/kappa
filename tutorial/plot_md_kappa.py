# function to generate MD kappa k vs. chain length plots
# run from inside directory with data files
# Tim Burt 10/5/17

import numpy as np
import glob
import matplotlib.pyplot as plt

num_lengths = 50
num_iter = 10

rawdata = np.zeros((num_lengths, num_iter))
cleandata_mean = np.zeros((num_lengths))
cleandata_std = np.zeros((num_lengths))
x = range(1, num_lengths + 1)

for name in glob.glob('*.k'):
    length_val = name.split("_")[1]
    iter_val = name.split("_")[3].strip('.k')
    k_val = open(name,"r")
    rawdata[length_val][iter_val] = k_val.read()

# averaging over replicas
for i in range(num_lengths):
    cleandata_mean[i] = np.mean(rawdata[i])
    cleandata_std[i] = np.std(rawdata[i], ddof=1)

plt.errorbar(x, cleandata_mean, yerr=cleandata_std)
plt.title('Thermal conductivity vs. chain length\nAverage of 10 runs\n300 K')
plt.legend('Polyeth')
plt.xlabel('Chain length (number of repeated molecules)')
plt.ylabel('Thermal conductance \\kappa \\frac{W}{mK}')
plt.savefig('k.pdf')
plt.show()
