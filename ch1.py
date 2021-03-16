#合成数据
from sklearn import datasets
X, y =  datasets.make_classfication(n_samples = 10**6, n_features = 10, random_state = 101)
print(X.shape, y.shape)

