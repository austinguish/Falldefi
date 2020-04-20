from get_data import get_all_data
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from joblib import dump, load
import numpy
all_data = get_all_data()
_all_data_x = []
_all_data_y = []
count = all_data.shape[0]
count1 = all_data.shape[1]


for i in range(0, count):
    _all_data_x.append(all_data.iloc[i, 0:21])
    _all_data_y.append(all_data.iloc[i, 21:22])




X_train, X_test, y_train, y_test = train_test_split(_all_data_x, _all_data_y, test_size=0.4, random_state=24)
test_count = len(X_test)
clf = svm.SVC(gamma='scale')
clf.fit(X_train, y_train)
print(test_count)
dump(clf, 'falldefi-1.1.joblib')#保存模型
#测试
all_data = get_all_data()
_all_data_x = []
_all_data_y = []
count = all_data.shape[0]
count1 = all_data.shape[1]

for i in range(0, count):
    _all_data_x.append(all_data.iloc[i, 0:21])
    _all_data_y.append(all_data.iloc[i, 21:22])
numpy.ravel(_all_data_y)



clf_load = load('falldefi-1.1.joblib')
X_train, X_test, y_train, y_test = train_test_split(_all_data_x, _all_data_y, test_size=0.4, random_state=24)
y_predict = clf_load.predict(X_train)
print(y_predict)
score = roc_auc_score(y_train, y_predict)
print(score)
