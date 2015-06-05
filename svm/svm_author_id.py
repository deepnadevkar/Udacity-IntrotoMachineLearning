#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score
from collections import Counter


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#clf = svm.SVC(kernel='linear')
clf = svm.SVC(kernel='rbf', C = 10000.0)#play around with different values of C (e.g., 10.0 (aacuracy = 0.616), 100.0 (aacuracy = 0.616), 100.0 (aacuracy = 0.821), 10000.0 (aacuracy = 0.892))

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

print accuracy_score(labels_test, pred)

answer_10 = pred[10]
answer_26 = pred[26]
answer_50 = pred[50]

print answer_10
print answer_26
print answer_50

print Counter(pred)

#########################################################


