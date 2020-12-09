#!/usr/bin/env python3
import numpy as np
import sys, getopt
import time

from custom_fnk import make_hist, label_position


def make_hist_signal(array, labels):
    '''It requires output_folder directory to work!!!'''
    weightArray = array[:, label_position(labels, 'matchHftWeight')] # None or array (depends whether you want weights included)
    output_dir = 'img_with_weights/'
    make_hist(array[:, label_position(labels, 'm')], 220, 'Signal_mass_pt12', 'mass [GeV / c^2]', 1.862, 1.866, weights=weightArray, output_folder=output_dir)
    make_hist(array[:, label_position(labels, 'pt')], 150, 'Signal_pt_12', 'pt [GeV]', weights=weightArray, output_folder=output_dir)
    make_hist(array[:, label_position(labels, 'decayLength')], 150, 'Signal_decayLength_pt_12', 'pt [GeV]', weights=weightArray, output_folder=output_dir)
    make_hist(array[:, label_position(labels, 'dca12')], 150, 'Signal_dca12_pt_12', weights=weightArray, output_folder=output_dir)
    
    make_hist(array[:, label_position(labels, 'ptKaon')], 150, 'Signal_ptKaon_pt_12', weights=weightArray, output_folder=output_dir)
    make_hist(array[:, label_position(labels, 'dcaKaon')], 150, 'Signal_dcaKaon_pt_12', weights=weightArray, output_folder=output_dir)

    make_hist(array[:, label_position(labels, 'ptPion')], 150, 'Signal_ptPion_pt_12', weights=weightArray, output_folder=output_dir)
    make_hist(array[:, label_position(labels, 'dcaPion')], 150, 'Signal_dcaPion_pt_12', weights=weightArray, output_folder=output_dir)

def make_hist_background(array, labels):
    '''It requires output_folder directory to work!!!'''
    output_dir = 'img/'
    make_hist(array[:, label_position(labels, 'm')], 220, 'Background_mass_pt12', 'mass [GeV / c^2]', 1.862, 1.866, output_folder=output_dir)
    make_hist(array[:, label_position(labels, 'pt')], 150, 'Background_pt_12', 'pt [GeV]', output_folder=output_dir)
    make_hist(array[:, label_position(labels, 'decayLength')], 150, 'Background_decayLength_pt_12', 'pt [GeV]', output_folder=output_dir)
    make_hist(array[:, label_position(labels, 'dca12')], 150, 'Background_dca12_pt_12', output_folder=output_dir)
    
    make_hist(array[:, label_position(labels, 'ptKaon')], 150, 'Background_ptKaon_pt_12', output_folder=output_dir)
    make_hist(array[:, label_position(labels, 'dcaKaon')], 150, 'Background_dcaKaon_pt_12', output_folder=output_dir)

    make_hist(array[:, label_position(labels, 'ptPion')], 150, 'Background_ptPion_pt_12', output_folder=output_dir)
    make_hist(array[:, label_position(labels, 'dcaPion')], 150, 'Background_dcaPion_pt_12', output_folder=output_dir)
    

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'i:')
    except getopt.GetoptError:
        print('Error...')
        sys.exit(2)

    if len(opts) != 1:
        print(f'I need 1 argument in format ./[program_name] -i <input_file.npy>')
        sys.exit(1)

    for opt, arg in opts:
        if opt in '-i':
            inputfile = arg
        
    start = time.time()
    x = input("Is it Signal or Background? [S/B]\n").lower()
    if x != 's' and x != 'b':
        print("arguments are S or B...")
        sys.exit(3)
    array = np.load(inputfile, allow_pickle=True)

    labels = list(array[:1].astype(str)[0])
    array = array[1:].astype('float64')
    print(f'Loaded in {time.time() - start:.2f}s')

    
    if x == 's':
        make_hist_signal(array, labels)
    elif x == 'b':
        make_hist_background(array,labels)


if __name__ == '__main__':
    main(sys.argv[1:])