from sklearn import svm
from sklearn.model_selection import train_test_split
#import help functions for ploting and reading data (helpFunc.py must be in the same folder as this code)
from helpFunc import read_data, plot_data, plot_decision_function
# Read data (files must be in the same folder as this code)
x, labels = read_data("points_class_0.txt", "points_class_1.txt")

# Split data to train and test on 80-20 ratio (change test_size for different ration: test_size = 0.2)
X_train, X_test, y_train, y_test = train_test_split(x, labels, test_size = 0.2, random_state=0)

#uncomment for seeing training and test set
#print("Displaying data.")  
# Plot traning and test data
# plot_data(X_train, y_train, X_test, y_test)

print('Training Linear SVM')
#parameters of SVM classifier can be found at:
#https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
# Create a linear SVM classifier 
clf = svm.SVC(kernel='linear')

# Train classifier 
clf.fit(X_train, y_train)
print("Displaying decision function.")  
# Plot decision function on training and test data
plot_decision_function(X_train, y_train, X_test, y_test, clf)

# Make predictions on unseen test data
clf_predictions = clf.predict(X_test)
print("Accuracy: {}%".format(clf.score(X_test, y_test) * 100 ))