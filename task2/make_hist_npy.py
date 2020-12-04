import numpy as np
import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'i:')
    except getopt.GetoptError:
        print('Error...')
        sys.exit(2)

    if len(opts) != 1:
        print(f'I need 1 arguments only')
        sys.exit(1)

    for opt, arg in opts:
        if opt in '-i':
            inputfile = arg

    array = np.load(inputfile, allow_pickle=True)
    print('Loaded')

    labels = array[:1].astype(str)
    array = array[1:].astype('float64')


    print(array[:50])
    print(array.shape)

if __name__ == '__main__':
    main(sys.argv[1:])