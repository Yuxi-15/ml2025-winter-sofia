from module5_mod import NumberSearcher

def main():
    searcher = NumberSearcher()

    while True:
        count = searcher.get_positive_int("How many numbers do you want to enter? ")
        searcher.read_numbers(count)

        x = searcher.get_int("Enter the number to search for: ")
        index = searcher.search_number(x)

        if index == -1:
            print("-1 (Sorry, the number is not found)")
        else:
            print(f"Your search number is at index {index}")

        if searcher.ask_exit():
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
