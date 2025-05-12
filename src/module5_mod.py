class NumberSearcher:
    def __init__(self):
        self.numbers = []

    def get_positive_int(self, n):
        while True:
            try:
                value = int(input(n))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def get_int(self, n):
        while True:
            try:
                return int(input(n))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def read_numbers(self, count):
        self.numbers = []
        for i in range(count):
            num = self.get_int(f"Enter number {i + 1}: ")
            self.numbers.append(num)

    def search_number(self, target):
        if target in self.numbers:
            return self.numbers.index(target) + 1  # 1-based index
        return -1

    def ask_exit(self):
        while True:
            answer = input("Do you want to exit? (yes/no): ").strip().lower()
            if answer in ["yes", "no"]:
                return answer == "yes"
            print("Invalid input. Please enter 'yes' or 'no'.")
