def get_int(prompt, positive_only=False):
    while True:
        try:
            value = int(input(prompt))
            if positive_only and value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def read_numbers(count):
    return [get_int(f"Enter number {i + 1}: ") for i in range(count)]

def search_number(numbers, target):
    try:
        return numbers.index(target) + 1  # 1-based index
    except ValueError:
        return -1

def ask_exit():
    while True:
        answer = input("Do you want to exit? (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    while True:
        n = get_int("Enter how many you want to input: ", positive_only=True)
        numbers = read_numbers(n)
        x = get_int("Enter your search number: ")
        result = search_number(numbers, x)
        print(f"Your search number location is at index {result}" if result != -1 else "-1 (Sorry, the number is not found)")

        if ask_exit():
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
