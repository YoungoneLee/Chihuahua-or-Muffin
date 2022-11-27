from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV

from helpFunc import read_data, plot_data, plot_decision_function

# Read data
x, labels = read_data("pointsGS_class_0.txt", "pointsGS_class_1.txt")
# Split data to train and test on 80-20 ratio
X_train, X_test, y_train, y_test = train_test_split(x, labels, test_size = 0.2, random_state=0)

#uncomment for plotting training and test dataset
#print("Displaying data. Close window to continue")
## Plot data 
plot_data(X_train, y_train, X_test, y_test)

print("Training SVM ...")
# make a classifier
#change Gamma and C parameters
#clf = svm.SVC(C = 1000.0, kernel='linear')

clf = svm.SVC(C = 1.0, kernel='rbf', gamma=50)

# Train classifier
clf.fit(X_train, y_train)

clf_predictions = clf.predict(X_train)
print("Accuracy training:\n%.2f"%(clf.score(X_train, y_train)*100))

# Make predictions on unseen test data
clf_predictions = clf.predict(X_test)
print("Accuracy:\n%.2f"%(clf.score(X_test, y_test)*100))

print("Displaying decision function")
# Plot decision function on training and test data
plot_decision_function(X_train, y_train, X_test, y_test, clf)
