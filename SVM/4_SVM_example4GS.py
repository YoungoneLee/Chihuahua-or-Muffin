from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV

from helpFunc import read_data, plot_data, plot_decision_function

# Read data
x, labels = read_data("pointsGS_class_0.txt", "pointsGS_class_1.txt")
# Split data to train and test on 80-20 ratio
X_train, X_test, y_train, y_test = train_test_split(x, labels, test_size = 0.2, random_state=0)

# Grid Search
print("Performing grid search ... ")
# Parameter Grid
#param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001, 0.00001, 10]}
param_grid = {'C': [0.5, 0.8, 1, 5, 10], 'gamma': [0.1, 0.01, 0.05]}
# Make grid search classifier
clf_grid = GridSearchCV(svm.SVC(), param_grid, verbose=1)
# Train the classifier
clf_grid.fit(X_train, y_train)

# clf = grid.best_estimator_()
print("Best Parameters:\n", clf_grid.best_params_)
print("Accuracy:\n%.2f"%(clf_grid.score(X_test, y_test)*100))

print("Displaying decision function for best estimator.")
# Plot decision function on training and test data
plot_decision_function(X_train, y_train, X_test, y_test, clf_grid)