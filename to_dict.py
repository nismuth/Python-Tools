# ToDict: takes a .txt file and converts its lines into a python dictionary to save the trouble

# Opens and reads the dict_make file
with open("dict_make.txt", "r") as file:
    lines = file.readlines()

# Creates an empty dictionary
data_dict = {}

# Processes each line
for line in lines:
    # Strips any whitespace or newline characters
    line = line.strip()

    # Skips empty lines
    if not line:
        continue

    # Splits by the first occurrence of a separator (assumes ':' as the separator)
    key_value = line.split(":", 1)

    # Ensures the line has both key(s) and value(s)
    if len(key_value) == 2:
        key = key_value[0].strip()
        value = key_value[1].strip()
        data_dict[key] = value

# Prints the dictionary in Python format
print("\ndata_dict =", data_dict)
