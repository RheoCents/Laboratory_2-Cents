def right_triangle_printer():
    try: 
        user_n_input = int(input("How high do you want your triangle to be: "))
        for i in range (user_n_input,1,-1):
            print("*"*(i))
    except ValueError:
        print("Please only input")
        right_triangle_printer()
right_triangle_printer()