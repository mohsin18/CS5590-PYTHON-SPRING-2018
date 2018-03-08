from sklearn import datasets,metrics
from sklearn import svm
from sklearn.model_selection import train_test_split

s=datasets.load_iris()
a=s.data
b=s.target
a_train,a_test,b_train,b_test=train_test_split(a,b,test_size=0.20)
model_linear=svm.SVC(kernel='linear')
b_predict = model_linear.fit(a_train,b_train).predict(a_test)
print(' Linear Kernel ',(model_linear.score(a,b)))
print('\n','Linear Kernel accuracy ', metrics.accuracy_score(b_test,b_predict))
d=svm.SVC(kernel='rbf')
b_rbf = d.fit(a_train,b_train).predict(a_test)
print('\n','rbf kernel ',(d.score(a,b)))
print('\n','rbf kernel accuracy: ', metrics.accuracy_score(b_test,b_rbf))