import numpy as np


class DataAnalytics:
    """NumPy Analyzer using OOP and NumPy functionality."""

    def __init__(self, array=None):
        self.__array = np.array(array) if array is not None else None

    # ---------------- Array Management ----------------
    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                n = int(input("Enter the number of elements: "))
                values = list(map(float, input(
                    f"Enter {n} elements separated by space: "
                ).split()))
                if len(values) != n:
                    print(f"Error: Please enter exactly {n} elements.")
                    return
                self.__array = np.array(values)

            elif choice == "2":
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                values = list(map(float, input(
                    f"Enter {rows * cols} elements for the array separated by space: "
                ).split()))
                if len(values) != rows * cols:
                    print(f"Error: Please enter exactly {rows * cols} elements.")
                    return
                self.__array = np.array(values).reshape(rows, cols)

            elif choice == "3":
                layers = int(input("Enter the number of layers: "))
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total = layers * rows * cols
                values = list(map(float, input(
                    f"Enter {total} elements for the array separated by space: "
                ).split()))
                if len(values) != total:
                    print(f"Error: Please enter exactly {total} elements.")
                    return
                self.__array = np.array(values).reshape(layers, rows, cols)

            else:
                print("Invalid choice.")
                return

            print("\nArray created successfully:")
            print(self.__array)

        except ValueError:
            print("Invalid input. Please enter numeric values.")

    def indexing_slicing(self):
        if self.__array is None:
            print("Please create an array first.")
            return

        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                try:
                    if self.__array.ndim == 1:
                        index = int(input("Enter the index: "))
                        print("Element:", self.__array[index])
                    else:
                        row = int(input("Enter the row index: "))
                        col = int(input("Enter the column index: "))
                        print("Element:", self.__array[row, col])
                except (ValueError, IndexError):
                    print("Invalid index.")

            elif choice == "2":
                try:
                    if self.__array.ndim != 2:
                        print("Slicing interface is implemented for 2D arrays.")
                        continue

                    row_range = input("Enter the row range (start:end): ")
                    col_range = input("Enter the column range (start:end): ")

                    r_start, r_end = map(int, row_range.split(":"))
                    c_start, c_end = map(int, col_range.split(":"))

                    sliced = self.__array[r_start:r_end, c_start:c_end]
                    print("\nSliced Array:")
                    print(sliced)
                except ValueError:
                    print("Invalid range. Use format start:end.")

            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    # ---------------- Mathematical Operations ----------------
    def mathematical_operations(self):
        if self.__array is None:
            print("Please create an array first.")
            return

        if self.__array.ndim != 2:
            print("Mathematical operations require a 2D array.")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        choice = input("Enter your choice: ").strip()

        try:
            if choice in {"1", "2", "3", "4"}:
                values = list(map(float, input(
                    f"Enter the same-size array elements ({self.__array.size} "
                    "elements separated by space): "
                ).split()))

                if len(values) != self.__array.size:
                    print("Error: Incorrect number of elements.")
                    return

                second = np.array(values).reshape(self.__array.shape)

                print("\nOriginal Array:")
                print(self.__array)
                print("\nSecond Array:")
                print(second)

                if choice == "1":
                    result = self.__array + second
                    operation = "Addition"
                elif choice == "2":
                    result = self.__array - second
                    operation = "Subtraction"
                elif choice == "3":
                    result = self.__array * second
                    operation = "Multiplication"
                else:
                    if np.any(second == 0):
                        print("Division by zero is not allowed.")
                        return
                    result = self.__array / second
                    operation = "Division"

                print(f"\nResult of {operation}:")
                print(result)

            elif choice in {"5", "6"}:
                rows, cols = self.__array.shape
                print(f"\nEnter {cols if choice == '5' else rows} "
                      "columns-compatible values for the second 2D array.")

                r2 = int(input("Enter rows of second array: "))
                c2 = int(input("Enter columns of second array: "))

                values = list(map(float, input(
                    f"Enter {r2 * c2} elements separated by space: "
                ).split()))

                if len(values) != r2 * c2:
                    print("Error: Incorrect number of elements.")
                    return

                second = np.array(values).reshape(r2, c2)

                if choice == "5":
                    if cols != r2:
                        print("Dot product requires first array columns = second array rows.")
                        return
                    print("\nDot Product:")
                    print(np.dot(self.__array, second))
                else:
                    if cols != r2:
                        print("Matrix multiplication requires first columns = second rows.")
                        return
                    print("\nMatrix Multiplication:")
                    print(np.matmul(self.__array, second))
            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid numeric input.")

    # ---------------- Combine / Split ----------------
    def combine_split(self):
        if self.__array is None:
            print("Please create an array first.")
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                if self.__array.ndim != 2:
                    print("Combine operation is demonstrated for 2D arrays.")
                    return

                rows, cols = self.__array.shape
                values = list(map(float, input(
                    f"Enter {rows * cols} elements for the second array: "
                ).split()))

                if len(values) != rows * cols:
                    print("Error: Incorrect number of elements.")
                    return

                second = np.array(values).reshape(rows, cols)
                print("\nOriginal Array:")
                print(self.__array)
                print("\nSecond Array:")
                print(second)

                print("\nCombined Vertically:")
                print(np.concatenate((self.__array, second), axis=0))

            elif choice == "2":
                if self.__array.ndim != 2:
                    print("Split operation is demonstrated for 2D arrays.")
                    return

                parts = int(input("Enter the number of equal parts: "))
                result = np.array_split(self.__array, parts, axis=0)

                print("\nSplit Arrays:")
                for i, part in enumerate(result, 1):
                    print(f"Part {i}:")
                    print(part)

            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input.")

    # ---------------- Search, Sort, Filter ----------------
    def search_sort_filter(self):
        if self.__array is None:
            print("Please create an array first.")
            return

        print("\nChoose an option:")
        print("1. Search")
        print("2. Sort Ascending")
        print("3. Sort Descending")
        print("4. Filter")

        choice = input("Enter your choice: ").strip()

        try:
            flat = self.__array.flatten()

            if choice == "1":
                value = float(input("Enter the value to search: "))
                positions = np.where(flat == value)[0]
                if len(positions):
                    print(f"Value {value} found at flattened index(es): {positions}")
                else:
                    print(f"Value {value} not found.")

            elif choice == "2":
                print("\nSorted Array (Ascending):")
                print(np.sort(flat))

            elif choice == "3":
                print("\nSorted Array (Descending):")
                print(np.sort(flat)[::-1])

            elif choice == "4":
                value = float(input("Filter values greater than: "))
                filtered = flat[flat > value]
                print(f"\nValues greater than {value}:")
                print(filtered)

            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid numeric input.")

    # ---------------- Statistics ----------------
    def statistics(self):
        if self.__array is None:
            print("Please create an array first.")
            return

        print("\nChoose a statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation Coefficient")

        choice = input("Enter your choice: ").strip()

        try:
            data = self.__array.flatten()

            if choice == "1":
                print("Sum of Array:", np.sum(data))
            elif choice == "2":
                print("Mean of Array:", np.mean(data))
            elif choice == "3":
                print("Median of Array:", np.median(data))
            elif choice == "4":
                print("Standard Deviation:", np.std(data))
            elif choice == "5":
                print("Variance:", np.var(data))
            elif choice == "6":
                print("Minimum Value:", np.min(data))
            elif choice == "7":
                print("Maximum Value:", np.max(data))
            elif choice == "8":
                p = float(input("Enter percentile (0-100): "))
                if not 0 <= p <= 100:
                    print("Percentile must be between 0 and 100.")
                    return
                print(f"{p}th Percentile:", np.percentile(data, p))
            elif choice == "9":
                values = list(map(float, input(
                    f"Enter {data.size} elements for the second array: "
                ).split()))
                if len(values) != data.size:
                    print("Error: Incorrect number of elements.")
                    return
                second = np.array(values)
                print("Correlation Coefficient:",
                      np.corrcoef(data, second)[0, 1])
            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input.")

    # ---------------- OOP Utility Methods ----------------
    @classmethod
    def from_list(cls, values):
        """Class method to create a DataAnalytics object from a list."""
        return cls(np.array(values))

    @staticmethod
    def show_project_info():
        print("\nNumPy Analyzer")
        print("A NumPy + OOP based data analysis toolkit.")

    # ---------------- Main Menu ----------------
    def run(self):
        self.show_project_info()

        while True:
            print("\n" + "=" * 45)
            print("Welcome to the NumPy Analyzer!")
            print("=" * 45)
            print("Choose an option:")
            print("1. Create a NumPy Array")
            print("2. Indexing and Slicing")
            print("3. Perform Mathematical Operations")
            print("4. Combine or Split Arrays")
            print("5. Search, Sort, or Filter Arrays")
            print("6. Compute Aggregates and Statistics")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.create_array()
            elif choice == "2":
                self.indexing_slicing()
            elif choice == "3":
                self.mathematical_operations()
            elif choice == "4":
                self.combine_split()
            elif choice == "5":
                self.search_sort_filter()
            elif choice == "6":
                self.statistics()
            elif choice == "7":
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    analyzer = DataAnalytics()
    analyzer.run()
