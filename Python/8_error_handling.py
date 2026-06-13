# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")
#error handling with multiple except blocks
try:
    file = open('non_existent_file.txt')
    num = int("xyz")
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("Invalid value for conversion to integer!")

finally:
    print("This block will always execute.")
