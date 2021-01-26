from utilities import prepare_set, high_score, save_result, get_Xy

from time import time

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class SVC_classifier:
    def __init__(self, with_PCA=True):
        self.value_param_small = [0.01, 0.1, 1.0]
        self.value_param_big = [10, 100, 1000]
        self.class_weight = [None, 'balanced']

        if with_PCA:
            self.pipe = make_pipeline(StandardScaler(), PCA(n_components=3), SVC())
        else:
            self.pipe = make_pipeline(StandardScaler(), SVC())

        self.param_grid = [{'svc__C': self.value_param_big,
                  'svc__gamma': self.value_param_small,
                  'svc__class_weight': self.class_weight}]

        self.svc_gs = GridSearchCV(estimator=self.pipe, 
                       param_grid=self.param_grid, scoring='balanced_accuracy', 
                       cv=10, n_jobs=-1)

    def fit(self, X, y):
        start_time = time()

        self.svc_gs = self.svc_gs.fit(X, y)

        self.training_time = time() - start_time
        self.best_params = self.svc_gs.best_params_

    def calc_efficiency(self, X, y):
        self.score = high_score(self.svc_gs, X, y)

    def get_params(self):
        return self.training_time, self.score, self.best_params