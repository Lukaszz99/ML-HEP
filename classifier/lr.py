from utilities import prepare_set, high_score, save_result, get_Xy

from time import time

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class LR:
    def __init__(self, with_PCA=True):
        self.value_param = [0.01, 0.1, 1.0, 10, 100, 1000]
        self.class_weight = [None, 'balanced']

        if with_PCA:
            self.pipe = make_pipeline(StandardScaler(), PCA(n_components=3), 
                    LogisticRegression(max_iter=200, n_jobs=-1))
        else:
            self.pipe = make_pipeline(StandardScaler(), 
            LogisticRegression(max_iter=200, n_jobs=-1))

        self.param_grid = [{'logisticregression__C': self.value_param,
                 'logisticregression__class_weight': self.class_weight,
                 'logisticregression__solver': ['saga', 'lbfgs']}]


        self.lr_gs = GridSearchCV(estimator=self.pipe, param_grid=self.param_grid, 
                scoring='balanced_accuracy', cv=10, n_jobs=-1)

    def fit(self, X, y):
        start_time = time()

        self.lr_gs = self.lr_gs.fit(X, y)

        self.training_time = time() - start_time
        self.best_params = self.lrgs.best_params_

    def calc_efficiency(self, X, y):
        self.score = high_score(self.lr_gs, X, y)

    def get_params(self):
        return self.training_time, self.score, self.best_params