import sys, getopt
import numpy as np
#import ROOT as root
from custom_fnk import load_root, root_tree2array, label_position


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'i:o:l:h:')
    except getopt.GetoptError:
        print('Error...')
        sys.exit(2)

    if len(opts) != 4:
        print(f'I need 4 arguments: in and out file, min and max pt value. Got only {len(opts)}...')
        sys.exit(1)

    for opt, arg in opts:
        if opt in '-i':
            inputfile = arg
        if opt in '-o':
            outputfile = arg
        if opt in '-l':
            min_pt = int(arg)
        if opt in '-h':
            max_pt = int(arg)

    root_file, root_objects = load_root(inputfile)

    print('Type object to read', root_objects)
    tree_name = input()

    if not tree_name in root_objects:
        print('Wrong value! Abroting...')
        sys.exit(3)

    array, labels = root_tree2array(root_file, tree_name)
    print('Loaded')
    pt_index = label_position(labels, 'pt')
    array = array[(array[:, pt_index] > min_pt) & (array[:, pt_index] < max_pt)]


    out_array = np.vstack((np.asarray(labels, object), array))
    np.save(outputfile, out_array)
    print('Saved')

    del out_array, array, labels, root_file, root_objects

if __name__ == '__main__':
    main(sys.argv[1:])