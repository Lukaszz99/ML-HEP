from sklearn.preprocessing import StandardScaler as SC
from sklearn.decomposition import PCA
import sys, getopt
import numpy as np
import gc


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

    # zmienne które chcemy badać
    features = ['m', 'pt', 'decayLength', 'dca12', 'dcaV0ToPv', 'ptKaon', 'dcaKaon', 'ptPion', 'dcaPion']

    array = np.load(inputfile, allow_pickle=True)

    labels = list(array[:1].astype(str)[0])
    array = array[1:].astype('float64')

    # lista indeksów, pod ktorymi sa interesujace zmienne
    feat_idxs = [labels.index(feat) for feat in features]

    # array jest teraz ustandaryzowany (mean=0, std=1) oraz zawiera tylko intersujace zmienne
    array = SC().fit_transform(array[:, feat_idxs])
    print(np.max(array[:, 4]))
    print(np.min(array[:, 4]))
    print(np.mean(array[:, 4]))
    print(np.std(array[:, 4]))
    # chcemy zachowac oryginalna wymiarowosc zbioru (liczbe kolumn)
    """pca = PCA(n_components=array.shape[1])

    pca.fit(array)

    print(pca.explained_variance_ratio_)

    feature_importance = []
    for i in range(pca.explained_variance_ratio_.shape[0]):
        feat_sum = 0

        for j in range(pca.components_.shape[0]):
            feat_sum += abs(pca.components_[j][i]) * pca.explained_variance_ratio_[j]


        feature_importance.append(feat_sum)

   
    feature_importance = [i / np.sum(feature_importance) for i in feature_importance]

    analysis_output = []
    for i in range(len(features)):
        analysis_output.append(f'{features[i]}: {feature_importance[i]}\n')"""


    # zapisz do pliku txt wynik analizy
    #f = open(f'{inputfile[:-4]}_pca.txt', 'w+')
    #f.write(f'File: {inputfile}\n')
    #f.write('Features with importance\n')
    #f.writelines(analysis_output)
    #f.close()


    # run Garbage collector
    gc.collect()

if __name__ == '__main__':
    main(sys.argv[1:])