import numpy as np

def load_npy(inputfile):
    file_npy = np.load(inputfile, allow_pickle=True)
    
    # oddzielenie labels
    file_labels = list(file_npy[:1].astype(str)[0])

    # oddzielenie danych i zmiana formatu z objet na float64
    file_npy = file_npy[1:].astype('float64')

    return file_npy, file_labels

def prepare_set():
    npy, labels = load_npy('../data/D0_set.npy')

    # przyogowanie danych do trenowania i testu
    np.random.shuffle(npy)
    
    weights = npy[:, -2]

    train_weights = weights[:50000]
    test_weights = weights[50000:60000]

    npy = np.delete(npy, -2, axis=1)
    
    labels = labels[:9] + [labels[-1]]
    
    targets = npy[:, -1]
    
    X_train = npy[:50000, :-1]
    y_train = targets[:50000]
    
    X_test = npy[50000:60000, :-1]
    y_test = targets[50000:60000]
    
    return X_train, y_train, X_test, y_test, train_weights, test_weights