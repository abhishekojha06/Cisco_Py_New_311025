
    # Write a Python program that:

    # 1. Accepts a sentence from the user.
    # 2. Splits the sentence into words and stores them in a **list**.
    # 3. Converts all words to **uppercase** and stores them in a **tuple**.
    # 4. Saves both the list and tuple into a file named **`sentence_data.txt`**.
    # 5. Reads back the data from the file and displays it on the screen.

sentence = input("Enter the Sentence") # input line

words_list = list(sentence.split()) # split and convert to list
words_upper = [word.upper() for word in words_list] # words upper and iterate through for loop
words_tuple = tuple(words_upper) # save in tuple


# open file as outputfile
with open('sentence_data.txt','w') as output_file:
    output_file.write(f"List: {words_list}\n")
    output_file.write(f"Tuple: {words_tuple}\n")

#for read file \n use for next line

with open('sentence_data.txt','r') as input_file:
    print(input_file.readline())
    print(input_file.readline())





