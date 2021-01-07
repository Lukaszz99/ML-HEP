#!/usr/bin/env python3

import ROOT as root
import numpy as np

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


def load_npy(inputfile):
    file_npy = np.load(inputfile, allow_pickle=True)
    
    # oddzielenie labels
    file_labels = list(file_npy[:1].astype(str)[0])

    # oddzielenie danych i zmiana formatu z objet na float64
    file_npy = file_npy[1:].astype('float64')

    return file_npy, file_labels