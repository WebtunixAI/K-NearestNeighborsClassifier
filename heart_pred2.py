# importing libraries pandas and kneighborsclassifier
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# reading csv file and taking class unique
df = pd.read_csv('heart_stalog.csv')
df['class'].unique()

# label encoder for making string data into binary form(0,1)
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
df['class'] = label_encoder.fit_transform(df['class'])

# print encoded data in new csv
df.to_csv("new.csv", index=None)

x = df.iloc[:, 4:13]
y = df.iloc[:, -1]

# split data in train test
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# implementing kneighborsclassifier for prediction(0=absent,1=present)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)
prc = model.predict(x_test)
print(prc)

# finding accuracy
from sklearn import metrics

print("accuracy:", metrics.accuracy_score(y_test, prc))
