from utilities import prepare_set, high_score, save_result, get_Xy

from tree_model import Decision_tree
from svc_model import SVC_classifier
from lr import LR

from datetime import datetime

def test_clf(model, learning_samples, testing_samples, SB_big_ratio, with_PCA):
    X_train, y_train, X_test, y_test = get_Xy(learning_samples, testing_samples, SB_big_ratio)

    clf = model
    clf.fit(X_train, y_train)
    clf.calc_efficiency(X_test, y_test)

    # time, score, params
    return clf.get_params()

if __name__ == "__main__":
    # True to wtedy jest 1:350 sygnal do tla, jak False to 1:2
    SB_big_ratio = False

    # Dla SB_big_ratio True:
    # Max learning = 100 000, testing = 11 000
    #
    # Dla SB_big_ratio False:
    # Max learning = 60 000, testing = 7 000

    learning_samples = 500
    testing_samples = 1000

    # czy algorytm (oprocz DecisionTree) ma uzyc PCA czy nie
    with_PCA = True

    clfs = [Decision_tree(), SVC_classifier(), LR()]

    # TUTAJ USTAW, JAKI MODEL DO SYMULACJI
    model = clfs[0]

    time, score, params = test_clf(model, learning_samples, testing_samples, 
                SB_big_ratio, with_PCA)

    if SB_big_ratio:
        ratio = '1:350'
    else:
        ratio = '1:2'

    text_to_save = f'Time {datetime.now()} \nModel {model} \nSB ratio {ratio} \nPCA {with_PCA} \nTraining time: {time}s \nEfficiency: {score} \nBest params: {params}\n'
    
    print(text_to_save)

    if model == clfs[0]:
        model_str = 'decision_tree'
    if model == clfs[1]:
        model_str = 'svc'
    if model == clfs[2]:
        model_str = 'lr'
    save_result(model_str, text_to_save)