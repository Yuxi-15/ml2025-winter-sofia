# module8_metrics-scikit.py

import numpy as np
from sklearn.metrics import precision_score, recall_score

def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")
        except:
            print("Invalid input. Please enter an integer.")

def get_binary_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value == 0 or value == 1:
                return value
            else:
                print("Input must be 0 or 1.")
        except:
            print("Invalid input. Please enter 0 or 1.")

def ask_exit():
    while True:
        answer = input("\nDo you want to exit? (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def run_evaluation():
    n = get_positive_int("Enter the number of data points: ")

    data = np.zeros((n, 2), dtype=int)

    for i in range(n):
        actual = get_binary_input(f"Enter x (actual value 0 or 1) for data point {i+1}: ")
        predicted = get_binary_input(f"Enter y (predicted value 0 or 1) for data point {i+1}: ")
        data[i] = [actual, predicted]

    y_true = data[:, 0]
    y_pred = data[:, 1]

    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    print("\nResults:")
    print(f"Precision: {precision:.2f}")
    print(f"Recall:    {recall:.2f}")

def main():
    while True:
        run_evaluation()
        if ask_exit():
            print("Goodbye~")
            break
        else:
            print("Let's calculate another dataset!\n")

if __name__ == "__main__":
    main()
