from sklearn import datasets
import matplotlib.pyplot as pt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
s = datasets.load_iris()

a = s.data
b = s.target
target_names = s.target_names
da = LinearDiscriminantAnalysis(n_components=2)
X = da.fit(a, b).transform(a)
c = ['blue', 'red', 'black']
for color, k, target_name in zip(c, [0, 1, 2], target_names):
    pt.scatter(X[b == k, 0], X[b == k, 1], alpha=.5, color=color,
                label=target_name)
pt.title('Linear Discriminatant Analysis of IRIS dataset')
pt.legend(loc='best', shadow=False, scatterpoints=1)
pt.show()