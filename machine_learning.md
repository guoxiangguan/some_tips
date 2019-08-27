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

## 常见算法

### 集成学习
* 根据个体学习器的生成方式, 目前的集成学习方法大致可分为两大类, 即个体学习器间存在强依赖关系, 必须串行生成的序列化方法, 以及个体学习器间不存在强依赖关系, 可同时生成的并行化的方法; 前者的代表是 Boosting, 后者的代表是 Bagging 和 "随机森林" (Random Forest)

#### Boosting
* Boosting 是一族可将弱学习器提升为强学习器的算法.
* 工作机制: 先从初始训练集训练出一个基学习器, 再根据基学习器的表现对训练样本分布进行调整, 使得先前基学习器做错的训练样本再后续受到更多关注, 然后基于调整后的样本分布来训练下一个基学习器; 如此反复进行, 直至基学习器数目达到事先指定的值 T, 最终将这 T 个基学习器进行加权结合.
* Boosting 族算法最著名的代表是 AdaBoost.
* Boosting 算法要求基学习器能对特定的数据分布进行学习, 这可通过 "重新赋权法" (re-weighting) 实施, 即在训练过程的每一轮中, 根据样本分布为每个训练样本重新赋予一个权重. 对无法接受带权样本的基学习算法, 则可以通过 "重采样法" (re-sampling) 来处理, 即在每一轮学习中, 根据样本分布对训练集重新进行采样, 再用重采样而得到的样本集对基学习器进行训练.
* 从偏差-方差分解的角度看, Boosting 主要关注降低偏差, 因此 Boosting 能基于泛化性能相当弱的学习器构建出很强的集成.


### 基于二次准则函数的 H-K 算法
* 基于二次准则函数的 H-K 算法较之于感知器算法的优点
    1. 可以判别问题是否线性可分
    2. 其解得适应性更好

### 感知器算法

### K-means 聚类算法
* K-means 聚类算法的特点
    1. 对大数据集有较高的效率并且具有可伸缩性
    2. 是一种无监督的学习方法
    3. k 值无法自动获取, 初始聚类中心随机选择

### PCA (主成分分析)
* 主要去做的事
    1. 可以找到相互独立的特征
        * 若先用 PCA, 再用朴素贝叶斯, 则效果比单独用朴素贝叶斯效果好很多.
    2. 降维
* 推导过程
    1. 先中心化数据
        - `A - np.mean(A)` (方便计算方差以求出数据的分布情况)
    2. 计算投影后的数据方差最大值


### EM 算法
#### 简介
* EM 算法称为期望最大值算法, 是无监督的算法, 通过逐步提高极大似然的下限, 以此求出极大似然函数对参数的估计, 为无监督算法.
* 是一种族算法(cluster algorithm)

