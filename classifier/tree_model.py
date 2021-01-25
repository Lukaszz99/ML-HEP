from utilities import prepare_set, high_score, save_result, get_Xy

from time import time

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier

class Decision_tree:
    def __init__(self):
        self.max_depth = [None, 10, 50, 100]
        self.class_weight = [None, 'balanced']

        self.tree_pipe = DecisionTreeClassifier()

        self.param_grid = [{'max_depth':self.max_depth,
                  'class_weight':self.class_weight}]

        self.tree_gs = GridSearchCV(estimator=self.tree_pipe, 
                       param_grid=self.param_grid, scoring='balanced_accuracy', 
                       cv=10, n_jobs=-1)

    def fit(self, X, y):
        start_time = time()

        self.tree_gs = self.tree_gs.fit(X, y)

        self.training_time = time() - start_time
        self.best_params = self.tree_gs.best_params_

    def calc_efficiency(self, X, y):
        self.score = high_score(self.tree_gs, X, y)

    def get_params(self):
        return self.training_time, self.score, self.best_params