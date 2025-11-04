#   ### Problem 2

#     Write a Python program that:

#     1. Reads a line of integers from the user (separated by spaces).
#     2. Stores them in a **list** and calculates the **sum and average**.
#     3. Saves the list, sum, and average into a text file named **`numbers_data.txt`**.
#     4. Reads the contents of the file and prints them back to the user.

#     ---

 


# beginning 
num_sep_by_space = input('Numbers (Space separated):') # '10 20 30'
num_str_list = num_sep_by_space.split() #['10', '20', '30']
nums = []
for num_str in num_str_list:
    num = int(num_str)
    nums.append(num)
print(nums) # [10, 20, 30]

total = 0
for num in nums:
    total += num 
# end beginning 


# # easy
# nums = [int(num_str) for num_str in input('Numbers (Space separated):').split()]
# total = sum(nums)
# # end easy 

avg = total / len(nums) # 60 / 3 = 20

print(f'sum:{total}')
print(f'average:{avg}')

print('To/From file...')

with open('numbers_data.txt', 'w') as out_file:
    out_file.write(f'numbers list: {nums}\n')
    out_file.write(f'sum: {total}\n')
    out_file.write(f'average: {avg}\n')

with open('numbers_data.txt', 'r') as in_file:
    line1 = in_file.readline()
    line2 = in_file.readline()
    line3 = in_file.readline()
    print(line1, end='')
    print(line2, end='')
    print(line3, end='')