### 路径搜索
* A* 算法, 俗称 A 星算法, 这是一种在图形平面上, 有多个节点的路径, 求出最低通过成本的算法.
    * 博客地址: [A星算法详解](https://blog.csdn.net/hitwhylz/article/details/23089415)
* Dijkstra
    * 使用广度优先搜索解决赋权有向图的单源最短路径问题

## 机器学习相关软件包

### SPASS
* SPASS 是统计产品与服务解决方案 (Statistical Product and Service Solutions) 的简称, 为 IBM 公司的一系列用于统计学习分析, 数据挖掘, 预测分析和决策支持任务的软件产品及相关服务的总称.
* SPASS 界面的主窗口为 *数据编辑窗口*

## 机器学习常识

### 可以用来降维的算法
1. Latent Dirichlet Allocation: 把文档投影到 "topic" 空间, 可以理解为降维.
2. word2vec: 在给定的语料库上训练一个模型, 输出出现在语料库中单词的向量 (word embedding) 表示, NLP 中传统的词表示方法是把每个单词表示成 dim (词汇量大小) 维的稀疏向量, 这个稀疏向量只有一个维度 (该单词的 index) 上是1, 其余全是0, 单词之间孤立, word embedding 则是把单词的表示降维到 n 维的稠密向量, n << dim.
3. PCA
4. 自编码: 隐藏层的神经元数目少于输入就可以看做降维和压缩.

### 偏差和方差
* 偏差: 描述的是预测值 (估计值) 的期望与真实值之间的差距. 偏差越大, 越偏离真实数据
* 方差: 描述的是预测值的变化范围, 离散程度, 也就是离其期望值的距离. 方差越大, 数据的分布越分散.

### 训练集
* 监督学习中的训练集用于估算模型

## 模型
* 生成式模型:
    * 判别式分析
    * 朴素贝叶斯
    - K 近邻
    - 混合高斯模型
    - 隐马尔科夫模型
    - 贝叶斯网络
    - Sigmoid Belief Networks
    - 马尔科夫随机场 (Markow Random Fields)
    - 深度信念网络(DBN)
- 判别式模型
    - 线性回归(Linear Regression)
    - Logistic Regression
    - 神经网络
    - 支持向量机
    - 高斯过程
    - 条件随机场(CRF)
    - CART(Classification and Regression Tree)
    - 最大熵

## CRF 模型和 HMM 以及 MEMM 模型之间的关系
1. CRF 没有 HMM 那样严格的独立性假设条件, 因此可以容纳任意的上下文信息. 与 ME 一样, 特征设计灵活. ---- 与 HMM 比较
2. 由于 CRF 计算全局最优输出节点的条件概率, 它还克服了最大熵马尔科夫模型标记偏置的缺点. ---- 与 MEMM 比较
3. CRF 是在给定需要标记的观察序列的条件下, 计算整个标记序列的联合概率分布, 而不是在给定当前状态条件下, 定义下一个状态的状态分布. ---- 与 ME 比较
4. 缺点: 训练代价大, 复杂度高.

## 隐马尔科夫模型

### 隐马尔科夫模型的三个基本问题以及相应的算法
1. 前向, 后向算法解决的是一个评估问题, 即给定一个模型, 求某特定观测序列的概率, 用于评估该序列最匹配的模型.
2. Baum-Welch 算法解决的是一个模型训练问题, 即参数估计, 是一种无监督的训练方法, 主要通过 EM 迭代实现.
3. 维特比算法 (Viterbi) 解决的是给定一个模型和某个特定的输出序列, 求最可能产生这个输出的状态序列. 如通过海藻变化 (输出序列) 来观测天气 (状态序列), 是预测问题, 通信中的解码问题.

### 应用
* 条件随机场和隐马尔科夫模型是典型的用来做序列标注问题的模型, 是构建语音识别声学模型的传统方法, RNN 因含有递归层而具有序列结构的特点, 现在被广泛用于语音识别等序列标注问题中.

### 文本分类中常用的特征选择方法
* 常采用特征选择方法。常见的六种特征选择方法：
    1. DF(Document Frequency) 文档频率
    DF:统计特征词出现的文档数量，用来衡量某个特征词的重要性
    2. MI(Mutual Information) 互信息法
    互信息法用于衡量特征词与文档类别直接的信息量。
    如果某个特征词的频率很低，那么互信息得分就会很大，因此互信息法倾向"低频"的特征词。
    相对的词频很高的词，得分就会变低，如果这词携带了很高的信息量，互信息法就会变得低效。
    3. (Information Gain) 信息增益法
    通过某个特征词的缺失与存在的两种情况下，语料中前后信息的增加，衡量某个特征词的重要性。
    4. CHI(Chi-square) 卡方检验法
    利用了统计学中的"假设检验"的基本思想：首先假设特征词与类别直接是不相关的
    如果利用CHI分布计算出的检验值偏离阈值越大，那么更有信心否定原假设，接受原假设的备则假设：特征词与类别有着很高的关联度。
    5. WLLR(Weighted Log Likelihood Ration)加权对数似然
    6. WFO（Weighted Frequency and Odds）加权频率和可能性

### 概率
* 全概率公式: P(X =1) = P(X = 1|Y = 1) * P(Y = 1) + P(X = 1|Y = 0) * P(Y = 0)

### 统计模式分类问题
* 当先验概率未知时，可以使用最小最大损失准则和N-P判决.
    最小损失准则中需要用到先验概率
    最大最小损失规则主要就是使用解决最小损失规则时先验概率未知或难以计算的问题的。
    在贝叶斯决策中，对于先验概率p(y)，分为已知和未知两种情况。 
    1. p(y)已知，直接使用贝叶斯公式求后验概率即可； 
    2. p(y)未知，可以使用聂曼-皮尔逊决策(N-P决策)来计算决策面。

### 有效解决过拟合的方法
1. 增加样本数量
2. 采用正则化的方法
* 增加特征数量和迭代更多的轮次不能有效解决过拟合

### 数据清理中, 处理缺失值的方法
1. 估算
2. 整例删除
3. 变量删除
4. 成对删除

### tanh
* tanh 的值域在 (-1,1)

### logistic regression
* 逻辑回归主要用于解决分类问题

### 从使用的主要技术上看，可以把分类方法归结为哪几种类型 
* 从使用技术上来分，可以分为四种类型：基于距离的分类方法、决策树分类方法、贝叶斯分类方法和规则归纳方法。基于距离的分类方法主要有最邻近方法；决策树方法有ID3、C4.5、VFDT等；贝叶斯方法包括朴素贝叶斯方法和EM算法；规则归纳方法包括AQ算法、CN2算法和FOIL算法。

### 一些降维方法
1. LASSO: 通过参数缩减达到降维的目的
2. PCA
3. 聚类分析
4. 小波分析: 有一些变换的操作降低干扰可以看做降维
5. 线性判别法: 通过找到一个空间使得类内距离最小, 类间距离最大
6. 拉普拉斯特征映射