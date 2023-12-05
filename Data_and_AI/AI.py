import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Preprocessing import FeatureExtract
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
# from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier

from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score

models = [
    # LogisticRegression(),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    SVC(),
    KNeighborsClassifier(),
    GaussianNB(),
    LinearDiscriminantAnalysis(),
    # MLPClassifier(),
    AdaBoostClassifier(),
    GradientBoostingClassifier(),
    # XGBClassifier(),
    # LGBMClassifier()
]
y = np.loadtxt("Data/Subject_1_nhammat.txt")
y1 = np.loadtxt("Data/Subject_1_momat.txt")
y2 = np.loadtxt("Data/Subject_1.txt")

df = pd.DataFrame.from_dict(FeatureExtract(y))
df1 = pd.DataFrame.from_dict(FeatureExtract(y1))
df2 = pd.DataFrame.from_dict(FeatureExtract(y2))

X = pd.concat([df, df1]).values
X1 = df2.values
# 0 la nham mat, 1 la mo mat, 2 la tap trung
y = pd.concat([pd.Series([0] * len(df)), pd.Series([1] * len(df1))]).values

# EDA data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
results = []
for model in models:
    model.fit(X_train, y_train)
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    k = 5
    kf = KFold(n_splits=k)
    accuracy_list = []
    for train_index, test_index in kf.split(X):
        # Split data into training and testing sets
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_list.append(accuracy)
    avg_accuracy = np.mean(accuracy_list)
    results.append((type(model).__name__, train_score, test_score, avg_accuracy))
    print(model.predict(df2.values))
    plt.plot(model.predict(X1))
    plt.show()

res = pd.DataFrame(results, columns=['Model', 'Train Accuracy', 'Test Accuracy', 'K fold Accuracy'])
print(res)

# print("Test score: ", score)
# filename = 'test.h5'
# pickle.dump(model, open(filename, 'wb'))
# loaded_model = pickle.load(open(filename, 'rb'))
# print(model.predict(X_test))

