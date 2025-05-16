import numpy as np


class KNNRegression:
    def __init__(self):
        self.points = None
        self.N = 0
        self.k = 0

    def get_positive_int(self, prompt):
        while True:
            try:
                n = int(input(prompt))
                if n > 0:
                    return n
                else:
                    print("Please enter a positive number.")
            except:
                print("Invalid input. Please enter an integer.")

    def get_float(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except:
                print("Invalid input. Please enter a number.")

    def read_numbers(self, count):
        # Read count points (x,y)
        self.N = count
        self.points = np.zeros((count, 2))
        for i in range(count):
            x = self.get_float(f"Enter x for point {i+1}: ")
            y = self.get_float(f"Enter y for point {i+1}: ")
            self.points[i] = [x, y]

    def get_int(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except:
                print("Invalid input. Please enter an integer.")

    def search_number(self, target):
        if self.k > self.N:
            return None

        X = float(target)
        distances = np.abs(self.points[:, 0] - X)
        nearest_indices = np.argsort(distances)[:self.k]
        y_values = self.points[nearest_indices, 1]
        y_pred = np.mean(y_values)
        return y_pred

    def ask_exit(self):
        while True:
            answer = input("Do you want to exit? (yes/no): ").strip().lower()
            if answer in ["yes", "no"]:
                return answer == "yes"
            print("Invalid input. Please enter 'yes' or 'no'.")
