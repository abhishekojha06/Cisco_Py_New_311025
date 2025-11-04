#    Write a Python program that:

#     1. Reads a list of names from the user (separated by spaces).
#     2. Sorts the names alphabetically and stores them in a list.
#     3. Converts the list into a tuple.
#     4. Saves the sorted list and tuple into a file named **`names_data.txt`**.
#     5. Reads and prints the saved data from the file.

#     ---

user_inp = input("Enter the user")

user = user_inp.split()
user_list = list(user)
sorted_user = sorted(user_list)

user_tuple = tuple(user_list)

#create file

with open('names_data.txt', 'w') as output_file:
    output_file.write(f"List: {user}\n")
    output_file.write(f"Sorted List: {sorted_user}\n")
    output_file.write(f"Tuple: {user_tuple}\n")

with open('names_data.txt', 'r') as in_file:
    print(in_file.readline())
    print(in_file.readline())
    print(in_file.readline())