import numpy as np

def load_npy(inputfile):
    file_npy = np.load(inputfile, allow_pickle=True)
    
    # oddzielenie labels
    file_labels = list(file_npy[:1].astype(str)[0])

    # oddzielenie danych i zmiana formatu z objet na float64
    file_npy = file_npy[1:].astype('float64')

    return file_npy, file_labels

def prepare_set(filename, sb_big_ratio=False):
    npy, labels = load_npy(filename)

    # if True, to podział jest 1:350 sygnał:tło, zamiast 1:2
    if sb_big_ratio:
        signal = npy[:200]
        background = npy[35000:105000]
        
        npy = np.vstack((signal, background))
        
    # przyogowanie danych do trenowania i testu
    np.random.shuffle(npy)

    weights = npy[:, -2]

    set_size = npy.shape[0]

    rng = int(0.9 * set_size)

    train_weights = weights[:rng]
    test_weights = weights[rng:set_size]

    npy = np.delete(npy, -2, axis=1)

    targets = npy[:, -1]

    X_train = npy[:rng, :-1]
    y_train = targets[:rng]

    X_test = npy[rng:set_size, :-1]
    y_test = targets[rng:set_size]

    return X_train, y_train, X_test, y_test

def get_Xy(learning_samples, testing_samples, sb_big_ratio=False):
    X_train, y_train, X_test, y_test = prepare_set('../data/D0_set_weighted.npy', sb_big_ratio)
    
    try:
        X_train = X_train[:learning_samples, 1:]
        y_train = y_train[:learning_samples]
    except IndexError:
        print(f'Wrong learning_samples value: {learning_samples}')

    try:
        X_test = X_test[:testing_samples, 1:]
        y_test = y_test[:testing_samples]
    except IndexError:
        print(f'Wrong testing_samples value: {testing_samples}')

    return X_train, y_train, X_test, y_test

def eff_signal(clf, X, y):
    '''How much of signal is classified as signal.'''
    test_count = 0
    fit_count = 0
    prediction = clf.predict(X)
    for i in range(len(y)):
        if y[i] == 1:
            test_count += 1
            if prediction[i] == 1:
                fit_count += 1

    return fit_count

def eff_background(clf, X, y):
    '''How much of background is classified as background.'''
    test_count = 0
    fit_count = 0
    prediction = clf.predict(X)
    for i in range(len(y)):
        if y[i] == 0:
            test_count += 1
            if prediction[i] == 0:
                fit_count += 1
    
    return (1 - fit_count / test_count) * test_count
    
def high_score(clf, X, y):
    '''Function for scoring argument in model optimization'''
    S = eff_signal(clf, X, y)
    B = eff_background(clf, X, y)
    return S/np.sqrt(S+B)

def save_result(model, text):
    path = f'{model}.txt'
    file = open(path, 'w+')

    file.write(text)
    file.close()