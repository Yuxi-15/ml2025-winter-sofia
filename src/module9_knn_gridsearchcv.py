import numpy as np
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def ask_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except:
            print("Invalid input. Please enter a number.")

def ask_non_negative_int(message):
    while True:
        try:
            value = int(input(message))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except:
            print("Invalid input. Please enter a number.")

def ask_float(message):
    while True:
        try:
            return float(input(message))
        except:
            print("Invalid input. Please enter a number.")

def ask_exit():
    while True:
        answer = input("\nDo you want to exit the program? (yes/no): ").strip().lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("Please type 'yes' or 'no'.")

def read_data_pairs(count, label):
    data = np.zeros((count, 2))
    for i in range(count):
        x = ask_float(f"Enter x (feature) for {label} point {i+1}: ")
        y = ask_non_negative_int(f"Enter y (label) for {label} point {i+1}: ")
        data[i] = [x, y]
    return data

def get_cv_folds(y):
    counts = Counter(y)
    return min(5, min(counts.values()))

def run_classifier():
    print("\n------ kNN ------")

    num_train = ask_positive_int("Enter number of training points: ")
    train_data = read_data_pairs(num_train, "training")
    X_train = train_data[:, 0].reshape(-1, 1)
    y_train = train_data[:, 1]

    num_test = ask_positive_int("Enter number of test points: ")
    test_data = read_data_pairs(num_test, "test")
    X_test = test_data[:, 0].reshape(-1, 1)
    y_test = test_data[:, 1]

    cv_folds = get_cv_folds(y_train)

    if cv_folds < 2:
        print("Not enough samples per class to use cross-validation.")
        print("Using default k = 1.")
        model = KNeighborsClassifier(n_neighbors=1)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print("\n=== Results ===")
        print("Used default k = 1")
        print(f"Test accuracy: {accuracy:.2f}")
        return

    param_grid = {'n_neighbors': list(range(1, 11))}
    model = KNeighborsClassifier()
    search = GridSearchCV(model, param_grid, cv=cv_folds)
    search.fit(X_train, y_train)

    # Test on test set
    best_k = search.best_params_['n_neighbors']
    best_model = search.best_estimator_
    predictions = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("\n------Here Is The Result ------")
    print(f"Best k: {int(best_k)}")
    print(f"Test accuracy: {accuracy:.2f}")

def main():
    while True:
        run_classifier()
        if ask_exit():
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
