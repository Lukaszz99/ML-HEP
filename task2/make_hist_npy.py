#!/usr/bin/env python3
import numpy as np
import sys, getopt
import time

from custom_fnk import make_hist, label_position #make_hist_weight


def make_hist_signal(array, labels):
    '''It requires img/ directory to work!!!'''
    make_hist(array[:, label_position(labels, 'm')], 22, 'Signal_mass_pt12', 'mass [GeV / c^2]', 1.862, 1.866)
    make_hist(array[:, label_position(labels, 'pt')], 150, 'Signal_pt_12', 'pt [GeV]')
    make_hist(array[:, label_position(labels, 'decayLength')], 150, 'Signal_decayLength_pt_12', 'pt [GeV]')
    make_hist(array[:, label_position(labels, 'dca12')], 150, 'Signal_dca12_pt_12')

    make_hist(array[:, label_position(labels, 'ptKaon')], 150, 'Signal_ptKaon_pt_12')
    make_hist(array[:, label_position(labels, 'dcaKaon')], 150, 'Signal_dcaKaon_pt_12')

    make_hist(array[:, label_position(labels, 'ptPion')], 150, 'Signal_ptPion_pt_12')
    make_hist(array[:, label_position(labels, 'dcaPion')], 150, 'Signal_dcaPion_pt_12')


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'i:')
    except getopt.GetoptError:
        print('Error...')
        sys.exit(2)

    if len(opts) != 1:
        print(f'I need 1 argument only in format ./[program_name] -i <input_file.npy>')
        sys.exit(1)

    for opt, arg in opts:
        if opt in '-i':
            inputfile = arg
        
    start = time.time()

    array = np.load(inputfile, allow_pickle=True)

    labels = list(array[:1].astype(str)[0])
    array = array[1:].astype('float64')
    print(f'Loaded in {time.time() - start:.2f}s')

    make_hist_signal(array, labels)

    #make_hist_signal_weight(array, labels)



if __name__ == '__main__':
    main(sys.argv[1:])