# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:39:36 2022

@author: etuba
"""

from keras.datasets import mnist
from matplotlib import pyplot, transforms
import random

# import MNIST digit dataset
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# print details about dataset
print('X_train: ' + str(train_X.shape))
print('Y_train: ' + str(train_y.shape))
print('X_test:  '  + str(test_X.shape))
print('Y_test:  '  + str(test_y.shape))

# show image examples
def showExamples(n=9):
    for i in range(n):  
        pyplot.subplot(330 + 1 + i)
        pyplot.imshow(train_X[i], cmap=pyplot.get_cmap('gray'))
    pyplot.show()

# use images with PIL
from PIL import Image

exampleDigit = Image.fromarray(train_X[0,:,:])
exampleDigit.show()

# checking class distribution
import numpy as np
unique, counts = np.unique(train_y, return_counts=True)
pyplot.bar(unique, counts)
unique, counts = np.unique(test_y, return_counts=True)
pyplot.bar(unique, counts)

pyplot.title('Class Frequency')
pyplot.xlabel('Class')
pyplot.ylabel('Frequency')
pyplot.show()

# image binarization
showExamples()
train_X[train_X>128] = 255
test_X[test_X>128] = 255
showExamples()

# histogram projection
def projectionHistogramVertical(img, show=False):
    projHist = np.zeros(img.shape[0],dtype=int)
    for i in range(img.shape[0]):
        projHist[i] = np.count_nonzero(img[:,i] == 255)
    if show:        
        f, (ax1, ax2) = pyplot.subplots(1, 2) 
        ax1.imshow(img,cmap=pyplot.get_cmap('gray'))
        ax2.bar(np.arange(len(projHist)),projHist)
        ax1.set_title("Digit")
        ax2.set_title("Vertical projection histogram")
        pyplot.show()
    return projHist

def projectionHistogramHorizontal(img, show=False):
    projHist = np.zeros(img.shape[0],dtype=int)
    for i in range(img.shape[1]):
        projHist[i] = np.count_nonzero(img[i,:] == 255)
    if show:        
        f, (ax1, ax2) = pyplot.subplots(1, 2) 
        ax1.imshow(img,cmap=pyplot.get_cmap('gray'))
        ax2.barh(np.arange(len(projHist)),projHist)
        ax1.set_title("Digit")
        ax2.set_title("Horizontal projection histogram")
        pyplot.show()
    return projHist

def projectionHistorgramXY(img, show=False):
    projHist = []
    for diff in range(1, img.shape[0]): 
        count = 0 
        for j in range(diff, img.shape[0]):
            if img[j][j-diff] == 0:
                count += 1
        projHist.append(count)
    projHist.reverse()

    count = 0
    for i in range(img.shape[0]):
        if img[i][i] == 255:
            count += 1
    projHist.append(count)

    for diff in range (1, img.shape[0]):
        count = 0
        for j in range(0, img.shape[0]-diff):
            if img[j][j+diff] == 0:
                count += 1
        projHist.append(count)

# i = np.argsort(test_y)
# test_X = test_X[i,:,:]  
digit = 3
x = 0
while x < 5:
    ind = random.randint(0,test_y.shape[0])
    
    if test_y[ind] == digit:
        print(ind)
        projectionHistorgramXY(test_X[ind],show=True)
        #projectionHistogramHorizontal(test_X[ind],show=True)
        x += 1
        
# feature extraction
features = []
for i in range(train_X.shape[0]):
    features.append(np.concatenate((projectionHistogramVertical(train_X[i]),
                    projectionHistogramHorizontal(train_X[i]))))

# test set features
featuresTest = []
for i in range(test_X.shape[0]):
    featuresTest.append(np.concatenate((projectionHistogramVertical(test_X[i]),
                    projectionHistogramHorizontal(test_X[i]))))

# classification
from sklearnex import patch_sklearn 
patch_sklearn()

from sklearn import svm, preprocessing
from sklearn.model_selection import GridSearchCV

# Grid Search
# print("Performing grid search ... ")
# # Parameter Grid
# #param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001, 0.00001, 10]}
# param_grid = {'C': [1, 10], 'gamma': [1, 0.01]}
# # Make grid search classifier
# clf_grid = GridSearchCV(svm.SVC(), param_grid, verbose=0)
# # Train the classifier
# clf_grid.fit(features, train_y)

features = preprocessing.scale(features)
featuresTest = preprocessing.scale(featuresTest)
clf = svm.SVC(C = 1.0, kernel='rbf', gamma=0.0001)
clf.fit(features, train_y)

# clf = grid.best_estimator_()
#print("Best Parameters:\n", clf_grid.best_params_)
print("Accuracy:\n%.2f"%(clf.score(featuresTest, test_y)*100))




