import numpy as np
from sklearn import linear_model
X = np.array([[-1, -1] , [-2, -1], [1, 1], [2, 1]])
Y = np.array([1, 2, 3, 4])
clf = linear_model.SGDClassifier()
clf.partial_fit(X, Y,[1,2,3,4,5,6,7])
print(clf.predict([[3,2]]))
clf.partial_fit([[3,2]], [5])
print(clf.prt([[edict([[3,2]]))
print(clf.predic-1.1,-1]]))
