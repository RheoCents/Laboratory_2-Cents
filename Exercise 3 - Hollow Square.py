def hollow_square_maker():
    try:
        user_integer_input = int(input("Please enter the size of the box: "))
        for i in range(user_integer_input):
            if i == 0 or i == user_integer_input - 1:
                print('x' * (user_integer_input-1))
            else:
                print('x' + ' ' * (user_integer_input) + 'x')
    except ValueError:
        print("Please enter an intiger")

hollow_square_maker()