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
X, y = iris.data, iris.target
# 根据多方面的评估选择最好的 k 个特征
sel = SelectKBest(chi2, k=3) # 针对分类型任务
X_sel = sel.fit_transform(X, y)
# 随机分离训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
```
* 非数字列处理
    `data_train.loc[data_train["Sex"] == "male","Sex"] = 0` # 将满足某个条件的元素重新赋值

#### 训练集和测试集的选取
* 留出法
    `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)`
* k 折交叉验证
```python
from sklearn import model_selection
#逻辑回归
from sklearn.linear_model import LogisticRegression   
#初始化逻辑回归算法
LogRegAlg=LogisticRegression(random_state=1)
re = LogRegAlg.fit(data_train[predictors],data_train["Survived"])
#使用sklearn库里面的交叉验证函数获取预测准确率分数
scores = model_selection.cross_val_score(LogRegAlg,data_train[predictors],data_train["Survived"],cv=3)
#使用交叉验证分数的平均值作为最终的准确率
print("准确率为: ",scores.mean())
```

#### 数据处理
* 如果某列存在大量的空值, 并且对结果的判断关系不大的话, 可以删去
* 如果某一列对结果的判断挺重要的, 可以选择平均值填充或者出现频率最多的值填充或者最大值进行填充
    `data_train["Age"] = data_train['Age'].fillna(data_train['Age'].median())`
    `data_test["Fare"] = data_test["Fare"].fillna(data_test["Fare"].max())`
* 如果某列即使不存在大量空值, 例如 id, 但与结果完全没有关系, 可以删去
* 虚拟化变量
    `X = pd.get_dummies(X) # 将所有的分类型特征转换为数字, 虚拟变量: dummy variables`

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

#### 随机森林
```python
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
predictors=["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]
#10棵决策树，停止的条件：样本个数为2，叶子节点个数为1
alg=RandomForestClassifier(random_state=1,n_estimators=10,min_samples_split=2,min_samples_leaf=1) 
#Compute the accuracy score for all the cross validation folds.  (much simpler than what we did before!)
#kf=cross_validation.KFold(data_train.shape[0],n_folds=3,random_state=1)
kf=model_selection.KFold(n_splits=3,shuffle=False, random_state=1)
scores=model_selection.cross_val_score(alg,data_train[predictors],data_train["Survived"],cv=kf)
print(scores)
#Take the mean of the scores (because we have one for each fold)
print(scores.mean())
```

#### Lasso
```python
from sklearn import linear_model
reg = linear_model.Lasso(alpha=0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])  
reg.predict([[1, 1]])
array([0.8])
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