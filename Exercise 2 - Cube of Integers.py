try:
    cube_list =[]
    user_aray = int(input("How many numbers are we cubing? e.g. 3: "))
    user_list = input("please input the numbers we are cubing: e.g. 1 20 33: ").split()
    for i in range (user_aray):
        cube_list.append(int(user_list[i]))
    for i in cube_list:
        print(int(i)**3)
except ValueError:
    print('Please only input intigers')
except IndexError:
    print("Please match your given array")