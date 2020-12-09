import sys, getopt
import numpy as np
import time
from custom_fnk import load_root, root_tree2array, label_position


def main(argv):
    
    inputfile, outputfile, min_pt, max_pt = error_checker(argv)

    start_time = time.time()

    # load root file typed in argv
    root_file, root_objects = load_root(inputfile)

    # select tree to read
    print('Type object to read', root_objects)
    tree_name = input()

    if not tree_name in root_objects:
        print('Wrong value! Abroting...')
        sys.exit(4)

    # transform .root file to numpy.array
    print('Tree loaded. Transforming to array....')
    array, labels = root_tree2array(root_file, tree_name)

    # select rows with min_pt < pt < max_pt
    pt_index = label_position(labels, 'pt')
    array = array[(array[:, pt_index] > min_pt) & (array[:, pt_index] < max_pt)]

    # glue labels with data in one array and save it
    # while reading change dtype of first row to str and others to float64
    out_array = np.vstack((np.asarray(labels, object), array))
    np.save(outputfile, out_array)
    print(f'Saved array with specifed pt range in file {outputfile}.npy. Time {time.time() - start_time:.2f}s.')

    del out_array, array, labels, root_file, root_objects


def error_checker(argv):
    """Check if argv is correct and return parsed in/out file and min, max pt using getopt (C-style parser for cmd).
       Argv should be in following order: -i <inputfile> -o <outputfile> -l <min_pt> -h <max_pt>"""
    try:
        opts, args = getopt.getopt(argv, 'i:o:l:h:')
    except getopt.GetoptError:
        print('Error...')
        sys.exit(1)

    if len(opts) != 4:
        print(f'I need 4 arguments: \n-i <inputfile> -o <outputfile> -l <min_pt> -h <max_pt>. \nGot only {len(opts)}...')
        sys.exit(2)

    for opt, arg in opts:
        if opt in '-i':
            inputfile = arg
        if opt in '-o':
            outputfile = arg
        if opt in '-l':
            min_pt = int(arg)
        if opt in '-h':
            max_pt = int(arg)

    if min_pt >= max_pt:
        print('min_pt must be lower than max_pt! Aborting...')
        sys.exit(3)

    return inputfile, outputfile, min_pt, max_pt


if __name__ == '__main__':
    main(sys.argv[1:])