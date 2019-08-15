# machine_learning notebook

## sklearn
### 常用包
```python
from sklearn import datasets
from sklearn import svm
from joblib import dump, load
from sklearn.feature_selection import VarianceThreshold, SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
```
### 加载数据集
```python
iris = datasets.load_iris()
digits = datasets.load_digits()
```
### 特征工程以及数据集的选取
```python
X, y =iris.data, iris.target
sel = SelectKBest(chi2, k=3) # 针对分类型任务
X_sel = sel.fit_transform(X, y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
```
### learning and predicting
```python
'''
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
pre = clf.predict(digits.data[-1:])
'''
model = LogisticRegression()
model.fit(X_train, y_train)
pre = model.predict(X_test)
metric = accuracy_score(y_test, pre)
print('metric: ',metric)
```
### model persistence
```python
clf = svm.SVC(gamma='scale')
X, y = iris.data, iris.target
clf.fit(X, y)
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print(clf2.predict(X[0:1]))
print(y[0])
dump(clf, 'clf.joblib')
clf = load('clf.joblib')
```