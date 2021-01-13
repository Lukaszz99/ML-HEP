import numpy as np

def load_npy(inputfile):
    file_npy = np.load(inputfile, allow_pickle=True)
    
    # oddzielenie labels
    file_labels = list(file_npy[:1].astype(str)[0])

    # oddzielenie danych i zmiana formatu z objet na float64
    file_npy = file_npy[1:].astype('float64')

    return file_npy, file_labels

def prepare_set(filename):
    npy, labels = load_npy(filename)

    # przyogowanie danych do trenowania i testu
    np.random.shuffle(npy)
    
    weights = npy[:, -2]

    set_size = npy.shape[0]

    rng = int(0.9 * set_size)

    train_weights = weights[:rng]
    test_weights = weights[rng:set_size]

    npy = np.delete(npy, -2, axis=1)
    
    labels = labels[:9] + [labels[-1]]
    
    targets = npy[:, -1]
    
    X_train = npy[:rng, :-1]
    y_train = targets[:rng]
    
    X_test = npy[rng:set_size, :-1]
    y_test = targets[rng:set_size]
    
    return X_train, y_train, X_test, y_test, train_weights, test_weights

