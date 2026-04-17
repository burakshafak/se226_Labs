import math


def circle_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    return math.pi * radius ** 2

def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return width * height

def triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return 0.5 * base * height



def remove_duplicates(data_list):
    return list(set(data_list))

def strip_whitespaces(string_list):
    return [item.strip() for item in string_list]

def calculate_mean(num_list):
    return sum(num_list) / len(num_list)

def find_maximum(num_list):
    return max(num_list)

def find_minimum(num_list):
    return min(num_list)



def main():
    print("1. Shape Calculator")
    print("2. Data Analyzer")

    choice = int(input("Choose an option (1 or 2): "))

    
    if choice == 1:
        print("\nSelect operation:")
        print("1. Circle Area")
        print("2. Rectangle Area")
        print("3. Triangle Area")

        op = int(input("Enter operation number: "))

        try:
            if op == 1:
                r = float(input("Enter radius: "))
                result = circle_area(r)

            elif op == 2:
                w = float(input("Enter width: "))
                h = float(input("Enter height: "))
                result = rectangle_area(w, h)

            elif op == 3:
                b = float(input("Enter base: "))
                h = float(input("Enter height: "))
                result = triangle_area(b, h)

            else:
                raise ValueError("Invalid operation number")

            print("Result:", round(result, 2))

        except ValueError as e:
            print("Input Error:", e)

    
    elif choice == 2:
        user_input = input("Enter comma-separated numbers: ")

        try:
            string_list = user_input.split(",")
            cleaned = strip_whitespaces(string_list)
            numbers = [float(x) for x in cleaned]

            unique_numbers = remove_duplicates(numbers)

            print("Cleaned data:", unique_numbers)
            print("Mean:", round(calculate_mean(unique_numbers), 2))
            print("Max:", find_maximum(unique_numbers))
            print("Min:", find_minimum(unique_numbers))

        except ValueError:
            print("Data Error: Please enter only numbers.")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
