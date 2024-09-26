def raise_to(base, power):
    answer = base
    if power == 0:
        return 1
    elif power == 1:
        return answer
    else:
        for _ in range (1,power):
            answer = answer*base
        return answer

print(raise_to(4,4))