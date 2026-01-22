import numpy as np

class DataAnalytics:
    def __init__(self):
        self.array = None

    def create_array(self):
        dim = int(input("Enter array dimension (1 or 2): "))

        if dim == 1:
            n = int(input("Enter number of elements: "))
            elements = list(map(int, input("Enter elements: ").split()))
            self.array = np.array(elements)
        elif dim == 2:
            r = int(input("Enter rows: "))
            c = int(input("Enter columns: "))
            elements = list(map(int, input(f"Enter {r*c} elements: ").split()))
            self.array = np.array(elements).reshape(r, c)
        else:
            print("Invalid dimension")

        print("Array created:\n", self.array)

    def indexing_slicing(self):
        print("\n1. Indexing\n2. Slicing")
        choice = int(input("Choose option: "))

        if choice == 1:
            i = int(input("Enter index: "))
            print("Element:", self.array[i])

        elif choice == 2:
            r = input("Row range (start:end): ").split(":")
            c = input("Column range (start:end): ").split(":")
            sliced = self.array[int(r[0]):int(r[1]), int(c[0]):int(c[1])]
            print("Sliced Array:\n", sliced)

    def math_operations(self):
        print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
        ch = int(input("Choose operation: "))

        elements = list(map(int, input("Enter same size array elements: ").split()))
        arr2 = np.array(elements).reshape(self.array.shape)

        if ch == 1:
            print("Result:\n", self.array + arr2)
        elif ch == 2:
            print("Result:\n", self.array - arr2)
        elif ch == 3:
            print("Result:\n", self.array * arr2)
        elif ch == 4:
            print("Result:\n", self.array / arr2)

    def combine_split(self):
        print("\n1. Combine\n2. Split")
        ch = int(input("Choose: "))

        if ch == 1:
            arr2 = np.array(list(map(int, input("Enter elements: ").split()))).reshape(self.array.shape)
            print("Combined:\n", np.concatenate((self.array, arr2)))

        elif ch == 2:
            n = int(input("Number of splits: "))
            print("Splitted Arrays:", np.array_split(self.array, n))

    def search_sort_filter(self):
        print("\n1.Search\n2.Sort\n3.Filter")
        ch = int(input("Choose: "))

        if ch == 1:
            val = int(input("Value to search: "))
            print("Found at positions:", np.where(self.array == val))

        elif ch == 2:
            print("Sorted Array:\n", np.sort(self.array))

        elif ch == 3:
            val = int(input("Filter values greater than: "))
            print("Filtered:\n", self.array[self.array > val])

    def statistics(self):
        print("Sum:", np.sum(self.array))
        print("Mean:", np.mean(self.array))
        print("Median:", np.median(self.array))
        print("Std Dev:", np.std(self.array))
        print("Variance:", np.var(self.array))
        print("Min:", np.min(self.array))
        print("Max:", np.max(self.array))
        print("Percentile (50%):", np.percentile(self.array, 50))

    @classmethod
    def info(cls):
        print("NumPy Analyzer using OOP Principles")

    @staticmethod
    def exit_program():
        print("Thank you for using NumPy Analyzer! have a good day!")
        exit()

def main():
    obj = DataAnalytics()
    DataAnalytics.info()

    while True:
        print("\n===== NumPy Analyzer =====")
        print("1.Create Array")
        print("2.Indexing & Slicing")
        print("3.Math Operations")
        print("4.Combine / Split")
        print("5.Search / Sort / Filter")
        print("6.Aggregates & Statistics")
        print("7.Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            obj.create_array()
        elif choice == 2:
            obj.indexing_slicing()
        elif choice == 3:
            obj.math_operations()
        elif choice == 4:
            obj.combine_split()
        elif choice == 5:
            obj.search_sort_filter()
        elif choice == 6:
            obj.statistics()
        elif choice == 7:
            DataAnalytics.exit_program()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()