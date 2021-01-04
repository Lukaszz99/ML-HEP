"""
To działa, ale robi wykresy niepotrzebnych rzeczy, więc nie uzywac,
a traktować jako przykładowy kod!
"""


"""#!/usr/bin/env python3

import ROOT as root
import numpy as np
import time

from custom_fnk import load_root, root_tree2array, label_position, make_hist


#clear global variables
root.gROOT.Reset()

start_time = time.time()

filename = '../data/D0_Signal_MonteCarlo.root'

root_file, root_objects = load_root(filename)

#print('Type object to read', root_objects)
#tree_name = input()
tree_name = 'ntpD0'

if not tree_name in root_objects:
    print('Wrong value! abroting...')
    exit(1)

array, labels = root_tree2array(root_file, tree_name)

print(f'Data loaded! Time: {time.time() - start_time:.4f}')

#tot_entries = array.shape[0]
#print(f'Total entries in file {tot_entries}')

for leaf in labels:
    entries = 2000000
    leaf_index = label_position(labels, leaf)
    arr = array[:entries, leaf_index]

    make_hist(x=arr, bins=100, label=leaf, entries=entries, mean=np.mean(arr), std=np.std(arr))"""