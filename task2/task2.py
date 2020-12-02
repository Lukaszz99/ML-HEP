#!/usr/bin/env python3

import ROOT as root
import numpy as np
import pandas as pd
import time

import matplotlib.pyplot as plt

start_time = time.time()

#clear global variables
root.gROOT.Reset()

# The conversion of the TTree to a numpy array is implemented with multi-
# thread support.
# About 2 times faster on I5-7200U with D0_Signal_MonteCarlo.root file
root.ROOT.EnableImplicitMT()

filename = '../data/D0_Signal_MonteCarlo.root'
file = root.TFile(filename, option='READ')

print(f'Loading file {filename} ...')

# print('List of objects in', filename)
# for key in file.GetListOfKeys():
#   print(key.GetClassName(), key.GetName())

#print(f'\nType tree name to load:')
#tree_name = input()

tree_name = 'ntpD0'
tree = file.Get(tree_name)

data, labels = tree.AsMatrix(return_labels=True)

print(f'Data loaded. Execution time {time.time() - start_time:.4f}')

test_data = data[:100]

plt.hist(x=test_data, bins=10, histtype='step')
plt.show()