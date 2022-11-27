from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV, train_test_split

from helpFunc import read_data, plot_data, plot_decision_function

# Read data
x, labels = read_data("pointsNoise_class_0.txt", "pointsNoise_class_1.txt")
#x, labels = read_data("points_class_0.txt", "points_class_1.txt")
# Split data to train and test on 80-20 ratio
X_train, X_test, y_train, y_test = train_test_split(x, labels, test_size = 0.2, random_state=0)

#uncomment for ploting training and test set
#print("Displaying data. Close window to continue.")
## Plot data
#plot_data(X_train, y_train, X_test, y_test)
C = 1
print("Training SVM with C=,",C)
# make a classifier and fit on training data
clf = svm.SVC(kernel='linear', C=C)
clf.fit(X_train, y_train)

print("Display decision function (C=",C,") ")
# Plot decision function on training and test data
plot_decision_function(X_train, y_train, X_test, y_test, clf)
print("Accuracy: {}%".format(clf.score(X_test, y_test) * 100 ))

