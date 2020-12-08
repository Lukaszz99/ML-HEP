#!/usr/bin/env python3

import ROOT as root
import numpy as np

import matplotlib.pyplot as plt

def load_root(filename):
    '''Loads a TTree model from ROOT. Returns file (ROOT.TFile) and list of objects.'''
    print(f'Loading file {filename} ...')

    file = root.TFile(filename, option='READ')

    # list of objects in root file
    objects = [key.GetName() for key in file.GetListOfKeys() if key.GetClassName() == 'TNtuple']

    return file, objects

def root_tree2array(root_file, tree_name):
    '''Converts TTree from ROOT.TFile to python array with separate labels. 
    The conversion of the TTree to a numpy array is implemented with multi-thread support. 
    About 2 times faster on I5-7200U with D0_Signal_MonteCarlo.root file.'''
    root.ROOT.EnableImplicitMT()

    tree = root_file.Get(tree_name) #Get TTree from TFile

    array, labels = tree.AsMatrix(return_labels=True)

    return array, labels 

def label_position(list, name):
    '''Returns an index of the requested label in a list.'''
    return list.index(name)

def make_hist(x, bins, title, x_label='', weights=None, x_min=None, x_max=None):
    '''Making histogram using matplotlib.'''
    hist_desc = f'Entries {format(x.shape[0], ".2e")}\
         \nMean {np.mean(x):.4f} \nStd dev {np.std(x):.4f}'
    img_path = f'img/{title}.png'

    plt.hist(x=x, bins=bins, histtype='step', label=hist_desc)

    if not x_min == None:
        plt.autoscale(enable=False, axis='x')
        plt.xlim((x_min, x_max))

    plt.title(title)
    plt.ylabel('Counts')
    plt.xlabel(x_label)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig(img_path)
    plt.show()