
from predict.predictor import OneHotPredictor, Commandline
from predict.config import get_ohe_config


from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler

@Commandline("RANDOMFORRESTREGMAX")
class RandomForestRegression_OHP(OneHotPredictor):

    def __init__(self, target, X_test, X_train, y_test, y_train):
        """
        initializes the training and testing features and labels

        :param target: string - label to be predicted or classified
        :param X_test: array(float) - testing features
        :param X_train: array(float) - training features
        :param y_test: array(float) - testing label
        :param y_train: array(float) - testing label
        """
        super().__init__(target, X_test, X_train, y_test, y_train)
        self.model_name = 'RANDOMFORRESTREGMAX'

    def predict(self):
        """
        trains the scikit-learn  python machine learning algorithm library function
        https://scikit-learn.org

        then passes the trained algorithm the features set and returns the
        predicted y test values form, the function

        then compares the y_test values from scikit-learn predicted to
        y_test values passed in

        then returns the accuracy
        """
        algorithm = RandomForestRegressor(n_estimators=get_ohe_config().r_n_estimators,
                                        max_depth=get_ohe_config().RFR_max_depth,max_features='sqrt')
        algorithm.fit(self.X_train, self.y_train)
        y_pred = list(algorithm.predict(self.X_test))
        self.acc = OneHotPredictor.get_accuracy(y_pred, self.y_test)
        return self.acc