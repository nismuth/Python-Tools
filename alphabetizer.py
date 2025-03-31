# Alphabetizer: sorts words alphabetically through the terminal or file input

print("\nWelcome to the Alphabetizer.")

# Asks the user for input method
read_choice = input("\nWill you be inputting through the terminal or a file? (T for terminal / F for file): ").upper()

input_list = []

if read_choice == "T":
    # Gets command to use terminal
    input_vals = input("Enter what you need to alphabetize, separated by commas:\n").split(", ")
    input_list.extend(input_vals)  # Adds individual elements from prior input

elif read_choice == "F":
    # Gets file name
    file_name = input("Enter the file name (include extension, ex. input.txt): ")
    try:
        with open(file_name, "r") as file:
            # Strips and reads lines through a list
            input_list.extend([line.strip() for line in file.readlines()])
    except FileNotFoundError:  # Exception for file reading error
        print("Error: File not found.")
        exit()

# Sorts the list alphabetically - no extra steps needed
input_list.sort()

# Prints the alphabetized list
print("\nAlphabetized List:")
for item in input_list:
    print(item)

