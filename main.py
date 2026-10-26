def read_sequence():
    """Read a sequence of numbers from the keyboard."""
    while True:
        text = input("Enter numbers separated by spaces: ")
        try:
            return [float(x) for x in text.split()]
        except ValueError:
            print("Invalid input. Please enter only numbers.")


def read_int(message):
    """Read a positive integer from the keyboard."""
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("The value must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def read_array():
    """Read a 2D array whose dimensions are given by the user."""
    rows = read_int("Number of rows: ")
    cols = read_int("Number of columns: ")
    array = []
    for i in range(rows):
        while True:
            text = input(f"Row {i + 1} ({cols} numbers separated by spaces): ")
            try:
                row = [float(x) for x in text.split()]
                if len(row) != cols:
                    print(f"You must enter exactly {cols} numbers.")
                    continue
                array.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter only numbers.")
    return array


def display_sequence(sequence):
    print("Sequence:", ", ".join(f"{x:g}" for x in sequence))


def display_array(array):
    print("Array:")
    for row in array:
        print("  " + " ".join(f"{x:8g}" for x in row))

def read_from_file():
    """Read a sequence of numbers from a text file named by the user."""
    filename = input("Enter the file name: ").strip()
    try:
        with open(filename, "r") as f:
            content = f.read()
        return [float(x) for x in content.split()]
    except FileNotFoundError:
        print(f"Error: the file '{filename}' does not exist.")
    except ValueError:
        print("Error: the file contains values that are not numbers.")
    return None

def main():
    while True:
        print("\n===== MENU =====")
        print("1. Read a sequence from the keyboard")
        print("2. Read an array from the keyboard")
        print("3. Read a sequence from a file")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_sequence(read_sequence())
        elif choice == "2":
            display_array(read_array())
        elif choice == "3":
            data = read_from_file()
            if data is not None:
                display_sequence(data)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()