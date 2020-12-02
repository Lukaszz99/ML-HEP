#!/usr/bin/env python3

import ROOT as root
import numpy as np

from custom_fnk import load_root, root_tree2array, label_position, make_hist


#clear global variables
root.gROOT.Reset()

root_file, root_objects = load_root()

#print('Type object to read', root_objects)
#tree_name = input()
tree_name = 'ntpD0'

if not tree_name in root_objects:
    print('Wrong value! abroting...')
    exit(1)

array, labels = root_tree2array(root_file, tree_name)

for _ in range(5):
    print('Choose variable to deal with: ', labels)
    leaf = input()

    leaf_index = label_position(labels, leaf)

    make_hist(x=array[:1000, leaf_index], bins=100, label=leaf)