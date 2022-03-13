# -*- coding: utf-8 -*-
"""GUI Model_ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oTND59X7dOb872pP1kZJtyiSVzhn3l2i
"""

# all necessary imports
import warnings
from decimal import Decimal
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
# ignore warnings generated due to usage of old version of tensorflow
warnings.simplefilter("ignore")

from google.colab import drive

drive.mount('/content/drive')

df = pd.read_csv("/content/drive/My Drive/Final Year Project/Dataset/dis_sym_dataset_comb.csv")

# creation of features and label for training the models
X = df.iloc[:, 1:]
Y = df.iloc[:, 0:1]

X.head()

Y.head()

# splitting data for training the classifiers and testing
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.10)

# LR Classifier
lr = LogisticRegression()
lr = lr.fit(X, Y)

# prediction of labels for the test data
lr_pred = lr.predict(x_test)
acc_lr = round(Decimal(accuracy_score(y_test, lr_pred) * 100), 2)

print(f"Accuracy (LR) : {acc_lr}%")

