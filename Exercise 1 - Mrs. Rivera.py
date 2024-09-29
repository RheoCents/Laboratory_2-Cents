def raise_to(base, power):
    if power < 0:
        raise ValueError("Exponent should be a non-negative integer.")
    answer = base
    if power == 0:
        return 1
    elif power == 1:
        return answer
    else:
        for _ in range(1, power):
            answer = answer * base
        return answer

def initilization():
    try:
        user_base = int(input("What is your base? "))
        user_exponent = int(input('What number should we raise it to? '))

        print(raise_to(user_base, user_exponent))

    except ValueError:
        print("Please enter an integer value for both the base and the exponent.")
        initilization()

initilization()