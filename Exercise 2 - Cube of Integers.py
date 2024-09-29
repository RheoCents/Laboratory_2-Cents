# Steps:
# 1. Input the size of the array.
# 2. input the elements of the array
# 3. display the cube of each element

# Sample output

# Enter the size of the array : 3
# Enter the elements separated by space: 3 10 20
# 27
# 1000
# 8000
cube_list =[]
user_aray = int(input("How many numbers are we cubing? e.g. 3: "))
user_list = input("please input the numbers we are cubing: e.g. 1 20 33: ").split()
for i in range (user_aray):
    cube_list.append(int(user_list[i]))
for i in cube_list:
    print(int(i)**3)