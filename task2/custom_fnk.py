#!/usr/bin/env python3

import ROOT as root
import numpy as np

import matplotlib.pyplot as plt

def load_root(filename):
    print(f'Loading file {filename} ...')

    file = root.TFile(filename, option='READ')

    # list of objects in root file
    objects = [key.GetName() for key in file.GetListOfKeys() if key.GetClassName() == 'TNtuple']

    return file, objects

def root_tree2array(root_file, tree_name):
    # The conversion of the TTree to a numpy array is implemented with multi-
    # thread support.
    # About 2 times faster on I5-7200U with D0_Signal_MonteCarlo.root file
    root.ROOT.EnableImplicitMT()

    tree = root_file.Get(tree_name)

    array, labels = tree.AsMatrix(return_labels=True)

    return array, labels, 

def label_position(list, name):
    return list.index(name)

def make_hist(x, bins, label, entries, mean, std):
    hist_desc = f'Entries {format(entries, ".2e")} \nMean {mean:.4f} \nStd dev {std:.4f}'
    img_path = f'img/{label}.png'

    plt.hist(x=x, bins=bins, histtype='step', label=hist_desc)
    plt.title(label)
    plt.ylabel('Counts')
    plt.legend(loc='best')
    plt.savefig(img_path)
    plt.show()