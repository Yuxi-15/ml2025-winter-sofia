from module6_knn_regr import KNNRegression


def main():
    regression = KNNRegression()

    while True:
        count = regression.get_positive_int("How many numbers do you want to enter? ")
        regression.read_numbers(count)

        k = regression.get_positive_int("Enter k (number of neighbors): ")
        regression.k = k

        x = regression.get_float("Enter the number to predict Y for (X value): ")

        if k > count:
            print(f"Error: k ({k}) cannot be greater than N ({count}).")
        else:
            result = regression.search_number(x)
            print(f"Predicted Y value for X={x} using {k}-NN regression is: {result}")

        if regression.ask_exit():
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
