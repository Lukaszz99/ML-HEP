from custom_fnk import label_position, load_npy
import numpy as np
import sys
import getopt

import matplotlib.pyplot as plt


#inputfile = 'D0_Signal_MonteCarlo_1_2.npy'

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


    array, labels = load_npy(inputfile)

    source = input("Is it Signal or Background? [S/B]\n").lower()
    if source != 's' and source != 'b':
        print("arguments are S or B...")
        sys.exit(3)

    hist2d(array, labels, source)


def hist2d(array, labels, source='s'):

    if source == 's':
        source = 'Signal'
        weights = array[:, labels.index('w')] * array[:, labels.index('matchHftWeight')]
    if source == 'b':
        source = 'Background'
        weights = [1 for i in array]


    idx_m = label_position(labels, 'm')
    idx_pt = label_position(labels, 'pt')
    idx_decayLength = label_position(labels, 'decayLength')
    idx_dca12 = label_position(labels, 'dca12')
    idx_dcaV0ToPv = label_position(labels, 'dcaV0ToPv')
    idx_ptPion = label_position(labels, 'ptPion')
    idx_dcaPion = label_position(labels, 'dcaPion')
    idx_ptKaon = label_position(labels, 'ptKaon')
    idx_dcaKaon = label_position(labels, 'dcaKaon')


    make_hist_2d(array[:, idx_m], array[:, idx_pt], weights, source, 'm', 'pt')
    make_hist_2d(array[:, idx_pt], array[:, idx_decayLength], weights, source, 'pt', 'decayLength')
    make_hist_2d(array[:, idx_pt], array[:, idx_dcaV0ToPv], weights, source, 'pt', 'dcaV0ToPv')
    make_hist_2d(array[:, idx_dcaV0ToPv], array[:, idx_ptPion], weights, source, 'dcaV0ToPv', 'ptPion')
    make_hist_2d(array[:, idx_dcaV0ToPv], array[:, idx_ptKaon], weights, source, 'dcaV0ToPv', 'ptKaon')
    make_hist_2d(array[:, idx_pt], array[:, idx_dca12], weights, source, 'pt', 'dca12')
    make_hist_2d(array[:, idx_pt], array[:, idx_ptPion], weights, source, 'pt', 'ptPion')
    make_hist_2d(array[:, idx_pt], array[:, idx_ptKaon], weights, source, 'pt', 'ptKaon')
    make_hist_2d(array[:, idx_ptPion], array[:, idx_ptKaon], weights, source, 'ptPion', 'ptKaon')


def make_hist_2d(x, y, weights, source, x_label='', y_label=''):
    # clear plt buffer
    plt.clf()

    title = f'{source}_{x_label}_vs_{y_label}'

    plt.hist2d(x, y, bins=150, weights=weights)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.colorbar().set_label('Counts')

    # zeby nic nie ucieło
    plt.tight_layout()

    img_path = f'../img/hist2d/{title}'

    plt.savefig(img_path)
    #plt.show()



if __name__ == '__main__':
    main(sys.argv[1:])