from custom_fnk import make_hist_2d, label_position
import numpy as np
import sys
import getopt


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


    array = np.load(inputfile, allow_pickle=True)

    labels = list(array[:1].astype(str)[0])
    array = array[1:].astype('float64')

    source = input("Is it Signal or Background? [S/B]\n").lower()
    if source != 's' and source != 'b':
        print("arguments are S or B...")
        sys.exit(3)

    hist2d_signal(array, labels, source)

def hist2d_signal(array, labels, source='s'):

    if source == 's':
        source = 'Signal'
    if source == 'b':
        source = 'Background'


    idx_m = label_position(labels, 'm')
    idx_pt = label_position(labels, 'pt')
    idx_decayLength = label_position(labels, 'decayLength')
    idx_dca12 = label_position(labels, 'dca12')
    idx_dcaV0ToPv = label_position(labels, 'dcaV0ToPv')
    idx_ptPion = label_position(labels, 'ptPion')
    idx_dcaPion = label_position(labels, 'dcaPion')
    idx_ptKaon = label_position(labels, 'ptKaon')
    idx_dcaKaon = label_position(labels, 'dcaKaon')
    weightArray = array[:, label_position(labels, 'matchHftWeight')]

    make_hist_2d(array[:, idx_m], array[:, idx_pt],150, f'{source}_m_vs_pt', 'm', 'pt', weights=weightArray)
    make_hist_2d(array[:, idx_pt], array[:, idx_decayLength],150, f'{source}_pt_vs_decayLength', 'pt', 'decayLength', weights=weightArray,xy_lim=[[1,2],[0,.1]])
    make_hist_2d(array[:, idx_pt], array[:, idx_dcaV0ToPv],150, f'{source}_pt_vs_dcaV0ToPv', 'pt', 'dcaV0ToPv', weights=weightArray, xy_lim=[[1,2],[0,.02]])
    make_hist_2d(array[:, idx_dcaV0ToPv], array[:, idx_ptPion],150, f'{source}_dcaV0ToPv_vs_ptPion', 'dcaV0ToPv', 'ptPion', weights=weightArray, xy_lim=[[0,.02],[0,2.5]])
    make_hist_2d(array[:, idx_dcaV0ToPv], array[:, idx_ptKaon], 150, f'{source}_dcaV0ToPv_vs_ptKaon', 'dcaV0ToPv', 'ptKaon', weights=weightArray, xy_lim=[[0,.02],[0,2.5]])
    make_hist_2d(array[:, idx_pt], array[:, idx_dca12],200, f'{source}_pt_vs_dca12', 'pt', 'dca12', weights=weightArray)
    make_hist_2d(array[:, idx_pt], array[:, idx_ptPion],150, f'{source}_pt_vs_ptPion', 'pt', 'ptPion', weights=weightArray)
    make_hist_2d(array[:, idx_pt], array[:, idx_ptKaon],150, f'{source}_pt_vs_ptKaon', 'pt', 'ptKaon', weights=weightArray)
    make_hist_2d(array[:, idx_ptPion], array[:, idx_ptKaon],200, f'{source}_ptPion_vs_ptKaon', 'ptPion', 'ptKaon', weights=weightArray)


#[[0, 0.1],[0,2.5]]

if __name__ == '__main__':
    main(sys.argv[1:])