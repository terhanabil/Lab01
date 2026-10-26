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


def main():
    print("=== Sequence ===")
    seq = read_sequence()
    display_sequence(seq)

    print("\n=== Array ===")
    arr = read_array()
    display_array(arr)


if __name__ == "__main__":
    main()