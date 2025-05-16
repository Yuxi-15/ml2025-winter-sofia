from module5_mod import NumberSearcher

def main():
    searcher = NumberSearcher()

    while True:
        count = searcher.get_positive_int("How many numbers do you want to enter? ")
        searcher.read_numbers(count)

        k = searcher.get_positive_int("Enter k (number of neighbors): ")
        searcher.k = k

        x = searcher.get_float("Enter the number to predict Y for (X value): ")

        if k > count:
            print(f"Error: k ({k}) cannot be greater than N ({count}).")
        else:
            result = searcher.search_number(x)
            print(f"Predicted Y value for X={x} using {k}-NN regression is: {result}")

        if searcher.ask_exit():
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
