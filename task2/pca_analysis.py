from sklearn.preprocessing import StandardScaler as SC
from sklearn.decomposition import PCA
import sys, getopt
import numpy as np


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


    # array jest teraz ustandaryzowany (mean=0, std=1)
    array = SC().fit_transform(array)

    # chcemy zachowac oryginalna wymiarowosc zbioru (liczbe kolumn)
    pca = PCA(n_components=array.shape[1])

    pca.fit(array)

    print(pca.explained_variance_ratio_)
    #print(pca.explained_variance_)
    #print(pca.singular_values_)
    print('\n')

    for i in range(pca.components_.shape[0]):
        print(abs(pca.components_[i]))

    print(labels[4])



if __name__ == '__main__':
    main(sys.argv[1:])