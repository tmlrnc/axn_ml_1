from sklearn.tree import DecisionTreeClassifier
from ohe.predictor import OneHotPredictor, Commandline
from ohe.config import get_ohe_config

@Commandline("DTC")
class DTC_OHP(OneHotPredictor):

    def __init__(self, target, X_test, X_train, y_test, y_train):
        super().__init__(target, X_test, X_train, y_test, y_train)
        self.model_name = 'Decision Tree Classifier'

    def predict(self):
        algorithm = DecisionTreeClassifier(random_state=get_ohe_config().DTC_random_state)
        algorithm.fit(self.X_train, self.y_train)
        y_pred = list(algorithm.predict(self.X_test))
        self.acc = OneHotPredictor.get_accuracy(y_pred, self.y_test)
        return self.acc